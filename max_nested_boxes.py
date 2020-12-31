def annoy(B):
    '''
    Input:  B | list of box dimension triples
    Output: A | list of indicies of max nesting boxes, increasing in dimension
    '''

    def update(box):
        annoyance[box] = 1

        for value in new_sorted[box]:
            if value not in annoyance:
                update(value)
            if annoyance[value] + 1 > annoyance[box]:
                sub_boxes[box] = value
                annoyance[box] = annoyance[value] + 1

    sorted_boxes = {tuple(sorted(B[i])):i for i in range(len(B))}
    new_sorted = {i:[] for i in sorted_boxes}
    sub_boxes = {i:None for i in sorted_boxes}

    for i in sorted_boxes:
        for j in sorted_boxes:
            count = 0
            for k in range(3):
                if i[k] > j[k]:
                    count += 1
                    
            if count == 3:
                new_sorted[i].append(j)

    annoyance = {}
    indices = []

    for i in sorted_boxes:
        update(i)

    max_value = max(annoyance.values())

    for i in annoyance:
        if annoyance[i] == max_value:
            box = i

            while max_value > 0:
                indices.append(box)
                box = sub_boxes[box]
                max_value -= 1
            indices.reverse()

            return [sorted_boxes[i] for i in indices]
