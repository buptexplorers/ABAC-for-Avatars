import random

random.seed(1)


def bytes_to_bits(input_bytes):
    """
    Convert bytes to an array of bits

    Bytes are converted little endianness following the paper
    """
    bit_string = ''.join(format(byte, '08b')[::-1] for byte in input_bytes)
    return list(map(int, list(bit_string)))


def cbd(eta: int, k: int, n: int):
    """
    生成服从中心二项分布的随机数
    :param eta: 整数
    :param k: 整数，属性的数量
    :param n: 整数
    :return: 二维数组，包含k个长度为n数组
    """

    input_bytes = [[random.randint(0, n) for j in range((n >> 2) * eta)] for i in range(k)]
    coefficients = [[0 for _ in range(n)] for _ in range(k)]
    for j in range(k):
        assert (n >> 2) * eta == len(input_bytes[j])

        list_of_bits = bytes_to_bits(input_bytes[j])
        for i in range(n):
            a = sum(list_of_bits[2 * i * eta + j] for j in range(eta))
            b = sum(list_of_bits[2 * i * eta + eta + j] for j in range(eta))
            coefficients[j][i] = a - b
    return coefficients

# len(test_array) == 128
# test_array = [[-10, -42, -45, -5, -122, -36, 94, 111, -22, 89, 53, -127, 127, 87, 32, 62, -113, 7, -118, -18, -125, 9, -112, 56, 72, -28, -124, 26, -24, 87, 114, 109, -72, 96, 123, -31, -119, 106, 22, 120, 19, 101, -30, -65, 75, -65, -2, 4, 118, 18, -24, -3, 6, -8, -50, 48, -99, -71, -63, 44, -30, 57, 29, 125, -27, -54, 98, -41, -2, -61, -59, -103, 127, -102, 1, 12, 81, -9, 75, 118, -11, 117, 87, -117, 8, -102, -6, -74, -9, -80, 30, -37, -87, -83, -113, -14, 20, 78, 92, 38, 54, -18, -56, 78, 39, 87, -26, 115, 89, -22, 125, -14, -85, 82, -101, 104, -91, 75, 92, -73, 37, 44, 13, 84, -114, -23, 126, 112]]
# # test_array值在0-255
# for i in range(len(test_array)):
#     for j in range(len(test_array[i])):
#         test_array[i][j] += 127
#
# res = cbd(test_array, 2, 1, 256)
# print(res)