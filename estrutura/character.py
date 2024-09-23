class Character:
    def __init__(self, name, hp, max_hp, attack, defense, inventory):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.inventory = inventory
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            print("Game over!")
            return False
    def take_damage(self, damage):
        if self.hp>0:
            damage = damage/self.defense
            if damage>self.hp:
                print("Game over!")
            else:
                self.hp-=damage
                print(f"Damage received! -{damage}hp!")
    def heal(self, amount):
        amount = self.max_hp * (amount/100)
        self.hp += amount
        print(f"HP points healed: {amount}")
    def attack_enemy(self, enemy, atk):
        if enemy>0:
            atk = (self.defense + self.attack)/2
            enemy -= atk
            print(f"Damage applied! Total damage: {atk}")
            if enemy<0:
                print(f"You win!")


