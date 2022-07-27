from operator import indexOf


def letter_counter(string, l):
    """Ищет количество вхождений символа в строку"""

    count = 0
    for s in string:
        if s == l:
            count += 1
    return count


def letter_counter_2(string, l):
    return string.count(l)


def letter_counter_3(string, l):
    letters = {}
    for s in string:
        if s in letters:
            letters[s] += 1
        else:
            letters[s] = 1
 
    try:
        return letters[l]
    except KeyError:
        return 0


print(letter_counter('some strange string!', '!'))
print(letter_counter_2('some strange string!', 's'))
print(letter_counter_3('some strange string!', 'dd'))