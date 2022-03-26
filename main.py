from openpyxl import load_workbook
import mysql.connector
import pandas

ExcelFile = load_workbook("sampleData.xlsx")
sheet = ExcelFile.active
rows = sheet.rows
headers = [cell.value for cell in next(rows)]


for row in rows:
    ##to check very row
    data = {}
    ##empty dictionary of data
    for title, cell in zip(headers, row):
        data[title] = cell.value
    print(data)



##mySQL connection
database = mysql.connector.connect(

        host = "sql11.freemysqlhosting.net",
        user = "sql11480583",
        password = "pa8DiBz9bc"

)
cursor = database.cursor()


##creating a table on Mysql
cursor.execute(" CREATE TABLE SampleData(First_Name VARCHAR (255),"
               " Last_Name VARCHAR (255), Company_Name(255), Address(255), City(255),"
               "Region(255), Phone_Number(15),Email(255), Web(255) )")






