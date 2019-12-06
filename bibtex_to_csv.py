import bibtexparser

def read_file(filename):
    with open('bibtex.bib') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    return bib_database.entries

def year_filter(bib_database, year):
    pass

def parse_bib_database(bib_database):
    for entry in bib_database:
        authors = entry['author'].split(',')
        entry['author'] = [val.strip() for val in set(authors)]
    print(bib_database)

def main():
    bib_database = read_file('bibtex.bib')
    parse_bib_database(bib_database)

main()