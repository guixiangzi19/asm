# from utils.excel_handler import *
#
#
# trans_list=get_trans_data(web_platform="neteller")
# trans_len = len(trans_list)
# for i in trans_list:
#     data=""
#     for k,v in i.items():
#         data += str(k)+':'+str(v)+'    '
#     print(data)
# import os
# import time
# import tkinter
# import tkinter.ttk
# import tkinter.messagebox as messagebox
# from tkinter.filedialog import askdirectory
#
# # 定义log
# import logging
# logger = logging.getLogger('info')
# logger.setLevel(logging.INFO)
# logger_handle = logging.FileHandler(os.path.join(os.getcwd(), 'upload_test.log'))
# logger.addHandler(logger_handle)
#
#
# # 选择文件夹
# def select_file_dir(ev, file_dir_input):
#     upload_file_dir = askdirectory(title='选择文件夹')
#     file_dir_input.delete(0, tkinter.END)
#     file_dir_input.insert(0, upload_file_dir)
#
#
# # button1 回调函数
# def create_test1():
#     file_dir = file_dir_input.get()  # 获取文件目录
#     module_flag = var.get()  # 获取radiobutton的值
#     if not file_dir:
#         messagebox.showinfo('提示', '请选择文件夹')
#         return False
#
#
# # button2 回调函数
# def create_test2():
#     file_dir = file_dir_input.get()  # 获取文件目录
#     module_flag = var.get()  # 获取radiobutton的值
#     if not file_dir:
#         messagebox.showinfo('提示', '请选择文件夹')
#         return False
#
#     # 文件上传进度条
#     canvas = tkinter.Tk()
#     canvas.title("文件上传进度")
#     progressbarOne = tkinter.ttk.Progressbar(canvas, length=300, value=0)
#     progressbarOne.pack(pady=20)
#     progressbarOne['value'] = 0
#
#     for key in range(20):
#         progressbarOne['value'] = key
#         canvas.update()
#         time.sleep(1)
#
#     canvas.destroy()
#
# # tkinter框口定义
# top = tkinter.Tk()
# top.title('文件上传')
# top.minsize(350, 200)
# top.maxsize(350, 200)
# top.grid_rowconfigure(4, minsize=46)
# top.grid_rowconfigure(5, minsize=46)
#
# # tkinter窗口内容定义
# var = tkinter.IntVar()
# var.set(1)
# exe_one = tkinter.Label(top, text='1.提示信息').grid(row=0)
# exe_two = tkinter.Label(top, text='2.提示信息').grid(row=1)
# exe_three = tkinter.Label(top, text='3.提示信息').grid(row=2)
# module_flag_one = tkinter.Radiobutton(top, variable=var, text='one', value=1)
# module_flag_one.grid(row=3)
# module_flag_two = tkinter.Radiobutton(top, variable=var, text='two', value=2)
# module_flag_two.grid(row=3, column=1)
# file_dir_input = tkinter.Entry(top)
# file_dir_input.grid(row=4, column=1, sticky="ew")
# select_but = tkinter.Button(top, text='选择文件夹')
# select_but.bind("<Button-1>", lambda event: select_file_dir(event, file_dir_input))
# select_but.grid(row=4)
#
# conn_db = tkinter.Button(top, text="button1", command=create_test1).grid(row=5)
# file_up = tkinter.Button(top, text="button2", command=create_test2).grid(row=5, column=1)
#
# top.mainloop()



import tkinter as tk
from tkinter import filedialog


def upload_file():
    selectFile = tk.filedialog.askopenfilename()
    entry1.insert(0, selectFile)
    print('上传的文件为: {}'.format(entry1.get()))


root = tk.Tk()

frm = tk.Frame(root)
frm.grid(padx='20', pady='30')
btn = tk.Button(frm, text='上传文件', command=upload_file)
btn.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
entry1 = tk.Entry(frm, width='40')
entry1.grid(row=0, column=1)

root.mainloop()
