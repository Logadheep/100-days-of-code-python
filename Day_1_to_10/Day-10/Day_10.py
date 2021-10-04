with open("input.txt") as r:
    lines = r.readlines()
    
r.close()

with open("output.txt", "w") as w:
    w.writelines(lines)
w.close()
