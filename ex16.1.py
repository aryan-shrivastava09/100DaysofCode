# to install a package
# run
# pip install packageNAme
from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Names', ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
table.align = 'l'
print(table)