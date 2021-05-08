import loader
import scraper
from typing import Callable, Dict

def _show_all():
    """
    show all influencers in local influencers.JSON 
    """
    gen=loader.local.getlist()
    for i in gen:
        print(i.get('name',{}))
        print(i.get('ig',{}))

def _err():
    """
    error function called if the operation passed is missing
    """
    print('operation not available')

def _exit():
    """
    close the CLI
    """
    exit()
    
def _help():
    """
    print available commands
    """
    print("Commands list: \n\n")
    for valid_op in op_list:
        print('\u25A2 ',f'{valid_op}:\n{op_list[valid_op].__doc__}')


op_list: Dict[str, Callable] = {
    'show_all': _show_all,
    'exit':_exit,
    'help': _help
}