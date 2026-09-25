import sys

sys.stdout.write("Program starting.\n\n")

sys.stdout.write("Insert a hex color: \n")
hexnum = input().lstrip("#")

red = hexnum[0:2]
green = hexnum[2:4]
blue = hexnum[4:6]

sys.stdout.write(
    f"Colors\n"
    f"- Red {red}\n"
    f"- Green {green}\n"
    f"- Blue {blue}\n\n"
)

sys.stdout.write("Program ending.\n")
