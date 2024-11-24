from moves import moves, move

tackle = move("Tackle", 40, 100, "Normal")
scratch = move("Scratch", 40, 100, "Normal")
ember = move("Ember", 45, 100, "Fire")
vine_whip = move("Vine Whip", 45, 100, "Water")
water_gun = move("Water Gun", 45, 100, "Grass")
tail_whip = move("Tail Whip", 40, 100, "Normal")

move_pool = moves()
move_pool.append(tackle)
move_pool.append(scratch)
move_pool.append(ember)
move_pool.append(vine_whip)
move_pool.append(water_gun)
move_pool.append(tail_whip)