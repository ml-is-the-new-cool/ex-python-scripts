def convert_integer_to_bits(n, n_max_bits=16):
    """
    Convert an integer to a list of bits in big endianness notation.
    
    The idea of the algorithm is to shift `n` incrementaly from 
    0 to `n_max_bits` and to use AND binary operator with the result in
    order to see if the current remaining.
    
    For educational purpose. In production, you should use :
    `format(n, f"{n_max_bits}b"`
    """
    assert(n >= 0), 'input should be >= 0'
    
    for i in range(n_max_bits):
        print("(", n, ">>", i, ") = (", str(n >> i), "& 1) =", str((n >> i) & 1))
    
    return ''.join(reversed(
        [str((n >> i) & 1) for i in range(n_max_bits)]
    ))


def count_bits_equal_to_1(n):
    return n.count('1')


if __name__ == "__main__":
    n = 1234
    n_max_bits = 16

    n_as_bits = convert_integer_to_bits(n, n_max_bits)

    print("own method    :", n_as_bits)
    print("format method :", format(n, f"0{n_max_bits}b"))
    print("number of bits equal to 1 :", count_bits_equal_to_1(n_as_bits))
