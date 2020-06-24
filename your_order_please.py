def easy_and_dirty_order(sentence):
    """
    Time complexity O(3n).
    Easy and dirty solution.
    """
    if not len(sentence):
        return ""
    
    words = sentence.split(" ")
    pos = [None] * len(words)
    
    for word in words:
        for letter in word:
            if letter.isdigit():
                pos[int(letter)-1] = word
    
    return " ".join(pos)

def order(sentence):
    """
    Time complexity O(3n).
    Elegant and pythonic solution.
    """
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))

if __name__ == "__main__":
    print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
    print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
    print(order(""), "")
