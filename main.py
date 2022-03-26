from openpyxl import load_workbook

ExcelFile = load_workbook("sampleData.xlsx")

print(ExcelFile.sheetnames)
