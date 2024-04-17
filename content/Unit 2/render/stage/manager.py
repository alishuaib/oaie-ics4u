import ipywidgets as widgets

class LevelManager:    
    class Meter:
        __frames = [
            "assets/ui/fire_green/loop.gif",
            "assets/ui/fire_orange/loop.gif",
            "assets/ui/fire_blue/loop.gif",
            "assets/ui/fire_white/loop.gif",
            "assets/ui/fire_purple/loop.gif",
        ]
        def __init__(self):            
            meter = [] # List of Image objects for each frame stack
            for index in range(len(self.__frames)):
                hold = []
                for i in range(5):
                    if i <= index: # If the index is less than or equal to the current level then show image
                        obj = widgets.Image(value=open(self.__frames[i], "rb").read()).add_class('stage')
                    else: # Otherwise show a blank box
                        obj= widgets.HTML(value="<span/>").add_class('stage')
                    hold.append(obj)
                meter.append(hold)
            stack = [widgets.HBox(m).add_class('stage_stack') for m in meter]
            self.container = widgets.Stack(stack,selected_index=0).add_class('ui_meter_stack')
            self.step_label = widgets.Label(value="Stage: "+str(self.container.selected_index+1)).add_class('stage_label')
       
        def set_index(self, i):
            self.container.selected_index = i

        def render(self):            
            self.step_label.value = "Stage: "+str(self.container.selected_index+1)
            meter_box = widgets.VBox([self.container , self.step_label]).add_class('ui_meter')
            return meter_box

    class Stage:
        __frames = [
            "assets/bg/forest.png",
            "assets/bg/desert.png",
            "assets/bg/cave.png",
            "assets/bg/mountain.png",
            "assets/bg/city.png"
        ]
        def __init__(self):
            self.container = widgets.Stack([
                widgets.Image(value=open(frame, "rb").read()).add_class('bg') for frame in self.__frames
            ],selected_index=0).add_class('bg_stack')
        def set_index(self, i):
            self.container.selected_index = i

        def render(self):
            return self.container

    
            
    def __init__(self , level=-1):
        self.level = level
        self.stage = self.Stage()
        self.meter = self.Meter()
        pass

    def _update(self):
        self.stage.set_index(self.level)
        self.meter.set_index(self.level)
        
    def stage_up(self):
        if self.level < 4:            
            self.level += 1
            self._update()

    def reset(self):
        self.level = -1
        # self._update()
    
    def on_loop(self):
        # Increment the step
        self.stage_up()