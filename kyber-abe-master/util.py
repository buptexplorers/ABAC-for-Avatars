from params import *
import random
import numpy as np
import time
import math


def can_add(matrix1, matrix2):
    """
    Returns True if two matrices can be added.
    """
    return len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0])


def can_multiply(matrix1, matrix2):
    """
    Returns True if two matrices can be multiplied.
    """
    return len(matrix1[0]) == len(matrix2)


def matrix_addition(matrix1, matrix2):
    """
    Adds two matrices element-wise.
    """
    # assert can_add(matrix1, matrix2)
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        row = poly_mod(np.array(row))
        result.append(row.tolist())
    return result


def matrix_multiplication(matrix1, matrix2):
    """
    Multiplies two matrices.
    """
    assert can_multiply(matrix1, matrix2)
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        result.append(row)
    return result

#  A uniformly randow polynomial matrix


def transpose(A):
    transposed = []

    for i in range(len(A[0])):
        row = []

        for j in range(len(A)):
            row.append(A[j][i])

        transposed.append(row)

    return transposed


# print(A)
# print(transpose(A))


def poly_mod(exp):
    """
    expression (mod (x^f + 1))
    """
    m = len(exp)
    res = exp % q
    for i in range(0, m-n):
        d = res[i]
        res[i] -= d
        res[i + n] -= d
    res = res[-n:] % q
    return res


def cbd_mod(exp):
    """
    expression (mod (x^f + 1))
    """
    m = len(exp)
    res = exp % eta
    for i in range(0, m-n):
        d = res[i]
        res[i] -= d
        res[i + n] -= d
    res = res[-n:] % eta
    return res


def poly_add(s1, s2):
    """
        t = s1 + s2
    """
    return poly_mod(np.polyadd(s1, s2))  # 多项式相加

def poly_sub(s1, s2):
    """
        t = s1 + s2
    """
    return (np.polysub(s1, s2))  # 多项式相减   #todo


def poly_mul(s1, s2):
    """
        t = s1 * s2
    """
    return poly_mod(np.convolve(s1, s2))  # convolve：卷积


def poly_dotprod(s1, s2):
    """
        t = s1[0]*s2[0] + s1[1]*s2[1] ... + s1[m-1]*s2[m-1]
    """
    n_poly = np.array([poly_mul(np.array(poly)[0], np.array(poly)[1])
                       for poly in zip(s1, s2)])
    n = [0]
    for j in n_poly:
        n = poly_add(n, j)

    return n


def matrix_vector_poly_mul(A, s):
    result = []

    for row in A:
        sum_poly = [0] * max(len(row[0]), len(s[0]))  # initialize a polynomial with zeros

        for i in range(len(row)):
            product = poly_mul(row[i], s[i])
            sum_poly = poly_add(sum_poly, product)

        result.append(sum_poly.tolist())

    return result


def timeit(code, title):
    st = time.time()
    res = code()
    end = time.time()
    t = round(end - st, 6)
    print(title, '-', round(1000*t,4), '(ms)')
    return res



def timeit1000(code, title):
    st = time.time()
    for i in range(1000):
        code()
    end = time.time()
    t = round(end - st, 6) / 1000
    print(title, '-', round(1000*t,4), '(ms)')


def getLambda(V, W, i):
    a,l = W.shape
    V_n = np.array(V)
    n1, n2, n3 = V_n.shape
    res = np.zeros(shape=(n2, n3))
    for j in range(l):
        res += W[i,j] * V_n[j]
    return res.tolist()





def string_to_M(s):
    # Convert string to binary representation
    binary_str = ''.join(format(ord(ch), '08b') for ch in s)

    # Split the binary string into chunks of size 17 (since 2^17) and convert to integers
    chunk_size = 17
    M = [int(binary_str[i:i + chunk_size], 2) for i in range(0, len(binary_str), chunk_size)]

    # Pad the last chunk if not full-sized
    if len(binary_str) % chunk_size != 0:
        padding = chunk_size - (len(binary_str) % chunk_size)
        M[-1] = int(binary_str[-(len(binary_str) % chunk_size):] + '0' * padding, 2)

    # Pad M to 256 elements if needed
    while len(M) < 256:
        M.append(0)

    return M

def M_to_string(M):
    # Convert integers in M to binary strings of size 17 (since 2^17)
    chunk_size = 17
    binary_str = ''.join(format(val, f'0{chunk_size}b') for val in M)

    # Split binary string into chunks of size 8, convert to characters
    chars = [chr(int(binary_str[i:i + 8], 2)) for i in range(0, len(binary_str), 8) if 32 <= int(binary_str[i:i + 8], 2) <= 126]

    return ''.join(chars)
#
#
# M = "I love BUPT. My name is LiJunJie"
# # M = '李俊杰 from BUPT'
# M_list = string_to_M(M)
# print(M_list)
# M_recover = M_to_string(M_list)
# print(M_recover)