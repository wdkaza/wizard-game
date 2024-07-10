import random
import time
class wizard:
    healtpoints = random.randint(50,70)
    damage = random.randint(20,25)
    hp_recovered = random.randint(10,30)

    def atack(self):
        time.sleep(1.5)
        print("=============================================\nWizard is atacking you!!!\n--------------------------------------------------------------")
        time.sleep(3)
        print("Wizard casts a fireball dealing: ", self.damage," Damage to your hp: ", human.healtpoints)
        time.sleep(3)
        human.healtpoints = human.healtpoints - self.damage
        print("Your healtpoints remaining: ",human.healtpoints)
        time.sleep(1.5)
        print("--------------------------------------------------------------\nWizard turn has ended\n=============================================")

    def heal(self):
        time.sleep(1.5)
        print("=============================================\nWizard is going to heal!!!\n--------------------------------------------------------------")
        time.sleep(3)
        self.healtpoints = self.healtpoints + self.hp_recovered
        print("Wizard used a health potion healing him for: ", self.hp_recovered)
        time.sleep(3)
        print("Wizard hp remaining: ",self.healtpoints)
        time.sleep(1.5)
        print("--------------------------------------------------------------\nWizard turn has ended\n=============================================")

class human:
    healtpoints = random.randint(90,100)
    damage = random.randint(30,50)
    hp_recovered = random.randint(15,35)

    def atack(self):
        print("=============================================\nYou are atacking!!!\n--------------------------------------------------------------")
        time.sleep(3)
        print("You swing a sword dealing: ", self.damage," Damage to wizard hp: ", wizard.healtpoints)
        time.sleep(3)
        wizard.healtpoints = wizard.healtpoints - self.damage
        print("Wizard healthpoints remaining: ",wizard.healtpoints)
        time.sleep(1.5)
        print("--------------------------------------------------------------\nYour turn has ended\n=============================================")

    def heal(self):
        print("=============================================\nYou are going to heal!!!\n--------------------------------------------------------------")
        time.sleep(3)
        self.healtpoints = self.healtpoints + self.hp_recovered
        print("You used a health potion healing yourself for: ", self.hp_recovered)
        time.sleep(3)
        print("Your hp remaining: ",self.healtpoints)
        time.sleep(1.5)
        print("--------------------------------------------------------------\nYour turn has ended\n=============================================")

