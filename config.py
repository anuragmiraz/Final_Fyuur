import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# My Change starts
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:doublea@localhost:5432/fyuur'
# My Change ends