#I did everything I could but it would not work so I changed the entire code...

print("Program starting.")
print()

hexnum = input("Insert a hex color: ")
hexnum = hexnum.lstrip("#")

red = hexnum[0:2]
green = hexnum[2:4]
blue = hexnum[4:6]

print("Colors")
print(f"- Red {red}")
print(f"- Green {green}")
print(f"- Blue {blue}")
print()

print("Program ending.")
