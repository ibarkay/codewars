def checkio(textys):
    count_listy = {}
    for i in textys.lower():
        if i.isalpha():
            count_listy[i] = textys.lower().count(i)

    print count_listy
     print max(count_listy.values())

    letters_after_count = []
    for letter, nums in count_listy.items():
        if nums == max(count_listy.values()):
            letters_after_count.append(letter)

    print letters_after_count

    if len(letters_after_count) == 1:
        return letters_after_count[0]

    if len(letters_after_count) > 1:
        return min(letters_after_count)


checkio('AAbcd')