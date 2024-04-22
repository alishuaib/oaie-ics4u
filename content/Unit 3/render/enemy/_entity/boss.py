from ...cls.entity import Entity

class Boss(Entity):
    """Entity class for boss"""
    _states = {
        "idle": "assets/enemy/boss.gif",
        "attack" : "assets/enemy/boss_attack.gif",
        "dead": "assets/enemy/boss_dead.gif"
    }
    _base_width = 43
    _base_height = 43

    attack = 2
    health = 10
    
    def __init__(self,scale=4):
        super().__init__(scale) 

    