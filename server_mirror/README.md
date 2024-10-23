# Server Mirror

## Purpose
A replicate of the server files maintaining the database for demonstration purposes.

## Setup
A basic/free PythonAnywhere account is not capable of running the server, so a paid account of $5.25 is the minimum cost to operate properly ($5 account plus $0.25 of an extra 1gb storage).

Playwright needs to be installed (though, it might be already installed.) `Playwright install` is necessary to update chromium and other dependencies, and this causes storage to exceed 1gb.

I created a flask web app and located where the flask_app.py would be located (i.e., '/mysite'). The WSGI file needs to be reviewed and modified, if necessary.

## Usage
Server conducts the information scraping four times a day and populates a database which is exported into a .csv file that the local repo will download and conduct comparisons to.