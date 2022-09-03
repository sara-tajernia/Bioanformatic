import copy


PAM250 = {
'A': {'A':  2, 'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N':  0, 'P':  1, 'Q':  0, 'R': -2, 'S':  1, 'T':  1, 'V':  0, 'W': -6, 'Y': -3},
'C': {'A': -2, 'C': 12, 'D': -5, 'E':-5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S':  0, 'T': -2, 'V': -2, 'W': -8, 'Y':  0},
'D': {'A':  0, 'C': -5, 'D':  4, 'E': 3, 'F': -6, 'G':  1, 'H':  1, 'I': -2, 'K':  0, 'L': -4, 'M': -3, 'N':  2, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'E': {'A':  0, 'C': -5, 'D':  3, 'E': 4, 'F': -5, 'G':  0, 'H':  1, 'I': -2, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P': -1, 'Q':  2, 'R': -1, 'S':  0, 'T':  0, 'V': -2, 'W': -7, 'Y': -4},
'F': {'A': -3, 'C': -4, 'D': -6, 'E':-5, 'F':  9, 'G': -5, 'H': -2, 'I':  1, 'K': -5, 'L':  2, 'M':  0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W':  0, 'Y':  7},
'G': {'A':  1, 'C': -3, 'D':  1, 'E': 0, 'F': -5, 'G':  5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N':  0, 'P':  0, 'Q': -1, 'R': -3, 'S':  1, 'T':  0, 'V': -1, 'W': -7, 'Y': -5},
'H': {'A': -1, 'C': -3, 'D':  1, 'E': 1, 'F': -2, 'G': -2, 'H':  6, 'I': -2, 'K':  0, 'L': -2, 'M': -2, 'N':  2, 'P':  0, 'Q':  3, 'R':  2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y':  0},
'I': {'A': -1, 'C': -2, 'D': -2, 'E':-2, 'F':  1, 'G': -3, 'H': -2, 'I':  5, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -5, 'Y': -1},
'K': {'A': -1, 'C': -5, 'D':  0, 'E': 0, 'F': -5, 'G': -2, 'H':  0, 'I': -2, 'K':  5, 'L': -3, 'M':  0, 'N':  1, 'P': -1, 'Q':  1, 'R':  3, 'S':  0, 'T':  0, 'V': -2, 'W': -3, 'Y': -4},
'L': {'A': -2, 'C': -6, 'D': -4, 'E':-3, 'F':  2, 'G': -4, 'H': -2, 'I':  2, 'K': -3, 'L':  6, 'M':  4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V':  2, 'W': -2, 'Y': -1},
'M': {'A': -1, 'C': -5, 'D': -3, 'E':-2, 'F':  0, 'G': -3, 'H': -2, 'I':  2, 'K':  0, 'L':  4, 'M':  6, 'N': -2, 'P': -2, 'Q': -1, 'R':  0, 'S': -2, 'T': -1, 'V':  2, 'W': -4, 'Y': -2},
'N': {'A':  0, 'C': -4, 'D':  2, 'E': 1, 'F': -3, 'G':  0, 'H':  2, 'I': -2, 'K':  1, 'L': -3, 'M': -2, 'N':  2, 'P':  0, 'Q':  1, 'R':  0, 'S':  1, 'T':  0, 'V': -2, 'W': -4, 'Y': -2},
'P': {'A':  1, 'C': -3, 'D': -1, 'E':-1, 'F': -5, 'G':  0, 'H':  0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N':  0, 'P':  6, 'Q':  0, 'R':  0, 'S':  1, 'T':  0, 'V': -1, 'W': -6, 'Y': -5},
'Q': {'A':  0, 'C': -5, 'D':  2, 'E': 2, 'F': -5, 'G': -1, 'H':  3, 'I': -2, 'K':  1, 'L': -2, 'M': -1, 'N':  1, 'P':  0, 'Q':  4, 'R':  1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4},
'R': {'A': -2, 'C': -4, 'D': -1, 'E':-1, 'F': -4, 'G': -3, 'H':  2, 'I': -2, 'K':  3, 'L': -3, 'M':  0, 'N':  0, 'P':  0, 'Q':  1, 'R':  6, 'S':  0, 'T': -1, 'V': -2, 'W':  2, 'Y': -4},
'S': {'A':  1, 'C':  0, 'D':  0, 'E': 0, 'F': -3, 'G':  1, 'H': -1, 'I': -1, 'K':  0, 'L': -3, 'M': -2, 'N':  1, 'P':  1, 'Q': -1, 'R':  0, 'S':  2, 'T':  1, 'V': -1, 'W': -2, 'Y': -3},
'T': {'A':  1, 'C': -2, 'D':  0, 'E': 0, 'F': -3, 'G':  0, 'H': -1, 'I':  0, 'K':  0, 'L': -2, 'M': -1, 'N':  0, 'P':  0, 'Q': -1, 'R': -1, 'S':  1, 'T':  3, 'V':  0, 'W': -5, 'Y': -3},
'V': {'A':  0, 'C': -2, 'D': -2, 'E':-2, 'F': -1, 'G': -1, 'H': -2, 'I':  4, 'K': -2, 'L':  2, 'M':  2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T':  0, 'V':  4, 'W': -6, 'Y': -2},
'W': {'A': -6, 'C': -8, 'D': -7, 'E':-7, 'F':  0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R':  2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y':  0},
'Y': {'A': -3, 'C':  0, 'D': -4, 'E':-4, 'F':  7, 'G': -5, 'H':  0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W':  0, 'Y': 10}
}

gap = 9



def find_max(matrix):
    maximum = -999999
    list_max = []
    for i in range(1, len(matrix)):
        if matrix[i][len(matrix[i])-1][0] > maximum:
            list_max = []
            list_max.append([matrix[i][len(matrix[i])-1][0], i, len(matrix[i])-1])
            maximum = matrix[i][len(matrix[i])-1][0]
        elif matrix[i][len(matrix[i])-1][0] == maximum and [matrix[i][len(matrix[i]) - 1][0], i, len(matrix[i]) - 1] not in list_max:
            list_max.append([matrix[i][len(matrix[i]) - 1][0], i, len(matrix[i]) - 1])
            maximum = matrix[i][len(matrix[i])-1][0]
    for j in range(1, len(matrix[0])):
        if matrix[len(matrix)-1][j][0] > maximum:
            list_max = []
            list_max.append([matrix[len(matrix)-1][j][0], len(matrix) - 1, j])
            maximum = matrix[len(matrix)-1][j][0]
        elif matrix[len(matrix)-1][j][0] == maximum and [matrix[len(matrix)-1][j][0], len(matrix) - 1, j] not in list_max:
            list_max.append([matrix[len(matrix)-1][j][0], len(matrix) - 1, j])
            maximum = matrix[len(matrix)-1][j][0]
    return list_max





def alignment():
    sequence1 = input()
    sequence2 = input()
    seq1 = list(sequence1)
    seq2 = list(sequence2)
    matrix = [[[0, 0] for x in range(len(seq2)+1)] for y in range(len(seq1)+1)]

    #creating a matrix with values
    for i in range (1, len(seq1)+1):
        for j in range (1, len(seq2)+1):
            num = [0, 0, 0]
            element = PAM250[seq1[i-1]]
            num[0] = matrix[i][j - 1][0] - gap
            num[1] = matrix[i - 1][j][0] - gap
            num[2] = element[seq2[j-1]] + matrix[i - 1][j - 1][0]
            matrix[i][j].pop()
            for k in range (len(num)):
                if num[k] == max(num[0], num[1], num[2]):
                    matrix[i][j][0] = num[k]
                    matrix[i][j].append(k+1)
    list_max = find_max(matrix)




# start of array
    seq = []
    for k in range (len(list_max)):
        x = list_max[k][1]
        y = list_max[k][2]
        if x != len(seq1):
            seq.append([seq1[len(seq1) - 1], '-'])
            for i in range((len(seq1) - 2), x-1, -1):
                seq[k][0] += seq1[i]
                seq[k][1] += '-'
            seq[k][0] += seq1[x - 1]
            seq[k][1] += seq2[y - 1]

        elif y != len(seq2):
            seq.append(['-', seq2[len(seq2) - 1]])
            for i in range((len(seq2) - 2), y-1, -1):
                seq[k][0] += '-'
                seq[k][1] += seq2[i]
            seq[k][0] += seq1[x - 1]
            seq[k][1] += seq2[y - 1]
        else:
            seq.append([seq1[x-1], seq2[y-1]])

    i= 0
    while i != len(seq):
        x = list_max[i][1]
        y = list_max[i][2]
        maximum = list_max[i][0]
        while x != 1 and y != 1:
            if len(matrix[x][y]) == 2:
                if matrix[x][y][1] == 1:
                    y -= 1
                elif matrix[x][y][1] == 2:
                    x -= 1
                elif matrix[x][y][1] == 3:
                    x -= 1
                    y -= 1
                if len(matrix[x][y]) == 2:
                    if matrix[x][y][1] == 1:
                        seq[i][0] += '-'
                        seq[i][1] += seq2[y - 1]
                    elif matrix[x][y][1] == 2:
                        seq[i][0] += seq1[x - 1]
                        seq[i][1] += '-'
                    else:
                        seq[i][0] += seq1[x - 1]
                        seq[i][1] += seq2[y - 1]
                elif len(matrix[x][y]) == 3:
                    save = copy.deepcopy(seq[i])
                    seq.append(save)
                    list_max.append([maximum, x, y])

                    if matrix[x][y][1] == 1:
                        seq[i][0] += '-'
                        seq[i][1] += seq2[y - 1]
                    elif matrix[x][y][1] == 2:
                        seq[i][0] += seq1[x - 1]
                        seq[i][1] += '-'
                    else:
                        seq[i][0] += seq1[x - 1]
                        seq[i][1] += seq2[y - 1]

                    if matrix[x][y][2] == 1:
                        seq[len(seq)-1][0] += '-'
                        seq[len(seq)-1][1] += seq2[y - 1]
                    elif matrix[x][y][2] == 2:
                        seq[i][0] += seq1[x - 1]
                        seq[len(seq)-1][1] += '-'
                    else:
                        seq[len(seq)-1][0] += seq1[x - 1]
                        seq[len(seq)-1][1] += seq2[y - 1]

            if len(matrix[x][y]) == 3:
                x1 = list(seq[i][0])
                last1 = x1[len(x1)-1]
                x2 = list(seq[i][1])
                last2 = x2[len(x2)-1]
                if last1 == '-':
                    y -= 1
                elif last2 == '-':
                    x -= 1
                else:
                    x -= 1
                    y -= 1
                if len(matrix[x][y]) == 2:
                    if matrix[x][y][1] == 1:
                        seq[i][0] += '-'
                        seq[i][1] += seq2[y - 1]
                    elif matrix[x][y][1] == 2:
                        seq[i][0] += seq1[x - 1]
                        seq[i][1] += '-'
                    else:
                        seq[i][0] += seq1[x - 1]
                        seq[i][1] += seq2[y - 1]
                elif len(matrix[x][y]) == 3:
                    save = copy.deepcopy(seq[i])
                    seq.append(save)
                    list_max.append([maximum, x, y])

                    if matrix[x][y][2] == 1:
                        seq[len(seq)-1][0] += '-'
                        seq[len(seq)-1][1] += seq2[y - 1]
                    elif matrix[x][y][1] == 2:
                        seq[len(seq)-1][0] += seq1[x - 1]
                        seq[len(seq)-1][1] += '-'
                    else:
                        seq[len(seq)-1][0] += seq1[x - 1]
                        seq[len(seq)-1][1] += seq2[y - 1]

                    if matrix[x][y][1] == 1:
                        seq[i][0] += '-'
                        seq[i][1] += seq2[y - 1]
                    elif matrix[x][y][1] == 2:
                        seq[i][0] += seq1[x - 1]
                        seq[i][1] += '-'
                    else:
                        seq[i][0] += seq1[x - 1]
                        seq[i][1] += seq2[y - 1]
        i += 1


    for i in range (len(seq)):
        s1 = seq[i][0].replace('-', '')
        s2 = seq[i][1].replace('-', '')
        s1 = s1[len(s1)::-1]
        s2 = s2[len(s2)::-1]
        if s1 != sequence1:
            part = ''.join(sequence1.rsplit(s1, 1))
            seq[i][0] += part[len(part)::-1]
            for k in range(len(part)):
                seq[i][1] += '-'
        if s2 != sequence2:
            part = sequence2.replace(s2, '')
            seq[i][1] += part[len(part)::-1]
            for k in range(len(part)):
                seq[i][0] += '-'

        seq[i][0] = seq[i][0][len(seq[i][0])::-1]
        seq[i][1] = seq[i][1][len(seq[i][1])::-1]


    sortedSeq = [i[0] + i[1] for i in seq]
    sortedSeq.sort()
    print(maximum)
    for i in sortedSeq:
        print(i[0:int(len(i) / 2)])
        print(i[int(len(i) / 2):])



if __name__ == '__main__':
    alignment()

