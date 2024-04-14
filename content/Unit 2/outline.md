# Project Outline

You will be designing a choice based adventure game. The goal is to reach the last stage and beat the final boss by making choices that will affect your characters stats.

## Main Gameplay Loop

The game will consist of 5 stages, each stage will present the player with 3 choices. The player will pick one choice and see the outcome before moving to the next stage.

### Choices

The game will have a total of 5 choices, from which 3 random choices will be selected per stage.
Fight:

-   Fight against a enemy, if you win raise max hp by 2.
    Train:
-   Lose current attack + 1 hp but gain 1 attack permanently
    Heal:
-   Heal back 1/3 hp
    Chest:
-   50% chance to lose 2 hp by damage, 50% chance to raise max hp by 5.
    Search:
-   Series of events with different probabilities
-   20% chance for a trap, lose 2 hp
-   20% chance to encounter a enemy, same as Fight choice
-   30% chance to find a healing potion, same as Heal choice
-   30% chance to find a item, max health +5

### User Interface

The user interface will consist of the following elements:

-   Player HP Bar
-   Enemy HP Bar
-   Stage Meter (Indicating current stage via a visual)
-   Stage Label (Indicating current stage via text)
-   3 Buttons for the choices
-   Viewbox containing the player and enemy images

---

Your project is broken down into 3 core phases:

1. Phase 1: Gameplay Logic
    - Implement the logic for each choice with modular design
    - Implement the stage progression logic
    - Implement enemy spawn logic
    - Implement victory and game over logic
2. Phase 2: User Interface
    - Implement the user interface elements
    - Implement the stage progression visual
    - Implement the choice buttons
    - Implement the player and enemy images
    - Link the user interface to gameplay logic
3. Phase 3: Document and Test
    - Document the code
    - Test the game for bugs
    - Test the game for balance
    - Test the game for user experience

By the end of the project, you're expected to have functional game that can be played from start to finish and user documentation that explains how to play the game along with the game mechanics (HP, Damage, Attack, Choices).

You will also be expected to submit the following:

-   GANTT Chart for project planning along with project process
-   A reflection of testing and debugging.
