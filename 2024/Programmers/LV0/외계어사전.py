import itertools

def solution(spell, dic):
    answer = []
    permutations = list(itertools.permutations(spell, len(spell)))
    transformed_permutations = list(map(lambda x: ''.join(x), permutations))

    for i in dic:
        if i in transformed_permutations:
            return 1

    return 2


def solution(spell, dic):
    for i in dic:
        if not set(spell) - set(i):
            return 1

    return 2