import bibtexparser
import csv

def read_file(filename):
    with open(filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries

def year_filter(bib_database, year):
    new_bibs = []
    for entry in bib_database:
        if entry['year'] == year:
            new_bibs.append(entry)

def year_range_filter(bib_database, yr):
    new_bibs = []
    for entry in bib_database:
        if entry['year'] >= yr[0] and entry['year'] <= yr[1]:
            new_bibs.append(entry)

def parse_bib_database(bib_database):
    db_list = [['Title', 'Name', 'Organization']]
    for entry in bib_database:
        if not 'author' in entry.keys():
            entry['author'] = ''
        else:
            authors = entry['author'].split(' and ')
            authors = parse_author(authors)
        if 'organization' in entry.keys():
            organization = entry['organization'].replace('\\', '')
        if 'school' in entry.keys():
            organization = entry['school'].replace('\\', '')
        if 'institution' in entry.keys():
            organization = entry['institution'].replace('\\', '')
        if 'publisher' in entry.keys():
            organization = entry['publisher'].replace('\\', '')
        
        for author in authors:
            author = author.strip()
            if author != 'others,':
                single_entry = []
                single_entry.append(entry['title'])
                single_entry.append(author)
                single_entry.append(organization)
                db_list.append(single_entry)
    return sorted(db_list)

def parse_author(authors):
    author_list = []
    for author in authors:
        author = bibtexparser.customization.splitname(author)
        author = bibtexparser.customization.convert_to_unicode(author)
        author_list.append(author['last'][0] + ', ' + ' '.join(author['first']))
        
    return author_list

def main():
    bib_database = read_file(input('Input filename: '))
    db_list = parse_bib_database(bib_database)

    with open("output.csv", "w", newline="") as output:
        writer = csv.writer(output)
        writer.writerows(sorted(db_list, key=lambda row: row[1].upper(), reverse=False))

main()