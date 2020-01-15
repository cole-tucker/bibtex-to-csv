import bibtexparser

def read_file(filename):
    with open('bibtex.bib') as bibtex_file:
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
    for entry in bib_database:
        entrytype = entry['ENTRYTYPE']
        title = entry['title']
        authors = entry['author'].split(',')
        parse_author(authors)

def parse_author(authors):
        for author in authors:
            author = bibtexparser.customization.splitname(author)
            if not author['jr']:
                author = ' '.join(author['von']) + ' ' + ' '.join(author['last']) + ', ' + ' '.join(author['first'])
            else:
                author = ' '.join(author['von']) + ' ' + ' '.join(author['last']) + ', ' + ' '.join(author['jr']) + ', ' + ' '.join(author['first'])
            print(author.strip(' ,'))

def main():
    bib_database = read_file('bibtex.bib')
    parse_bib_database(bib_database)

main()