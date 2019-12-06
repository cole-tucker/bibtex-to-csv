import bibtexparser

def read_file(filename):
    with open('test.bib') as bibtex_file:
        bibtex_str = bibtex_file.read()
    bib_database = bibtexparser.loads(bibtex_str)
    return bib_database.entries

def parse_bib_database(bib_database):
    for entry in bib_database:
        authors = entry['author'].split(',')
        entry['author'] = [val.strip() for val in set(authors)]
    print(bib_database)

def main():
    bib_database = read_file('test.bib')
    parse_bib_database(bib_database)

main()