import render
from render.style import apply_style
from render.player import Player
from render.enemy import Enemy
from render.stage import LevelManager

import ipywidgets as widgets
from IPython.display import display
import random
from render.action_log import log , display_log

def show_demo():
        #Load CSS Styling
    apply_style()


    #Level Manager 
    manager = LevelManager()
    background = manager.stage.render()
    stage = manager.meter.render()

    player = Player()
    enemy = Enemy()

    #Health / Level UI
    health_label = render.Label(value='💖')
    health_bar = player.hp.render()
    enemy_label = render.Label(value='🖤')
    enemy_bar = enemy.hp.render()

    ui_box = widgets.Box([health_label,health_bar,stage,enemy_bar,enemy_label]).add_class('header_box')


    # Buttons
    btn1 = widgets.Button(description='1')
    btn2 = widgets.Button(description='2')
    btn3 = widgets.Button(description='3')

    def choice_heal():
        health , health_value = player.hp.health_up(player.hp.max_health // 2)
        log(f"> Healed for {health_value} health [💖 {health}/{player.hp.max_health}]")

    def choice_training():
        health,health_value = player.hp.health_down(1+player.atk.current)
        atk,atk_value = player.atk.attack_up(1)
        log(f"> Spent {health_value} health training [💖 {health}/{player.hp.max_health}]")
        log(f"> Attack increased by {atk_value} [⚔️ +{atk}]")

    def choice_chest():
        chance = random.random()
        if 0 <= chance < 0.5:
            health,health_value = player.hp.max_up(5)
            log(f"> 🎁 Chest had a item!")
            log(f"> Max HP Increased by +{health_value} [💖 {player.hp.current}/{player.hp.max_health}]")
        else:
            health,health_value = player.hp.health_down(2)
            log(f"> 🩹 Chest had a trap! Took {health_value} damage [💖 {health}/{player.hp.max_health}]")

    def choice_search():
        chance = random.random()
        if 0 <= chance < 0.2: # 20% chance of a trap
            health,health_value = player.hp.health_down(2)
            log(f"> 🔍 You triggered a trap!")
            log(f"Took {health_value} damage [💖 {health}/{player.hp.max_health}]")
        elif 0.2 <= chance < 0.4: # 20% chance of a monster
            log(f"> 🔍 You ran into a monster!")
            choice_fight()
        elif 0.4 <= chance < 0.7: # 30% chance of healing
            log(f"> 🔍 You found a healing potion!")
            choice_heal()
        else: # 30% chance of Max Health increase
            health,health_value = player.hp.max_up(5)
            log(f"> 🔍 You found an item!")
            log(f"> Max HP Increased by +{health_value} [💖 {player.hp.current}/{player.hp.max_health}]")



    def choice_fight():
        global enable_fight
        enable_fight = True
        enemy_name = random.choice(list(enemy.normal.keys()))
        enemy.new(enemy_name)
        log(f"> You encountered a {enemy_name}!")

    choices = [
            {
                "code" : "fight",
                "label" : "⚔️ Fight",
                "style" : "danger",
                "function" : choice_fight
            },
            {
                "code" : "search",
                "label" : "🔍 Search",
                "style" : "info",
                "function" : choice_search
            },
            {
                "code" : "chest",
                "label" : "🎁 Chest",
                "style" : "primary",
                "function" : choice_chest
            },
            {
                "code" : "train",
                "label" : "💪 Train",
                "style" : "warning",
                "function" : choice_training
            },
            {
                "code" : "heal",
                "label" : "🩹 Heal",
                "style" : "success",
                "function" : choice_heal
            }
        ]

    def btn_click_before(b):
        global enable_fight
        global game_state
        # Get code by searching for the label in the choices list
        if b.description == "Try Again" or b.description == "🔁":
            player.new()
            enemy.new("empty")
            manager.reset()
            enable_fight = False
            game_state = "play"
            next_game_loop()
            return
        
        if b.description == "Victory" or b.description == "🏆":
            player.new()
            enemy.new("empty")
            manager.reset()
            enable_fight = False
            game_state = "play"
            next_game_loop()
            return
        
        if enable_fight:
            if b.description == "💥 Attack":
                player.attack(enemy)
            elif b.description == "🛡️ Defend":
                player.guard()
            enemy.attack(player)
        else:
            function=None
            for choice in choices:
                if choice["label"] == b.description:
                    function = choice["function"]
                    break
            log(f"{b.description}")
            function()

        next_game_loop()

    btn1.on_click(btn_click_before)
    btn2.on_click(btn_click_before)
    btn3.on_click(btn_click_before)

    btn_box = widgets.Box([btn1, btn2, btn3]).add_class('btn_box')

    #Sprite box for display player and enemy/event sprites, background image
    sprite_box = widgets.Box([player.render(),enemy.render()]).add_class('sprite_box')

    #View box for displaying battle scene
    view_box = widgets.Box([background,sprite_box]).add_class('view_box')
    
    #Parent box for containing all elements
    
    parent = widgets.Box([render.BACKGROUND,ui_box,btn_box,view_box]).add_class('parent')

    #Display all elements
    display(parent)
    display_log()

    log("== Action Log ==")

    # Game Loop

    def next_game_loop():
        global enable_fight
        global game_state

        #Check for enemy death
        if enemy.hp.current <= 0 and not enable_fight:
            enemy.new("empty")
        elif enemy.hp.current <= 0 and enable_fight:
            if enemy.current == "boss":
                if manager.level == 4:
                    log("🏆🏆 Victory 🏆🏆")
                    player.set_state("end_battle")
                    game_state = "win"
            else:
                health,health_value = player.hp.max_up(2)
                log(f"> 🔥 You absorb the enemy's power!")
                log(f"> Max HP Increased by +{health_value} [💖 {player.hp.current}/{player.hp.max_health}]")
            enable_fight = False

        

        #on_loop functionality
        player.hp.on_loop() #Check HP and update bar
        enemy.hp.on_loop() # Check HP and update bar

        #Check for player death
        if player.hp.current <= 0:
            game_state = "lose"
            enable_fight = False
        else:    
            if not enable_fight and game_state == "play": 
                manager.on_loop() # Step Up
                if manager.level >= 4:
                    log("Stage Boss has Appeared!")
                    enable_fight = True
                    enemy.new("boss")

        
        
        #Create a new set of choices
        if game_state == "lose":
            btn1.description = "🔁"
            btn2.description = "Try Again"
            btn3.description = "🔁"
            btn1.button_style = "primary"
            btn2.button_style = "primary"
            btn3.button_style = "primary"
        elif game_state == "win":
            btn1.description = "🏆"
            btn2.description = "Victory"
            btn3.description = "🏆"
            btn1.button_style = "success"
            btn2.button_style = "success"
            btn3.button_style = "success"
        else:
            selected_choices = random.sample(choices, 3)
            btn1.description = selected_choices[0]["label"]
            btn2.description = selected_choices[1]["label"]
            btn3.description = selected_choices[2]["label"]
            btn1.button_style = selected_choices[0]["style"]
            btn2.button_style = selected_choices[1]["style"]
            btn3.button_style = selected_choices[2]["style"]

        #Check for fight
        if enable_fight:
            btn1.description = "💥 Attack"
            btn2.description = "🛡️ Defend"
            btn3.layout.visibility = "hidden"
            btn1.button_style = "danger"
            btn2.button_style = "warning"
        else:
            btn3.layout.visibility = "visible"

    global game_state
    game_state = "play"     
    global enable_fight
    enable_fight = False
    next_game_loop()