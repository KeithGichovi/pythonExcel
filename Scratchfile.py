
from openpyxl import load_workbook
import mysql.connector
import mysql


database = mysql.connector.connect(

    host="localhost",
    user="root",
    database="datafromcode"

)
cursor = database.cursor()

cursor.execute(" CREATE TABLE DataFromCode1(First_Name VARCHAR (255),"
               " Last_Name VARCHAR (255), Company_Name VARCHAR (255), Address VARCHAR (255), City VARCHAR (255),"
               "Region VARCHAR (255), Phone_Number INT (15),Email VARCHAR(255) PRIMARY KEY  , Web VARCHAR(255) )")

ExcelFile = load_workbook("sampleData.xlsx")
sheet = ExcelFile.active
rows = sheet.rows
headers = [cell.value for cell in next(rows)]

for row in rows:

    data = {}

    for title, cell in zip(headers, row):
        data[title] = cell.value

    cursor.execute("INSERT INTO DataFromCode VALUES data[title.0],data[title.1],data[title.2], data[title.3], "
                   "data[title.4],data[title.5],data[title.6], data[title.7], data[title.8]")

    database.commit()


