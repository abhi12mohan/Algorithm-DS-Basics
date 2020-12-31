DIRECTIONS = {"N": (-1, 0), "E": ( 0, 1), "S": ( 1, 0), "W": ( 0,-1)}

def make_move(B, m, orientation):
    '''
    Apply move m to board B (or inverse if orientation is 'backward')
    Return resulting board, or None if m is not a valid move
    Input:      B | tuple of tuples representing a board configuration
                m | triple representing a board move
      orientation | either 'forward' or 'backward'
    '''
    if m is None:
        return None

    r, c, d = m
    dr, dc = DIRECTIONS[d]
    R, C = len(B), len(B[0])

    if (0 <= r + 2*dr < R) and (0 <= c + 2*dc < C): # move is on board
        before, after = (1, 1, 0), (0, 0, 1)
        if orientation == "backward":
            before, after = after, before

        for i in range(3):                          # check that move is valid
            if B[r + i*dr][c + i*dc] != before[i]:
                return None

        B_ = [[p for p in row] for row in B]
        for i in range(3):                          # make move
            B_[r + i*dr][c + i*dc] = after[i]
            
        return tuple(tuple(p for p in row) for row in B_)

def peg_solve(B):
    '''
    Input:  B | tuple of tuples representing a board configuration
    Output: M | tuple of moves to solve B, or None if no such moves exist
    '''
    rows = len(B)
    columns = len(B[0])
    pegs = sum(sum(i) for i in B)
    moves = []

    def solver(B, pegs):
        for row in range(rows):
            for column in range(columns):
                if B[row][column] == 1:
                    for direction in DIRECTIONS:
                        new_board = make_move(B, (row, column, direction), 'forward')

                        if new_board:
                            moves.append((row, column, direction))
                            pegs -= 1

                            if pegs == 1:
                                return moves
                            elif solver(new_board, pegs):
                                return moves
                            else:
                                moves.pop()
                                pegs += 1

    final_moves = solver(B, pegs)
    return None if final_moves == [] else final_moves
