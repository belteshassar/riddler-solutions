from solution import ImpossiblePuzzle

import numpy as np
import matplotlib.pyplot as plt


def tester(*args):
    def sums(puzzle):
        ret = dict()
        for i, j in puzzle:
            if i+j in ret:
                ret[i+j].append((i, j))
            else:
                ret[i+j] = [(i, j)]
        return ret

    def prods(puzzle):
        ret = dict()
        for i, j in puzzle:
            if i*j in ret:
                ret[i*j].append((i, j))
            else:
                ret[i*j] = [(i, j)]
        return ret

    for a, b in ImpossiblePuzzle.from_range(*args):
        puzzle = ImpossiblePuzzle.from_range(*args)
        p = a*b
        s = a+b

        k = 0
        while True:
            k += 1
            l = len(puzzle)
            if len(prods(puzzle)[p]) == 1:
                break
            puzzle = puzzle.does_pete_know('no')
            k += 1
            if len(sums(puzzle)[s]) == 1:
                break
            puzzle = puzzle.does_susan_know('no')
            if l == len(puzzle):
                k = 0
                break
        yield a, b, k


if __name__ == '__main__':
    n = 99
    res = np.zeros((n, n))
    for i, j, k in tester(1, n+1):
        res[i-1, j-1] = k
        res[j-1, i-1] = k
    fig, ax = plt.subplots()
    plt.set_cmap('inferno')
    im = ax.imshow(np.ma.array(res, mask=(res == 0)),
                   aspect='equal',
                   interpolation='nearest',
                   extent=(0.5, n+0.5, 0.5, n+0.5),
                   origin='lower')
    plt.colorbar(im, label='Rounds to crack')
    ax.invert_yaxis()
    ax.autoscale(tight=True)
    plt.show()
