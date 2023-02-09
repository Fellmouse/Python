class Player:
  def __init__(self, name, type):
    self.name =  name
    self.type = type
    self.hp = 100
    self.mp = 120
    self.armor = 50
    self.ap = 20
    
  def attack(self, player):
    hp = player.hp
    damage = self.ap * (100 - player.armor) / 100
    player.armor -= damage
    player.hp -= damage
    print("player {0} took {1} damage".format(player.name, damage))
    if (player.hp <= 0):
      print("player is ded")

player = Player("Fell", "warrior")
player2 = Player("Mouse", "paladin")

'''
print(player.name)
print(player2.name)
print(player2.hp)
player.attack(player2)
print(player2.hp)
print(player2.armor)

print("Name: {0}".format(player.name))
print("type: {0}".format(player.type))
print("hp: {0}".format(player.hp))
print("mp: {0}".format(player.mp))
print("armor: {0}".format(player.armor))
print("ap: {0}".format(player.ap))
print(player2.type)
'''

player.attack(player2)
player.attack(player2)
player.attack(player2)
player.attack(player2)
player.attack(player2)
player.attack(player2)
player.attack(player2)
