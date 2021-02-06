################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 3
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

def increase_global_enemies():
  global enemies
  enemies += 1
  print(enemies)
increase_global_enemies()