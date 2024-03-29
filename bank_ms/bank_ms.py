import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

if __name__ == '__main__':
    app.run()
