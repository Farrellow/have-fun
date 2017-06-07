# -*- coding: utf-8 -*-

import sys

#def _print(x, y, s):
#    sys.stdout.write('\033[' + str(y + 1) + ';' + str(x * 2 + 1) + 'H')
#    sys.stdout.write(s)
#
#def show_display():
#    for i in range(x_axis_end):
#        for j in range(y_axis_end):
#            if cell_space[i][j] == D_2_L:
#                cell_space[i][j] = L
#                show(i, j)
#            if cell_space[i][j] == L_2_D:
#                cell_space[i][j] = D
#                hide(i, j)
#
#def get_count(i, j):
#    count = 0
#    if i > 0:
#        if cell_space[i - 1][j] == L or cell_space[i - 1][j] == L_2_D:
#            count += 1
#    if i < x_axis_end - 1:
#        if cell_space[i + 1][j] == L or cell_space[i + 1][j] == L_2_D:
#            count += 1
#    if j > 0:
#        if cell_space[i][j - 1] == L or cell_space[i][j - 1] == L_2_D:
#            count += 1
#    if j < y_axis_end - 1:
#        if cell_space[i][j + 1] == L or cell_space[i][j + 1] == L_2_D:
#            count += 1
#
#    if i > 0 and j > 0:
#        if cell_space[i - 1][j - 1] == L or cell_space[i - 1][j - 1] == L_2_D:
#            count += 1
#    if i > 0 and j < y_axis_end - 1:
#        if cell_space[i - 1][j + 1] == L or cell_space[i - 1][j + 1] == L_2_D:
#            count += 1
#    if i < x_axis_end - 1 and j > 0:
#        if cell_space[i + 1][j - 1] == L or cell_space[i + 1][j - 1] == L_2_D:
#            count += 1
#    if i < x_axis_end - 1 and j < y_axis_end - 1:
#        if cell_space[i + 1][j + 1] == L or cell_space[i + 1][j + 1] == L_2_D:
#            count += 1
#
#    return count
#
#def next_step():
#    for i in range(x_axis_end):
#        for j in range(y_axis_end):
#            count = get_count(i, j)
#            status = cell_space[i][j]
#            if status == L:
#                if count < 2:
#                    cell_space[i][j] = L_2_D
#                elif count > 3:
#                    cell_space[i][j] = L_2_D
#                else:
#                    pass
#            if status == D:
#                if count == 3:
#                    cell_space[i][j] = D_2_L


DIE   = 0
LIVE  = 1
D_2_L = 2
L_2_D = 3


class Space(object):
    # space[x][y] -> int, x and y can be any int
    #
    # scale_d: tuple(i, j) -> list[list[]]                                   
    #
    # for any i, j:
    # there is a block = scale_d[(i, j)], that:
    # x == i * scale + x0 and y == j * scale + y0
    # <==> space[x][y] is block[x0][y0]
    scale = 5
    live_set = set()  # (x, y)

    class Block(list):
        def __init__(self):
            list.__init__(self)
            for _ in range(Space.scale):
                self.append([DIE for _ in range(Space.scale)])

    scale_d = {}  # (i, j) -> Block

    class L(list):
        def __init__(self, x):
            self.x = x
            self.i = x // Space.scale
    
        def __getitem__(self, y):
            j = y // Space.scale
            if Space.scale_d.get((self.i, j)) == None:
                return 0
            else:
                block = Space.scale_d[(self.i, j)]
                return block[self.x % Space.scale][y % Space.scale]

        def __setitem__(self, y, val):
            j = y // Space.scale
            if Space.scale_d.get((self.i, j)) == None:
                block = Space.Block()
                block[self.x % Space.scale][y % Space.scale] = val
                Space.scale_d[(self.i, j)] = block
            else:
                block = Space.scale_d[(self.i, j)]
                block[self.x % Space.scale][y % Space.scale] = val

    def __init__(self):
        self.x_d = {} # x -> L

    def __getitem__(self, x):
        if self.x_d.get(x) == None:
            self.x_d[x] = self.L(x)
            return self.x_d[x]
        else:
            return self.x_d[x]

    def get_neighbors(self, x, y):
        return [
                (i, j) for i in range(x - 1, x + 2) 
                    for j in range(y - 1, y + 2) 
                        if x != i or y != j
                ]

    def next_step(self):
        handler_set = set()
        for x, y in self.live_set:
            pass
