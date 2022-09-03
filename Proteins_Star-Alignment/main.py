import numpy as np
import heapq
import operator

def input_data():
    numbers = input()
    proteins = []
    for i in range(int(numbers)):
        proteins.append(input())
    return proteins


def kth_largest(arr, k):
    # Sort the given array
    s_arr = arr.copy()
    s_arr.sort(reverse=True)

    # Return k'th element in the
    # sorted array
    for i in range(len(arr)):
        if arr[i] == s_arr[k-1]:
            index = i
            break
    return s_arr[k-1], index

# def input_protain():


def global_align(x, y, s_match, s_mismatch, s_gap):
    A = []
    for i in range(len(y) + 1):
        A.append([0] * (len(x) + 1))

    for i in range(len(y) + 1):
        A[i][0] = s_gap * i

    for i in range(len(x) + 1):
        A[0][i] = s_gap * i

    for i in range(1, len(y) + 1):
        for j in range(1, len(x) + 1):
            A[i][j] = max(A[i][j - 1] + s_gap, A[i - 1][j] + s_gap,
                          A[i - 1][j - 1] + (s_match if (y[i - 1] == x[j - 1] and y[i - 1] != '-') else 0) + (
                              s_mismatch if (y[i - 1] != x[j - 1] and y[i - 1] != '-' and x[j - 1] != '-') else 0) + (
                              s_gap if (y[i - 1] == '-' or x[j - 1] == '-') else 0))
    align_X = ""
    align_Y = ""
    i = len(x)
    j = len(y)

    while i > 0 or j > 0:
        current_score = A[j][i]
        if i > 0 and j > 0 and (
                ((x[i - 1] == y[j - 1] and y[j - 1] != '-') and current_score == A[j - 1][i - 1] + s_match) or
                ((y[j - 1] != x[i - 1] and y[j - 1] != '-' and x[i - 1] != '-') and current_score == A[j - 1][
                    i - 1] + s_mismatch) or
                ((y[j - 1] == '-' or x[i - 1] == '-') and current_score == A[j - 1][i - 1] + s_gap)):

            align_X = x[i - 1] + align_X
            align_Y = y[j - 1] + align_Y
            i = i - 1
            j = j - 1

        elif i > 0 and (current_score == A[j][i - 1] + s_gap):
            align_X = x[i - 1] + align_X
            align_Y = "-" + align_Y
            i = i - 1
        else:
            align_X = "-" + align_X
            align_Y = y[j - 1] + align_Y
            j = j - 1

    return (align_X, align_Y, A[len(y)][len(x)])



def A_star(proteins):

    # print(123456789013456789, proteins)
    scores = np.zeros((len(proteins), len(proteins)))
    for i in range(len(proteins)):
        for j in range(i+1, len(proteins)):
            x, y, score = global_align(proteins[i], proteins[j], 3, -1, -2)
            scores[i][j], scores[j][i] = score, score

    # for i in scores:
        # print(i)
    sums = []
    for i in scores:
        sums.append(int(np.sum(i)))
    center = proteins[np.argmax(sums)]
    dict_sums = {}
    for i in range(len(sums)):
        dict_sums[i] = sums[i]
    dict_sums = dict(sorted(dict_sums.items(), key=operator.itemgetter(1),reverse=True))
    all_alignments = []
    all_gaps = []


    # print(111111, sums, proteins)
    old_gap_center = []

    for i in range(1, len(sums)):

        align_X, align_Y, s = global_align(center, proteins[list(dict_sums.keys())[i]], 3, -1, -2)
        # print(align_X, align_Y, s)
        # print(1, all_alignments)
        center = align_X
        if len(all_alignments) > 0:
            all_alignments[0] = align_X
        else:
            all_alignments.append(align_X)
        all_alignments.append(align_Y)
        # print(12356, all_alignments)
        gap_center = []
        gap_y = []
        x = [char for char in align_X]
        for j in range(len(x)):
            if x[j] == '-':
                gap_center.append(j)
        # print(gap_center)
        # print(0, gap_center)
        y = [char for char in align_Y]
        for j in range(len(y)):
            if y[j] == '-':
                gap_y.append(j)
        # print(gap_y)

        # print(gap_y, gap_center, old_gap_center)
        s2 = old_gap_center.copy()
        # print(1, gap_center, old_gap_center)
        for j in range(len(old_gap_center)):
            for k in range(len(gap_center)):
                # print('hii')
                if gap_center[k] < old_gap_center[j]:
                    # print('bye')
                    # old_gap_center[j] += 1
                    s2[j] += 1
        # print(2, gap_center, old_gap_center, s2)
        for j in range(1, len(all_alignments)-1):
            # print(all_alignments[j])
            for k in gap_center:
                # and len(all_alignments[0]) < len(all_alignments[j])
                if k not in gap_y and k not in old_gap_center :
                # if k not in gap_y and k not in s2:
                    # print(k)
                    if len(all_alignments[j]) < len(all_alignments[0]):
                        all_alignments[j] = all_alignments[j][:k] + '-' + all_alignments[j][k:]

        old_gap_center = gap_center
        # print(all_alignments, '\n\n')
    # print(all_alignments ,'\n\n\n\n\n')
    return all_alignments


def get_score(proteins):
    match = 3
    mismatch = -1
    gap_gap =0
    gap = -2
    score = 0
    # print(proteins)
    for i in range(len(proteins)):
        if i < len(proteins):
            for j in range(i+1, len(proteins)):
                for k in range(len(proteins[0])):
                    if proteins[i][k] == proteins[j][k]:
                        if proteins[i][k] == '-':
                            score += gap_gap
                        else:
                            score += match
                    else:
                        if proteins[i][k] == '-' or proteins[j][k] == '-':
                            score += gap
                        else:
                            score += mismatch
    # print(score)
    return score




def block(proteins, score):
    while True:
        start, finish = -1, -1

        for j in range(len(proteins[0])):
            for i in range(len(proteins)):
                p = proteins[0][j]
                if start == -1:
                    if proteins[i][j] != p:
                        start = j
                else:
                    # print(i, j)
                    if proteins[i][j] != p:
                        continue
                    if proteins[i][len(proteins) - 1] != p:
                        # print('llllll')
                        finish = j
                    if finish - start == 1:
                        start, finish = -1, -1
                # print(start, finish)
        # print(1234567890, start, finish)

        alignments = []
        alignments2 = []
        for i in range(len(proteins)):
            p = [char for char in proteins[i]]
            s = ''
            for j in range(start, finish + 1):
                if p[j] != '-':
                    s += p[j]
            alignments.append(s)
        # print(123, alignments)

        pro = A_star(alignments)
        # print(987654321, pro)

        for i in range(len(pro)):
            p = [char for char in pro[i]]
            s = ''
            for j in range(len(p)):
                if p[j] != '-':
                    s += p[j]
            alignments2.append(s)
        # print(alignments2)

        for i in range(len(alignments)):
            for j in range(len(alignments2)):
                if alignments[i] == alignments2[j] and i != j:
                    # swap = alignments[j]
                    # alignments[j] = alignments[i]
                    # alignments[i] = swap
                    swap = pro[j]
                    pro[j] = pro[i]
                    pro[i] = swap
                    swap = alignments2[j]
                    alignments2[j] = alignments2[i]
                    alignments2[i] = swap
        # print(123456789, pro)
        # print(proteins)

        # if score > get_score()
        proteins2 = proteins.copy()

        x = []
        for i in range(len(proteins2)):
            p = [char for char in proteins2[i]]
            # p2 = [char for char in pro[i]]
            s = ''
            for j in range(len(proteins2[i])):
                if j < start or j > finish:
                    s += p[j]
                else:
                    s += pro[i]
                    break
            x.append(s)

        # print('end', x)
        # print(get_score(x))
        if score < get_score(x):
            proteins, score = x, get_score(x)
        else:
            return proteins, score



    #     s = ''
    #     for j in range(start, finish + 1):
    #         if p[j] != '-':
    #             s += p[j]
    #     alignments.append(s)




    # for i in range(len(proteins)):
    #     p = [char for char in proteins[i]]
    #     s = ''
    #     for j in range(start, finish+1):
    #         if p[j] != '-':
    #             s += p[j]
    #     alignments.append(s)






def output(input, output):
    # print(input )
    # print(12, output)
    test = []
    for i in range(len(output)):
        p = [char for char in output[i]]
        s = ''
        for j in range(len(p)):
            if p[j] != '-':
                s += p[j]
        test.append(s)
    # print(test)

    for i in range(len(input)):
        for j in range(len(test)):
            if input[i] == test[j] and i != j:
                # swap = alignments[j]
                # alignments[j] = alignments[i]
                # alignments[i] = swap
                # print('dngfdnsbfd')
                swap = test[j]
                test[j] = test[i]
                test[i] = swap
                swap = output[j]
                output[j] = output[i]
                output[i] = swap

    # print(123456789, output)
    print(get_score(output))
    for i in range(len(output)):
        print(output[i])
    # print(proteins)






if __name__ == '__main__':
    proteins = input_data()
    all_proteins = A_star(proteins)
    score = get_score(all_proteins)
    proteins2, score2 = block(all_proteins, score)
    # print('hiiiii', proteins2, score2)
    output(proteins, proteins2)


