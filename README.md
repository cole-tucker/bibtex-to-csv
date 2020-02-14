# bibtex-to-csv
This program takes a BibTeX file and converts the name, title, organizational affiliation, and year into a csv file

### How to run:
1. Clone this repo to desired location.
1. Go into your Command Line Interface (Terminal for Mac, Command Prompt for Windows, etc.)
2. Go to the project directory
3. You will need to setup Flask for this project. To do so you will need to create a virtual environment for this project:
```
On Mac:
python3 -m venv [ENV NAME]

If you are using Python 2:
python2 -m virtualenv [ENV NAME]


On Windows:
py -3 -m venv [ENV NAME]

If you are using Python 2:
\Python27\Scripts\virtualenv.exe [ENV NAME]
```

3. Do not make a new project folder
4. In the command line, run
```
. [VENV_NAME]/bin/activate
pip install -r requirements.txt
```

5. Open bibtex_to_csv.py and change the `UPLOAD_FOLDER` to your project directory
6. Finally, run `export FLASK_APP=bibtex_to_csv` whenever you start your environment and `flask run` to start your server

Go to localhost:[Port Specified in Command Line] in desired browser
You will now have a local server up and running. In bibtex_to_csv.py, change the UPLOAD_FOLDER variable to desired path. To refresh the server after a code change, run `flask run` again.