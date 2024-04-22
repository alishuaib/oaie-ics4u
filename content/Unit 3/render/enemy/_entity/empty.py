from ...cls.entity import Entity

class Empty(Entity):
    """Entity class for no display"""
    _states = {
        "idle": "assets/enemy/empty.gif",
        "attack" : "assets/enemy/empty.gif",
        "dead" : "assets/enemy/empty.gif",
    }
    _base_width = 25
    _base_height = 25

    attack = 1
    health = 1
    
    def __init__(self,scale=2):
        super().__init__(scale)

  