from pathlib   import Path
from importlib import import_module as import_


def clean(string):
    if   'binary' in string: string = string.replace('binary', 'binary ')
    elif 'odd'    in string: string = string.replace('odd'   , 'odd-'   )
    
    return string.replace('Sort', '')


folder = 'algorithms'

files  = (i.stem for i in Path(folder).iterdir())
files  = ((i, import_(f'{folder}.{i}')) for i in files if 'Sort' in i)

algorithmsDict = {clean(i): vars(j)[i] for i, j in files}
    
