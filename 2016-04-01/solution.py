class ImpossiblePuzzle(list):
    @staticmethod
    def from_set(s, allow_equal=True):
        s = set(s)
        if allow_equal:
            return ImpossiblePuzzle(
                (i, j) for i in s for j in s if i <= j)
        else:
            return ImpossiblePuzzle(
                (i, j) for i in s for j in s if i < j)

    @staticmethod
    def from_range(*args, **kwargs):
        allow_equal = kwargs.get('allow_equal', True)
        return ImpossiblePuzzle.from_set(range(*args), allow_equal)

    def does_pete_know(self, answer):
        p = dict()
        for i, j in self:
            if i*j in p:
                p[i*j].append((i, j))
            else:
                p[i*j] = [(i, j)]
        ret = []
        for pairs in p.values():
            if (len(pairs) > 1) != (answer == 'yes'):
                ret += pairs
        return ImpossiblePuzzle(ret)

    def does_susan_know(self, answer):
        s = dict()
        for i, j in self:
            if i+j in s:
                s[i+j].append((i, j))
            else:
                s[i+j] = [(i, j)]
        ret = []
        for pairs in s.values():
            if (len(pairs) > 1) != (answer == 'yes'):
                ret += pairs
        return ImpossiblePuzzle(ret)


if __name__ == '__main__':
    puzzle = ImpossiblePuzzle.from_range(1, 10)
    # Q1
    print(puzzle
          .does_pete_know('no')
          .does_susan_know('no')
          .does_pete_know('no')
          .does_susan_know('no')
          .does_pete_know('no')
          .does_susan_know('no')
          .does_pete_know('no')
          .does_susan_know('no')
          .does_pete_know('yes')
          )
    # Q2
    print(puzzle
          .does_pete_know('no')
          .does_susan_know('no')
          .does_pete_know('no')
          .does_susan_know('no')
          .does_pete_know('no')
          .does_susan_know('no')
          .does_pete_know('no')
          .does_susan_know('no')
          .does_pete_know('no')
          .does_susan_know('yes')
          )
