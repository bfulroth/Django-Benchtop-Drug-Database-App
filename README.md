[![Build Status](https://travis-ci.com/bfulroth/Django-Benchtop-Drug-Database-App.svg?branch=master)](https://travis-ci.com/bfulroth/Django-Benchtop-Drug-Database-App)

[![Maintainability](https://api.codeclimate.com/v1/badges/12c98d78c674d643f3a6/maintainability)](https://codeclimate.com/github/bfulroth/Django-Benchtop-Drug-Database-App/maintainability)

<a href="https://codeclimate.com/github/bfulroth/Django-Benchtop-Drug-Database-App/test_coverage"><img src="https://api.codeclimate.com/v1/badges/12c98d78c674d643f3a6/test_coverage" /></a>

# Django-Benchtop-Drug-Database-App

The purpose of this app is to take some of the pain and frustration away from tracking of drugs recieved at the lab bench for testing.

## Getting Started

- Open terminal on your mac.
- cd into the directory where you want to install this app.
- Fork this repo:
  - cmd: git clone https://github.com/bfulroth/Django-Benchtop-Drug-Database-App.git
- Install pipenv
  - cmd: pip install pipenv
- Create a new Pipenv environment with all of the dependencies needed for this app.
  - cmd: pipenv install

## Loading Initial Data

Data must be correctly formatted and persisted in an amazon s3 bucket in csv format.

- cmd: python manage.py load_initial_data

Note: That this cmd can be run for a batch upload of new drug locations.

**Warning**
If you need to purge the backend database of all data: (This cannot be reversed).

- cmd: python manage.py purge_sqllite_db

## Running the Django Server locally

- cmd: python manage.py runserver

The server will be running locally at default port http://127.0.0.1:8000/
Copy and paste the url above into the browser of your choice.

## Using the App

See the home page at the link above for navigation.
