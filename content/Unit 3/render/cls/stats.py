from .event import Event

import ipywidgets as widgets
import random

class Attack:
    current = 1

    def __init__(self,attack=1):
        self.current = attack

    def new(self,attack=1):
        self.current = attack

    def attack_up(self,value=1):
        self.current += value
        return self.current,value
    
    def attack_down(self,value=1):
        self.current = max(1, self.current - value)
        return self.current,value
    

class Health:
    max_health = None
    current = None

    health_bar = None

    is_guard = False
    is_dodge = False

    EVENT_KEYS = {
        "guard_start": "guard_start",
        "guard_end": "guard_end",
        "dodge_start": "dodge_start",
        "dodge_end": "dodge_end",
        "health_up": "health_up",
        "health_down": "health_down",
        "dead": "dead"
    }

    def __init__(self,max=10,style="danger"):
        self.max_health = max
        self.current = max
        self.event = Event(list(self.EVENT_KEYS.keys()))

        self.health_bar = widgets.IntProgress(
            value=self.current, 
            min=0, 
            max=self.max_health,
            bar_style=style
        ).add_class('ui_health')
        
    def render(self):
        return self.health_bar
    
    def new(self,max,style="danger"):
        """Set up a new health instance without recreating widget"""
        self.max_health = max
        self.current = max

        self.health_bar.max = self.max_health
        self.health_bar.value = self.current
        self.health_bar.bar_style = style
    
    def max_up(self,value):
        self.max_health += value
        self.current = min(self.max_health, self.current + value)
        self.on_change() 
        return self.max_health,value
    
    def max_down(self,value):
        self.max_health = max(1, self.max_health - value)
        self.current = min(self.max_health, self.current)
        self.on_change() 
        return self.max_health,value
    
    def health_up(self,value):
        self.event['health_up']()
        self.current = min(self.max_health, self.current + value)
        self.on_change() 
        return self.current,value
    
    def health_down(self,value):
        self.event['health_down']()
        value = self._check(value)
        self.current -= value   
        self.on_change()     
        return self.current,value
    
    def guard(self):
        self.event['guard_start']()
        self.is_guard = True
        return self.is_guard
    

    def dodge(self):
        self.event['dodge_start']()
        self.is_dodge = True
        return self.is_dodge

    def _check(self,value):
        if self.is_guard:
            self.event['guard_end']()
            self.is_guard = False
            return value // 2
        elif self.is_dodge:
            self.event['dodge_end']()
            self.is_dodge = False
            success = random.choice([False,True])
            if success:
                return 0
            else:
                return value
        return value
    
    def on_change(self):
        #Update health bar widget
        self.health_bar.max = self.max_health
        self.health_bar.value = self.current

    def on_loop(self):
        

        #Check if entity is dead
        if self.current <= 0:
            self.event['dead']()

        #Reset guard and dodge
        if self.is_guard:
            self.event['guard_end']()
            self.is_guard = False
        if self.is_dodge:
            self.event['dodge_end']()
            self.is_dodge = False
            
    