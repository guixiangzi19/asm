import os
import pandas as pd
import xlwt, xlrd, openpyxl
from xlutils.copy import copy
from datetime import datetime
from utils.constains import *


def create_folder(path):
    if os.path.exists(path):
        return
    else:
        os.makedirs(path)


def create_file(filename, sheet_name, table_header: list):
    if os.path.exists(filename):
        return
    else:
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet1 = workbook.add_sheet(sheet_name)
        for i in range(len(table_header)):
            sheet1.write(0, i, table_header[i])
        workbook.save(filename)


def get_transactions_file_name(web_platform: str):
    day = datetime.today().strftime("%Y%m%d")
    month = datetime.today().strftime("%Y%m")
    excel_name = day + ".xls"
    for m in payment_methods:
        if web_platform.lower() == m:
            filepath = os.path.join(os.path.dirname(__file__), f'../data/{m}/', month)
    return filepath, os.path.join(filepath, excel_name)


def get_bind_file_name(web_platform: str):
    excel_name = f"{web_platform}_eg_bind.xls"
    filepath = os.path.join(os.path.dirname(__file__), f'../resource/bind/')
    return filepath, os.path.join(filepath, excel_name)


def before_append_data(path, filename, sheet_name, table_header):
    create_folder(path)
    create_file(filename, sheet_name, table_header)


def append_transactions_xlsx(web_platform: str, content: list):
    path, filename = get_transactions_file_name(web_platform)
    print(path)
    print(filename)
    sheet_name = "transactions"
    table_header = transactions_table_header
    before_append_data(path, filename, sheet_name, table_header)
    df_old = pd.DataFrame(pd.read_excel(filename, sheet_name))
    row_old = df_old.shape[0]
    df = pd.DataFrame(content)
    workbook = openpyxl.load_workbook(filename)
    writer = pd.ExcelWriter(filename, engine='openpyxl')
    writer.book = workbook
    writer.sheets = dict((ws.title, ws) for ws in workbook)
    df.to_excel(writer, sheet_name=sheet_name, startrow=row_old + 1, index=False, header=False)
    writer.save()


def append_transactions_xls(web_platform: str, content: list):
    path, filename = get_transactions_file_name(web_platform)
    sheet_name = "transactions"
    table_header = transactions_table_header
    before_append_data(path, filename, sheet_name, table_header)
    rows_append = len(content)
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_name(sheet_name)
    rows_old = worksheet.nrows
    cols_old = worksheet.ncols
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)

    for i in range(rows_append):
        transaction = content[i]
        for j in range(0, cols_old):
            key = worksheet.cell_value(rowx=0, colx=j)
            new_worksheet.write(i + rows_old, j, transaction.get(key))

    new_workbook.save(filename)


def append_bind_xls(web_platform: str, content: list):
    path, filename = get_bind_file_name(web_platform)
    sheet_name = web_platform.lower()
    table_header = bind_table_header
    before_append_data(path, filename, sheet_name, table_header)
    rows_append = len(content)
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_name(sheet_name)
    rows_old = worksheet.nrows
    cols_old = worksheet.ncols
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(rows_append):
        transaction = content[i]
        for j in range(0, cols_old):
            key = worksheet.cell_value(rowx=0, colx=j)
            new_worksheet.write(i + rows_old, j, transaction.get(key))
    new_workbook.save(filename)

    #加一个写缓存的方法


def get_data_from_excel(path, sheet_name):
    dt = pd.read_excel(path, sheet_name=sheet_name).to_dict()
    payload_lst = []
    for i in range(len(list(dt.values())[0])):
        payload = {}
        for k, v in dt.items():
            k = k.lower()
            if pd.isnull(v.get(i)):
                continue
            payload[k] = v.get(i)
        payload_lst.append(payload)
    return payload_lst


def get_bind_data(web_platform: str):
    path, filename = get_bind_file_name(web_platform)
    sheet_name = web_platform.lower()
    return get_data_from_excel(filename, sheet_name)


def get_trans_data(web_platform: str):
    path, filename = get_transactions_file_name(web_platform)
    sheet_name = "transactions"
    return get_data_from_excel(filename, sheet_name)


# https://blog.csdn.net/m0_43437756/article/details/121866578?spm=1035.2023.3001.6557&utm_medium=distribute.pc_relevant_bbs_down.none-task-blog-2~default~OPENSEARCH~default-11.nonecase&depth_1-utm_source=distribute.pc_relevant_bbs_down.none-task-blog-2~default~OPENSEARCH~default-11.nonecase

# content = [{"transaction_id": "333", "email": "297177459@168.com", "game_id": "111111", "mount": "100", 'unit': "usd",
#             "chips": "200", "state": "fail"}, ]
#
content1 = [{"transaction_id": "444", "email": "00007459@168.com", "game_id": "", "amount": "100", 'unit': "usd",
             "chips": "200","date":"Dec 25 2021,3:43 PM","state": "fail"}, ]
#


append_transactions_xls(web_platform='skrill', content=content1)
# append_transactions_xls(web_platform='ecopayz', content=content)
# append_transactions_xls(web_platform='neteller', content=content)
#
# content3=[{"email": "297177459@168.com", "game_id": "4444"}, ]
#
#
# append_bind_xls('skrill',content3)
# append_bind_xls('ecopayz',content3)
# append_bind_xls('neteller',content3)
#
# a=get_bind_data('skrill')
# b=get_trans_data('skrill')
# print(a)
# print(b)