
from airtest.core.api import connect_device

win_app = connect_device("Windows:///")

def connect_app(process_id=None):
    def _c(pid):
        try:
            win_app.connect(process=pid)
            win_app._top_window.set_focus()
            return True
        except:
            return False
    if process_id is None:
        return None
    if isinstance(process_id, set):
        for pid in process_id:
            if _c(pid):
                return pid
    else:
        if _c(process_id):
            return process_id
        else:
            return None

