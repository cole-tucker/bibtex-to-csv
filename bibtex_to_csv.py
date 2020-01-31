import bibtexparser
import csv

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

def year_range_filter(bib_database, year1, year2):
    new_bibs = []
    for entry in bib_database:
        if 'year' in entry.keys():
            if int(entry['year']) >= year1 and int(entry['year']) <= year2:
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

def main():
    # bib_database = read_file(input('Input filename: '))
    # year_input = input('Year Filter? "Y start, end" OR "Y year" ')
    bib_database = read_file('test/test.bib')
    year_input = 'y 1958'

    # Single year filter
    if year_input[0].upper() == 'Y' and len(year_input) == 6:
        bib_database = year_filter(bib_database, int(year_input[-4:]))
    # Year range filter
    if year_input[0].upper() == 'Y' and len(year_input) == 12:
        bib_database = year_range_filter(bib_database, int(year_input[-10:-6]), int(year_input[-4:]))

    db_list = parse_bib_database(bib_database)
    # Sort on author
    db_list[1:] = sorted(db_list[1:], key=lambda row: row[0].upper(), reverse=False)

    with open("output.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerows(db_list)

main()