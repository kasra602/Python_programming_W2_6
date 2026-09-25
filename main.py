print("Program starting.\n")

hexnum = input("Insert a hex color:\n")
hexnum = hexnum.lstrip("#")

red = hexnum[0:2]
green = hexnum[2:4]
blue = hexnum[4:6]

print(f"Colors\n- Red {red}\n- Green {green}\n- Blue {blue}\n")
print("Program ending.\n")
