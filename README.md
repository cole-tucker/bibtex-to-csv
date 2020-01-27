# bibtex-to-csv
This program takes a BibTeX file and converts the name, title, organizational affiliation, and year into a csv file

### How to run:
1. Go into your Command Line Interface (Terminal for Mac, Command Prompt for Windows, etc.)
2. Go to the project directory
3. Run the command below
```python
python3 ./bibtex_to_csv.py
```

4. It will ask for a filename. Make sure that file is in the same directory as the program, or you know how to handle directories from the command line.

5. It will ask for a year filter. Following the question with "Y YYYY" or "Y YYYY, YYYY" will filter the file to only output records in the respective years. Any other input will result in the program running for all years. **It must be in the correct format or else the program will not recognize the years.**