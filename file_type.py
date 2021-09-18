import os

XML47File = 'xml47 package file'
RSMFile = 'compiled program as embeddable rust source code'


ASMFile = 'assembly file'
DOTFile = 'graphviz dot file'

UnknownFile = 'unknown file type'

def file_type(file_path):
    file_name, extension = os.path.splitext(file_path)
    if extension == '.x47':
        return XML47File
    elif extension == '.rsm':
        return RSMFile
    elif extension == '.a47':
        return ASMFile
    elif extension == '.dot':
        return DOTFile
    else:
        return UnknownFile