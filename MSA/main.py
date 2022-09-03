import numpy
from itertools import chain, combinations
def input_data():
    seq = []
    aminos = []
    n = int(input())
    for i in range(n):
        seq.append(input())
        x = [char for char in seq[i]]
        for t in x:
            if t not in aminos:
                aminos.append(t)

    ans = input()
    height = numpy.zeros([len(seq), len(x)], dtype=int)
    str = ['' for i in range(len(seq[0]))]
    for i in range(len(height)):
        x = [char for char in seq[i]]
        for j in range(len(x)):
            str[j] += x[j]

    return seq, aminos, ans, str

def MSA(seq, aminos, str):
    matrix = numpy.zeros([len(aminos), len(seq[0])], dtype=float)
    for i in range(len(matrix)):        #aminos
        for j in range(len(matrix[0])):     #seq
            matrix[i][j] = str[j].count(aminos[i]) + 2
    div = 0
    for i in range(len(matrix)):
        div += matrix[i][0]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] /= 18

    for i in range(len(matrix)):
        sum = numpy.sum(matrix[i])/5
        for j in range(len(matrix[0])):
            matrix[i][j] = numpy.log2(matrix[i][j]/sum)
    return matrix


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def score(matrix, aminos, ans):
    strs = []
    seq = [char for char in ans]
    for i in range(len(matrix[0])):
        for j in range(len(seq)-i):
            str = ''
            for k in range(j, j+i+1):
                str += seq[k]
            if str not in strs:
                strs.append(str)
    max_str = ''
    max_score = -9999.9
    list1 = []
    for j in range(len(matrix[0])):
        list1.append(j)
    for i in range(len(strs)):
        x = [char for char in strs[i]]

        for result in powerset(list1):
            str = []
            if len(result) == len(matrix[0])-len(x):
                list_result = list(result)
                counter = 0
                for i in range(len(matrix[0])):
                    if i in list_result:
                        str.append('-')
                    else:
                        str.append(x[counter])
                        counter += 1
                score = 0
                for j in range(len(str)):
                    score += matrix[aminos.index(str[j])][j]
                if max_score < score:
                    max_score = score
                    max_str = str
    answer = ''
    for i in range(len(max_str)):
        answer += max_str[i]
    print(answer)

if __name__ == '__main__':
    seq, aminos, ans, str = input_data()
    matrix = MSA(seq, aminos, str)
    str = [char for char in ans]
    substr = []
    score(matrix, aminos, ans)
