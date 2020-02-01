from cx_Freeze import setup, Executable

base = None    

executables = [Executable("FirstKeylogger.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "My First Key Logger",
    options = options,
    version = "1.0.0",
    description = 'This is my first attempt at creatining a user/noob friendly Key Logger',
    executables = executables
)
