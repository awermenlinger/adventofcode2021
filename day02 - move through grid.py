horizontal = 0
depth = 0

moves = open('files\day02.txt', 'r').read().rstrip().split('\n')

for move in moves:
   if move[0] == "f": horizontal += int(move[-1])
   elif move[0] == "u": depth -= int(move[-1])
   elif move[0] == "d": depth += int(move[-1])

print("1 - Forward: {}  Depth: {}   Result: {}".format(horizontal, depth, horizontal*depth))

horizontal = 0
depth = 0
aim = 0

moves = open('files\day2.txt', 'r').read().rstrip().split('\n')

for move in moves:
   if move[0] == "f": 
       horizontal += int(move[-1])
       depth += aim * int(move[-1])
   elif move[0] == "u": aim -= int(move[-1])
   elif move[0] == "d": aim += int(move[-1])

print("1 - Forward: {}  Depth: {}   Result: {}".format(horizontal, depth, horizontal*depth))