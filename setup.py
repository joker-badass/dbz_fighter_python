import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
   name = "DBZ GAME",
   options = {'build_exe': {'packages' :['pygame'],
                            'include_files' : ['image','song']}},
   executables = executables                         
)