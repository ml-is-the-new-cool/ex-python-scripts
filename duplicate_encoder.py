import collections


def duplicate_encode(word):
    """
    This solution is O(n) instead of O(n^2) like the methods that use .count()
    because .count() is O(n) and it's being used within an O(n) method.
    The space complexiety is increased with this method.
    """
    # ensure word is in lower case
    word = word.lower()
    
    # use a defaultdict to avoid initialization of each key
    frequencies = collections.defaultdict(int)
    for letter in word:    
        frequencies[letter] += 1
    
    # encode the word
    encoded_word = ''
    for letter in word:
        encoded_word += ')' if frequencies[letter] > 1 else '('
    return encoded_word


def bad_duplicate_encode(word):
    """
    This solution is O(n^2).
    """
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])


if __name__ == "__main__":
    print(duplicate_encode("din"), "<->", "(((")
    print(duplicate_encode("recede"), "<->", "()()()")
    print(duplicate_encode("Success"), "<->", ")())())", "should ignore case")
    print(duplicate_encode("(( @"), "<->", "))((")
