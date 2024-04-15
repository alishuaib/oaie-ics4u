from IPython.display import display
from ipywidgets import Output

action_log = Output()

def log(message): 
    with action_log:
        print(message)

def display_log():
    display(action_log)