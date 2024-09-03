import openpyxl
import pandas as pd


def data_reader(sheet_name):
    data = []
    workbook = openpyxl.load_workbook('C:/Users/manju/OneDrive/Desktop/data.xlsx')
    sheet = workbook[sheet_name]
    total_rows = sheet.max_row
    total_columns = sheet.max_column
    for row in range(2, total_rows + 1):
        for column in range(1, total_columns + 1):
            data.append(sheet.cell(row, column).value)
    return data


def excel_to_dictionary(sheet_name):
    df = pd.read_excel('C:/Users/manju/OneDrive/Desktop/data.xlsx', sheet_name=sheet_name, engine='openpyxl')
    data_dict = dict(zip(df['variable'], df['value']))
    return data_dict


