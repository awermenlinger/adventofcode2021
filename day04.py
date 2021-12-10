import numpy as np

with open('files/day04.txt', 'r') as f:
    data = f.read().split('\n\n')

nbs_drawn = [int(i) for i in data[0].split(',')]
boards = [[[int(i) for i in line.split()] for line in board.split('\n')] for board in data[1:]]

#create empty boards
marks = [[[0 for i in range(len(boards[0][0]))] for j in range(len(boards[0]))] for k in range(len(boards))]

boards = [np.array(board) for board in boards]
marks = [np.array(mark) for mark in marks]

def mark_boards(nb_drawn, boards, marks):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k] == nb_drawn:
                    marks[i][j][k] = 1

def check_marks(mark):
    bingo = False
    #check rows
    for i in range(mark.shape[0]):   
        if np.min(mark[i][:]) == 1:
            bingo = True

    #check columns
    for i in range(mark.shape[1]):
        if np.min(mark[:,i]) == 1:
            bingo = True

    return bingo

overall_bingo = False
i=0
while overall_bingo == False:
    mark_boards(nbs_drawn[i], boards, marks)
    for j in range(len(boards)):
        bingo = check_marks(marks[j])
        if bingo == True:
            overall_bingo = True
            winning_board = boards[j]
            winning_marks = marks[j]
            winning_number = nbs_drawn[i]
            winning_values = np.sum(np.ma.masked_where(winning_marks == 1, winning_board))
            print('Bingo!')
    i+=1

print("part 1: {}".format(winning_number*winning_values))


#create empty marks
marks_to_prune = [[[0 for i in range(len(boards[0][0]))] for j in range(len(boards[0]))] for k in range(len(boards))]
marks_to_prune = [np.array(mark) for mark in marks_to_prune]
boards_to_prune = boards.copy()

i=0
overall_bingo = False
while overall_bingo == False:
    mark_boards(nbs_drawn[i], boards_to_prune, marks_to_prune)
    j = 0
    while j < len(boards_to_prune):
        bingo = check_marks(marks_to_prune[j])
        if bingo == True:
            if len(boards_to_prune) > 1:
                boards_to_prune.pop(j)
                marks_to_prune.pop(j)
            else:
                overall_bingo = True
                winning_board_pruned = boards_to_prune[j]
                winning_marks_pruned = marks_to_prune[j]
                winning_number_pruned = nbs_drawn[i]
                winning_values_pruned = np.sum(np.ma.masked_where(winning_marks_pruned == 1, winning_board_pruned))
                j+=1
        else:
            j+=1
    i+=1
print("part 2: {}".format(winning_number_pruned*winning_values_pruned))