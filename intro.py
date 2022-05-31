import time 
import pandas as pd
from test import Connection
import mysql.connector
#import pymssql
from flask import Flask, render_template
conn = Connection()
app = Flask(__name__)

# conn = mysql.connector.connect(host = 'localhost', port = '3306', user = 'root', password = '', database = "testing")
# cursor = conn.cursor()
# query = "select * from student"
# cursor.execute(query)
# df = cursor.fetchall()
data = {'Farhan': 'Teacher', 'Waqar':'Student', 'Ejaz':'Student'}
@app.route("/")

def hello_world():
    
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about_us.html', name = data)

@app.route("/contact")
def contact_us():
    return render_template('contact_us.html')

@app.route("/blog")
def blog():
    return render_template('Blogs.html')    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


