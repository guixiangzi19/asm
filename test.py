from utils.excel_handler import *


trans_list=get_trans_data(web_platform="neteller")
trans_len = len(trans_list)
for i in trans_list:
    data=""
    for k,v in i.items():
        data += str(k)+':'+str(v)+'    '
    print(data)