from ...cls.entity import Entity

class Slime(Entity):
    """Entity class for slime"""
    _states = {
        "idle": "assets/enemy/slime.gif",
        "attack" : "assets/enemy/slime_attack.gif",
        "dead": "assets/enemy/slime_dead.gif"
    }
    _base_width = 32
    _base_height = 25

    attack = 1
    health = 5
    
    def __init__(self,scale=3):
        super().__init__(scale)

  