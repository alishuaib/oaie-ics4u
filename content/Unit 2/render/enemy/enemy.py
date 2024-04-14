from ..enemy import _entity
from ..cls.stats import Attack, Health
from ..cls.event import Event
import ipywidgets as widgets

class Enemy:        
    other = {
        "empty": _entity.Empty()
    }
    boss = {
        "boss": _entity.Boss(scale=3)
    }
    normal = {
        "slime":_entity.Slime(scale=3)
    }

    _all_entities = {**other, **boss, **normal}
    _all_views = {key: value.render() for key, value in _all_entities.items()}

    EVENT_KEYS = {
        "attack" : "attack"
    }



    def __init__(self, enemy="empty"):
        self.event = Event(list(self.EVENT_KEYS.keys()))
        self.hp = Health(max=1)
        self.atk = Attack(attack=1)
        self.container = widgets.Stack(
            list(self._all_views.values()), 
            selected_index=0
        ).add_class('enemy_stack')  
        
        self.new(enemy)


    def attack(self, player):
        """
        Take an Player object and reduce it's health by the enemy attack level
        """
        if self.hp.current <= 0: return
        self.event['attack']()
        remaining_hp,amount = player.hp.health_down(self.atk.current)
        print(f"<< 🔪 Enemy attacked for {amount} [💖 {remaining_hp}/{player.hp.max_health}]")
    
    def new(self,enemy):
        if enemy not in list(self._all_entities.keys()):
            raise ValueError(f"Enemy {enemy} not found")
        
        self.enemy = self._all_entities[enemy]
        self.current = enemy
        self.hp.new(self.enemy.health,style="warning")
        self.atk.new(self.enemy.attack)

        #Death Event
        self.hp.event['dead'] = lambda: [
            self.enemy.set_state("dead",repeat=True),
            print(">> Enemy Defeated")
        ]

        #Attack Event
        self.event['attack'] = lambda: [
            self.enemy.set_state("attack",repeat=False,fallback="idle",move='left'),
        ]

        self.container.selected_index =  list(self._all_views.keys()).index(enemy)

    def render(self):
        return self.container