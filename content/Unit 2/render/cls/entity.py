import ipywidgets as widgets
import threading as th
from PIL import Image

def get_total_gif_duration(file_path):
    gif = Image.open(file_path)
    total_duration = 0
    while True:
        total_duration += gif.info['duration']
        try:
            gif.seek(gif.tell() + 1)
        except EOFError:
            break
    return total_duration/1000

class Entity:
    _states = {
        "idle": ""
    }
    _base_width = 0
    _base_height = 0

    def __init__(self,scale, debug = False):
        self.current_state = "idle"
        self.width = str(self._base_width * scale)+"px"
        self.height = str(self._base_height * scale)+"px"

        self.animate_timer = None
        self.state_timer = None
        self._timers = {}
        self._durations = {}
        
        self._get_duration()        

        self.image = widgets.Image(
            value=open(self._states[self.current_state], "rb").read(), 
            format='gif', 
            layout=widgets.Layout(
                width=self.width, 
                height=self.height
            )
        )

        self.container = widgets.HBox(
            [self.image], 
            layout=widgets.Layout(
                justify_content='center' , 
                align_items='center' , 
                width=self.width, 
                height=self.height
            )
        ).add_class("ani_container")

        if debug: self.container.add_class("debug")

    def set_state(self, state, repeat=True, fallback="idle", move=None):
        """Set the current state of the animation
        state: str - the new state to set
        repeat: bool - if the animation should repeat
        fallback: str - the state to fallback to after the animation completes if repeat is False
        """
        #If state is not in list of states, raise error
        if state not in self._states.keys():
            raise ValueError(f"Invalid state\n{self._states.keys()}")
        
        #Wait for current state animation to finish
        if self.state_timer and self.state_timer.is_alive():
            while self.state_timer.is_alive():
                pass


        self.current_state = state # Set current state to new state
        self._new_render()
        if not repeat:
            self._set_timer(fallback=fallback)
        if move:
            self._animate_action(move)

    def _animate_action(self,move):
        if self.animate_timer:
            self.animate_timer.cancel()
            self.animate_timer = None
        self.container.add_class(f"bounce_{move}")
        self.animate_timer = th.Timer(1, self.container.remove_class, args=[f"bounce_{move}"])
        self.animate_timer.start()
        

    def render(self):
        return self.container
        
    def _new_render(self, state=None):
        #If no state is passed, set state to current state
        if state:
            self.current_state = state
        self.image.value = open(self._states[self.current_state], "rb").read()

    def _set_timer(self, fallback):
        #Set a new timer to fallback when current state animation ends
        if self.state_timer:
            self.state_timer.cancel()
            self.state_timer = None
        self.state_timer = th.Timer(
            self._durations[self.current_state], 
            self._new_render,
            args=[fallback]
        )
        self.state_timer.start()
    
    def _get_duration(self):
        for state in self._states:
            duration = get_total_gif_duration(self._states[state])
            self._durations[state] = duration
        