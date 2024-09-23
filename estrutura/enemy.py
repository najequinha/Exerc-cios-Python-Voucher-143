class Enemy:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False  
    def take_damage(self, damage):
        self.hp -= damage
    def attack_enemy(self, enemy, atk):
        if enemy>0:
            atk = (self.defense + self.attack)/2
            enemy -= atk
            if enemy<0:
                print(f"Game over!")