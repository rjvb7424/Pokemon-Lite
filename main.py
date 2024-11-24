from charmander import charmander
from squirtle import squirtle
from battle import battle

charmander1 = charmander()
squirtle1 = squirtle()
battle1 = battle(charmander1, squirtle1)

battle1.battle_logic()