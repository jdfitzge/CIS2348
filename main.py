def selection_sort_descend_trace(mod):
    for i in range(len(mod) - 1):
        max_ind = i
        for j in range(i + 1, len(mod)):
            if mod[j] > mod[max_ind]:
                max_ind = j
        mod[i], mod[max_ind] = mod[max_ind], mod[i]
        print(' '.join([str(x) for x in mod]),'')
    return mod
if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)