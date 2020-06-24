import numpy as np

def extract_foo(x):
    return x.size


def extract_foo_of_foo(x):
    return [x.size for _ in range(18)]


def extract_feats():
    input_array = np.ones((36,))
    output_matrix = np.empty((36, 22))

    for x_idx, x_val in enumerate(input_array):
        output_matrix[x_idx, 0:4] = [
            extract_foo(x_val),
            extract_foo(x_val),
            extract_foo(x_val),
            extract_foo(x_val),
        ]

        output_matrix[x_idx, 4:22] = extract_foo_of_foo(x_val)

    return output_matrix


if __name__ == "__main__":
    print(extract_feats())

