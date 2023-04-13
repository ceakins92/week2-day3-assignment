def is_pangram(letters):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in letters:
            return False
    return True


print(is_pangram("The quick brown fox jumps over the lazy dog"))


def find_pangram(astring):
    alph_set = set(letter for letter in 'abcdefghijklmnopqrstuvwxyz')
    return len(alph_set.difference(set(astring.lower()))) < 1


print(find_pangram('The quick brown fox jumps over the lazy dog'))
print(find_pangram('abc'))
