from solution import PossiblePairs


def tester(*args):
    def sums(possible):
        ret = dict()
        for i, j in possible:
            if i+j in ret:
                ret[i+j].append((i, j))
            else:
                ret[i+j] = [(i, j)]
        return ret

    def prods(possible):
        ret = dict()
        for i, j in possible:
            if i*j in ret:
                ret[i*j].append((i, j))
            else:
                ret[i*j] = [(i, j)]
        return ret

    for a, b in PossiblePairs.from_range(*args):
        possible = PossiblePairs.from_range(*args)
        p = a*b
        s = a+b

        k = 0
        while True:
            k += 1
            l = len(possible)
            if len(prods(possible)[p]) == 1:
                yield (a, b), 'P{}'.format(k)
                break
            possible = possible.does_pete_know('no')
            if len(sums(possible)[s]) == 1:
                yield (a, b), 'S{}'.format(k)
                break
            possible = possible.does_susan_know('no')
            if l == len(possible):
                yield (a, b), 'Never'
                break


if __name__ == '__main__':
    print(list(tester(1, 10)))
