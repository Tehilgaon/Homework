import copy
import alphaBetaPruning


VICTORY = 10 ** 20  # The value of a winning board (for max)
LOSS = -VICTORY  # The value of a losing board (for max)
TIE = 0  # The value of a tie
SIZE = 4  # the length of winning seq.
COMPUTER = SIZE + 1  # Marks the computer's cells on the board
HUMAN = 1  # Marks the human's cells on the board

rows = 6
columns = 7

'''
Tehila Gaon ID: 315136952
'''


class game:
    board = []
    size = rows * columns
    playTurn = HUMAN
    value = 0.00001

    # Used by alpha-beta pruning to allow pruning

    '''
    The state of the game is represented by a list of 4 items:
        0. The game board - a matrix (list of lists) of ints. Empty cells = 0,
        the comp's cells = COMPUTER and the human's = HUMAN
        1. The heuristic value of the state.
        2. Whose turn is it: HUMAN or COMPUTER
        3. Number of empty cells
    '''


def create(s):
    # Returns an empty board. The human plays first.
    # create the board
    s.board = []
    for i in range(rows):
        s.board = s.board + [columns * [0]]

    s.playTurn = HUMAN
    s.size = rows * columns
    s.value = 0.00001


def cpy(s1):
    # construct a parent DataFrame instance
    s2 = game()
    s2.playTurn = s1.playTurn
    s2.size = s1.size
    s2.board = copy.deepcopy(s1.board)
    return s2


def value(s):
    # Returns the heuristic value of s
    return s.value


def checkSeq(s):
    # Checks all the board's seq
    # If it identifies for in a row, it changes to VICTORY/LOSS. Otherwise it updates val
    s.value = 1
    rm = [SIZE - 1, 0, SIZE - 1, -SIZE + 1]
    cm = [0, SIZE - 1, SIZE - 1, SIZE - 1]
    for row in range(0, rows):
        for col in range(0, columns):
            for i in range(len(rm)):
                t = estimate(s, row, col, row + rm[i], col + cm[i])
                if t in [LOSS, VICTORY]:
                    s.value = t
                    break
                else:
                    s.value += t


def estimate(s, r1, c1, r2, c2):
    # Giving a score to each kind of sequence
    # r1, c1 are in the board. if r2,c2 not on board returns 0.
    # If empty returns 0.00001.
    if r2 < 0 or c2 < 0 or r2 >= rows or c2 >= columns:
        return 0  # r2, c2 are illegal
    dr = (r2 - r1) // (SIZE - 1)  # the horizontal step from cell to cell
    dc = (c2 - c1) // (SIZE - 1)  # the vertical step from cell to cell
    sum = 0
    seq = [0] * SIZE
    for i in range(SIZE):  # summing the values in the seq.
        sum += s.board[r1 + i * dr][c1 + i * dc]
        seq[i] = s.board[r1 + i * dr][c1 + i * dc]

    if seq == [COMPUTER] * SIZE:
        return VICTORY
    if seq == [HUMAN] * SIZE:
        return LOSS
    if seq == (SIZE - 1) * [HUMAN] + [COMPUTER] or sum == [COMPUTER] + (SIZE - 1) * [HUMAN]:  # blocking the enemy's win
        return 1000
    score = 0
    if sum > 0 and sum % COMPUTER == 0:  # 1/2/3-in-a-row ,and there is a room to complete a quartet
        score = sum * 10
    if sum == HUMAN * (SIZE-1):  # enemy's 3-in-a-row and there is a room to complete a quartet
        score = -1000
    if sum == HUMAN * (SIZE-2):  # enemy's 2-in-a-row and there is a room to complete a quartet
        score = -100

    if c1 == c2:  # a vertical threat is more trivial and easily blocked, therefore its weight should be lower
        score /= 2

    if score != 0:
        return score
    return 0.00001  # not 0 because TIE is 0


def emptySquare(threat):
    # Finds and returns the indexes of the threat's empty square in the board
    # threat = seq-Of-3
    emptySquare = threat[0].index(0)
    i = threat[1]  # r1
    j = threat[2]  # c1
    if threat[1] != threat[3]:
        i += emptySquare
    if threat[2] != threat[4]:
        j += emptySquare
    return [i, j]


def printState(s):
    # Prints the board. The empty cells are printed as numbers = the cells name(for input)
    # If the game ended prints who won.
    for r in range(rows):
        print("\n|", end="")
        # print("\n",len(s[0][0])*" --","\n|",sep="", end="")
        for c in range(columns):
            if s.board[r][c] == COMPUTER:
                print("X|", end="")
            elif s.board[r][c] == HUMAN:
                print("O|", end="")
            else:
                print(" |", end="")

    print()
    for i in range(columns):
        print(" ", i, sep="", end="")
    print()

    checkSeq(s)
    val = value(s)
    if s.size == 0:  # checking if it is a TIE
        val = TIE
    s.size -= 1  # one less empty cell

    if val == VICTORY:
        print("I won!")
    elif val == LOSS:
        print("You beat me!")
    elif val == TIE:
        print("It's a TIE")


def isFinished(s):
    # S returns True if the game ended
    return value(s) in [LOSS, VICTORY, TIE] or s.size == -1


def isHumTurn(s):
    # Returns True iff it is the human's turn to play
    return s.playTurn == HUMAN


def decideWhoIsFirst(s):
    # The user decides who plays first
    if int(input("Who plays first? 1-me / anything else-you : ")) == 1:
        s.playTurn = COMPUTER
    else:
        s.playTurn = HUMAN
    return s.playTurn


def makeMove(s, c):
    # Puts mark (for human or comp.) in col. c
    # and switches turns.
    # Assumes the move is legal.
    r = 0
    while r < rows and s.board[r][c] == 0:
        r += 1

    s.board[r - 1][c] = s.playTurn  # marks the board
    if s.playTurn == COMPUTER:
        s.playTurn = HUMAN
    else:
        checkSeq(s)
        s.playTurn = COMPUTER


def inputMove(s):
    # Reads, enforces legality and executes the user's move.
    # self.printState()
    flag = True
    while flag:
        c = int(input("Enter your next move: "))
        if c < 0 or c >= columns or s.board[0][c] != 0:
            print("Illegal move.")

        else:
            flag = False
            makeMove(s, c)


def getNext(s):
    # returns a list of the next states of s
    ns = []
    for c in list(range(columns)):
        if s.board[0][c] == 0:
            tmp = cpy(s)
            makeMove(tmp, c)
            ns += [tmp]
    return ns


def inputComputer(s):
    return alphaBetaPruning.go(s)
