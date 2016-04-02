from solution import ImpossiblePuzzle


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
                yield (a, b), 'P{}'.format(k)
                break
            puzzle = puzzle.does_pete_know('no')
            if len(sums(puzzle)[s]) == 1:
                yield (a, b), 'S{}'.format(k)
                break
            puzzle = puzzle.does_susan_know('no')
            if l == len(puzzle):
                yield (a, b), 'Never'
                break


if __name__ == '__main__':
    print(list(tester(1, 40)))
