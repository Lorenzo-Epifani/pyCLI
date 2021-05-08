import loader.local
import os
print('\u2523',__name__)
root=f'{os.path.abspath("./")}/{__name__}'


def print_tree(_depth,_root):
    _depth+=1
    this_dir=next(os.walk(_root))
    for _file in this_dir[2]:
        if(_file != '__init__.py'):
            print('\u2523','\u2501\u2501'*_depth,_file)
    for dir in this_dir[1]: 
        print('\u2523','\u2501\u2501'*_depth,dir)
        print_tree(_depth,f'{_root}/{dir}')

print_tree(0,root)
