from stats import wizard, human
import time
import random

enemy_dead = False
player_dead = False

choises = ['attack','heal']

print("Hello! Here are your stats\nHealth = ",human.healtpoints,"\nDamage = ",human.damage,"\nHeal ammount = ",human.hp_recovered)

time.sleep(3)
print("An enemy has atacked you its a wizard\nHe will start the fight")

while enemy_dead or player_dead == False:

    if human.healtpoints <= 0:
        player_dead = True
        print("Game over. You died!")
        break
    if wizard.healtpoints <= 0:
        enemy_dead = True
        print("Game over. Wizard died!")
        break

    wizard_move = random.randint(1, 2)
    if wizard_move == 1:
        wizard.atack(human)
    if wizard_move == 2:
        wizard.heal(wizard)

    user_choice = input("Would you like to (attack) or (heal?): ")
    if user_choice == choises[0]:
        human.atack(wizard)
    if user_choice == choises[1]:
        human.heal(human)


