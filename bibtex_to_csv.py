import os
import bibtexparser
import csv
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Users/coletucker/dev/repos/bibtex-to-csv/'
ALLOWED_EXTENSIONS = {'bib'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(request.form)
            if request.form['year'] != '':
                year_input = request.form['year']
            else:
                year_input = 'n'
            main(filename, year_input)
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('index.html')

def read_file(filename):
    with open(filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=bibtexparser.bparser.BibTexParser(common_strings=True))

    return bib_database.entries

def handle_year(years):
    year_mil_cen = years[0][:2]
    year_start = int(years[0][-2:])
    year_end = int(years[-1][-2:])

    if int(year_start) > int(year_end):
        last_cen_years = [year_mil_cen + str(i) for i in range(year_start, 100)]
        this_cen_years = [str(int(year_mil_cen) + 1) + str(i) for i in range(0, year_end)]

        return last_cen_years.append(this_cen_years)

    return [year_mil_cen + str(i) for i in range(year_start, year_end + 1)]

def year_filter(bib_database, year):
    new_bibs = []
    for entry in bib_database:
        if 'year' in entry.keys():
            year_split = entry['year'].split('--')
            if len(year_split) > 1:
                if str(year) in handle_year(year_split):
                    new_bibs.append(entry)
            else:
                if str(year) == entry['year']:
                    new_bibs.append(entry)

    return new_bibs

def year_range_filter(bib_database, year_range):
    new_bibs = []
    for entry in bib_database:
        if 'year' in entry.keys():
            year_split = entry['year'].split('--')
            if len(year_split) > 1:
                year_list = handle_year(year_split)
                for year in year_range:
                    if str(year) in year_list:
                        new_bibs.append(entry)
            else:
                for year in year_range:
                    if str(year) in entry['year']:
                        new_bibs.append(entry)

    return new_bibs

def parse_bib_database(bib_database):
    db_list = [['Name', 'Title', 'Organization', 'Year of Publication']]
    for entry in bib_database:
        if 'organization' in entry.keys():
            organization = entry['organization'].replace('\\', '')
        if 'school' in entry.keys():
            organization = entry['school'].replace('\\', '')
        if 'institution' in entry.keys():
            organization = entry['institution'].replace('\\', '')
        if 'publisher' in entry.keys():
            organization = entry['publisher'].replace('\\', '')

        if 'year' in entry.keys():
            year = entry['year']
        else:
            year = ''
        
        if 'author' in entry.keys():
            authors = entry['author'].split(' and ')
            authors = parse_author(authors)
            for author in authors:
                author = author.strip()
                if author != 'others,':
                    single_entry = []
                    single_entry.append(author)
                    single_entry.append(entry['title'])
                    single_entry.append(organization)
                    single_entry.append(year)
                    db_list.append(single_entry)

        else:
            authors = ''
            single_entry = []
            single_entry.append(authors)
            single_entry.append(entry['title'])
            single_entry.append(organization)
            single_entry.append(year)
            db_list.append(single_entry)
    return db_list

def parse_author(authors):
    author_list = []
    for author in authors:
        author = bibtexparser.customization.splitname(author)
        author = bibtexparser.customization.convert_to_unicode(author)
        author_list.append(author['last'][0] + ', ' + ' '.join(author['first']))
        
    return author_list

def main(filename, year_input):
    # bib_database = read_file(input('Input filename: '))
    # year_input = input('Year Filter? "Y start, end" OR "Y year" ')
    bib_database = read_file(filename)
    year_input = year_input.split('-')
    # year_input = 'n'

    # Single year filter
    if len(year_input) == 1 and len(year_input[0]) == 4:
        bib_database = year_filter(bib_database, int(year_input[0]))
    # Year range filter
    if len(year_input) == 2:
        if int(year_input[1]) < int(year_input[2]):
            year_range = [i for i in range(int(year_input[0]), int(year_input[1]) + 1)]
        else:
            ...
        bib_database = year_range_filter(bib_database, year_range)

    db_list = parse_bib_database(bib_database)
    # Sort on author
    db_list[1:] = sorted(db_list[1:], key=lambda row: row[0].upper(), reverse=False)

    with open("output.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerows(db_list)

# main()