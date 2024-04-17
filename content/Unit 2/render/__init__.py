from .demo import show_demo

import ipywidgets as widgets
BACKGROUND = widgets.Image(
    value=open("assets/ui/header/5.png", "rb").read(),
    format='png'
).add_class('parent_bg')

class Label(widgets.Label):
    def __init__(self, value, *args, **kwargs):
        super().__init__(value, *args, **kwargs)
        self.add_class('ui_label')

