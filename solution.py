# function to keep only Alphabets
def keep_Alphabet(word):
    alpha_only = ''
    for l in word:
        if l.isalpha() == True:
            alpha_only += l
    return alpha_only


# function to convert all the letters to lowercase
def convert_to_lowercase(word):
    lower = ''
    for l in word:
        lower += l.lower()
    return lower


# function to keep only 'a's , 'b's, and 'c's
def clean_string(word):
    cleaned = ''
    for l in word:
        if l == 'a' or l == 'b' or l == 'c':
            cleaned += l
    return cleaned


# function to convert adjacent distinct characters to the third character
def convert_to_third(char1, char2):
    if (char1 == 'a' and char2 == 'b') or (char1 == 'b' and char2 == 'a'):
        return 'c'
    elif (char1 == 'a' and char2 == 'c') or (char1 == 'c' and char2 == 'a'):
        return 'b'
    else:
        return 'a'


# function to get places where I can make any replacements
def find_possible_positions(str):
    possible_pos = []
    for ind in range(len(str) -1):
        if str[ind] != str[ind+1]:
            possible_pos.append(ind)

    return possible_pos


# function o replace the pos and pos+1 with the third character
def replace(word, pos):
    return word[0:pos] + convert_to_third(word[pos], word[pos+1]) + word[pos+2:]


# function to remove duplicates from a list
def keep_distinct(list):

    distinct = []
    for l in list:
        if l not in distinct:
            distinct.append(l)

    return distinct


# function to keep strings with minimum length
def keep_minimum(list):
    list_with_minmum_length = []
    minimum_length = len(list[0])
    for stri in list:
        if len(stri) < minimum_length:
            minimum_length = len(stri)

    for stri in list:
        if len(stri) == minimum_length:
            list_with_minmum_length.append(stri)

    return list_with_minmum_length


# function to Shorten the string
def shortening_string(word):

    possible_postions = find_possible_positions(word)
    solutions = []

    if len(possible_postions) == 0:
        solutions.append(word)
    else:
        for move in possible_postions:
            solutions.extend(shortening_string(replace(word, move)))

        solutions = keep_minimum(solutions)
        solutions = keep_distinct(solutions)

    return solutions


if __name__ == "__main__":

    word = 'cab'
    word = keep_Alphabet(word)
    word = convert_to_lowercase(word)
    word = clean_string(word)

    print(shortening_string(word))