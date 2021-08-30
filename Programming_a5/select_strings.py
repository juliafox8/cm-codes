def select_strings(names, letter):
    #base case 
    if names == []:
        return []
    first_name = names[0]

    if first_name == '':
        return select_strings(names[1:], letter)

    if first_name[-1] == letter:
        return [first_name] + select_strings(names[1:], letter) 
    return select_strings(names[1:], letter)


def select_strings_backward(names, letter):
    #base case 
    if names == []:
        return []
    last_name = names[-1]

    if last_name == '':
        return select_strings_backward(names[:-1], letter)

    if last_name[-1] == letter:
        return [last_name] + select_strings_backward(names[:-1], letter) 
    
    return select_strings_backward(names[:-1], letter)


