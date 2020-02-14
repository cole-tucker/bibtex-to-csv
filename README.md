# bibtex-to-csv
This program takes a BibTeX file and converts the name, title, organizational affiliation, and year into a csv file

### How to run:
1. Go into your Command Line Interface (Terminal for Mac, Command Prompt for Windows, etc.)
2. Go to the project directory
3. You will need to setup Flask for this project. Goto the below link to install.
`https://flask.palletsprojects.com/en/1.1.x/installation/#virtual-environments` and install the virtual environment.
4. In the command line, run
```
pip install -r requirements.txt
. [VENV_NAME]/bin/activate
export FLASK_APP=bibtex_to_csv
flask start
```

You will now have a local server up and running. In bibtex_to_csv.py, change the UPLOAD_FOLDER variable to desired path. To refresh the server after a code change, run `flask run` again.