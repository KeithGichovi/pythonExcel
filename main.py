from openpyxl import load_workbook

ExcelFile = load_workbook("sampleData.xlsx")
sheet = ExcelFile.active
rows = sheet.rows

headers = [cell.value for cell in next(rows)]
##print(headers)

for row in rows:
    data = {}
    for title, cell in zip(headers, row):
        data[title] = cell.value

    print(data)
