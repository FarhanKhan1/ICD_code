import mysql.connector
import pandas as pd
class Connection:
    def __init__(self):
            self.conn = mysql.connector.connect(host = 'localhost', port = '3306', user = 'root', password = '', database = "testing")
            self.cursor = self.conn.cursor()
            self.query = "select * from student"
            self.cursor.execute(self.query)
            self.df = pd.DataFrame(self.cursor.fetchall())

    def get_data(self):
        for row in self.df:
            print(f"Roll_no: {row[0]} and Name: {row[1]} and gender: {row[3]}" )

    def total_rows(self):
        return self.cursor.rowcount

