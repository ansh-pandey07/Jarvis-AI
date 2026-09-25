import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\anshhacker\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\anshhacker\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("Hotward.py", base=base, icon="icon.ico")]


cx_Freeze.setup(
    name = "Anshpad Text Editor",
    options = {"build_exe": {"packages":["pyqt5","os"], "include_files":["jarvis.py",'tcl86t.dll','tk86t.dll']}},
    version = "0.1",
    description = "Tkinter Application",
    executables = executables
    )