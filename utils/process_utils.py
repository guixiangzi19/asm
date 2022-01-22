import subprocess

from subprocess import check_output

import pythoncom
from win32com.client import GetObject

def process_is_exists(name="PokerHub.exe"):
    wmi = GetObject("winmgmts:")
    process_code = wmi.ExecQuery(f'select * from Win32_Process where Name="{name}"')
    if len(process_code)>0:
        return True
    else:
        return False


def shell(cmd):
    stdout, stderr = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = stdout if stdout else stderr

    try:
        return o.decode("utf-8")
    except:
        return ""

def get_process_pid(name="chrome.exe") ->set:
    pid_list = set()
    wmi = GetObject("winmgmts:")
    process_code = wmi.ExecQuery(f'select * from Win32_Process where Name="{name}"')
    if process_code and len(process_code) > 0:
        for process_info in process_code:
            pid_list.add(process_info.ProcessId)
    return pid_list

def kill_process(name=None, pid=None):
    if pid:
        if isinstance(pid, list):
            for p in pid:
                shell(f"TASKKILL /PID {p} /T /F")
        else:
            shell(f"TASKKILL /PID {pid} /T /F")

    if name:
        shell(f"TASKKILL /IM {name} /T /F")
