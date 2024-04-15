from ..cls.stats import Attack, Health
from ..cls.entity import Entity
from ..cls.event import Event
from render.action_log import log
class Inventory:
    pass

class Player(Entity):
    """Animations frames for idle, run, attack, start_battle, end_battle, guard, dead, crouch, search"""
    _states = {
        "idle": "assets/player/idle.gif",
        "run": "assets/player/run.gif",
        "attack": "assets/player/attack.gif",
        "start_battle": "assets/player/start_battle.gif",
        "end_battle": "assets/player/end_battle.gif",
        "guard": "assets/player/guard.gif",
        "dead": "assets/player/dead.gif",
        "crouch": "assets/player/crouch.gif",
        "search": "assets/player/search.gif"
    }
    _base_width = 50
    _base_height = 37

    EVENT_KEYS = {
        "attack" : "attack"
    }
    
    def __init__(self,scale=1):
        super().__init__(scale,) 
        self.event = Event(list(self.EVENT_KEYS.keys()))
        #Define health bar
        self.hp = Health(max=10)

        #Define attack 
        self.atk = Attack(attack=1)

        #Define Animation Events for Health
        # self.hp.event[self.hp.EVENT.health_down] = lambda: self.set_state("crouch",repeat=False,fallback="idle")
        self.hp.event['guard_start'] = lambda: self.set_state("guard",repeat=False,fallback="idle")
        self.hp.event['guard_end'] = lambda: self.set_state("idle",repeat=True)
        self.hp.event['dodge_start'] = lambda: self.set_state("guard",repeat=False,fallback="idle")
        self.hp.event['dodge_end'] = lambda: self.set_state("idle",repeat=True)
        self.hp.event['dead'] = lambda: [
            self.set_state("dead",repeat=True),
            log("> 💀 Player has fallen"),
            log("XX GAME OVER XX")
        ]

        #Define Animation Events for Player
        self.event['attack'] = lambda: [
            self.set_state("attack",repeat=False,fallback="idle",move='right'),
        ]

    def attack(self, enemy):
        """
        Take an Enemy object and reduce it's health by the players attack level
        """
        if self.hp.current <= 0: return
        self.event['attack']()
        remaining_hp,amount = enemy.hp.health_down(self.atk.current)
        log(f">> 💥 Player attacked for {amount} [🖤 {remaining_hp}/{enemy.hp.max_health}]")
    
    def guard(self):
        """
        Reduce incoming damage by half
        """
        self.hp.guard()
        log(">> 🛡️ Player is guarding")

    def dodge(self):
        """
        A chance to dodge an incoming attack and completely avoid damage
        50% chance
        """
        self.hp.dodge()
        log(">> 🦵 Player is preparing to dodge")

    def new(self):
        self.hp.new(10)
        self.atk.new(1)
        self.set_state("idle",repeat=True)