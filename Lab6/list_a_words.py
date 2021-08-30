def list_a_words(lst):
    if lst == []:
        return []
    if isinstance(lst[0], str) == True:
        if (lst[0] != "") and (lst[0][0] == 'a'):
            return lst[0] + list_a_words(lst[1:])

