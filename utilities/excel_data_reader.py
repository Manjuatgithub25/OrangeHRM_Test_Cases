import openpyxl


def data_reader():
    data = []
    workbook = openpyxl.load_workbook('C:/Users/manju/OneDrive/Desktop/login.xlsx')
    sheet = workbook['login_credentials']
    total_rows = sheet.max_row
    total_columns = sheet.max_column
    for row in range(2, total_rows + 1):
        for column in range(1, total_columns + 1):
            data.append(sheet.cell(row, column).value)
    return data
