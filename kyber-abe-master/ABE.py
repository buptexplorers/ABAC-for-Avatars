from CBD import cbd
from Compress import Compress, Decompress
import random
import numpy as np
from util import poly_dotprod, poly_add, matrix_addition, matrix_vector_poly_mul, transpose, poly_sub, getLambda
from KeyCons import KeyCons


def Setup(n: int, k: int, q: int, eta: int, attributeSet: list, seed=1):
    """
    生成每个属性对应的密钥参数集

    :param n: kyber n
    :param k: kyber k
    :param q: 质数
    :param eta:
    :param attributeSet: 总属性列表
    :param seed: 随机数种子
    :return: 字典："属性" : "密钥参数"。
    ——————————————（1） R ——————————————————
    R是私钥字典，其键为属性值，例如A B C D等，对应的值通过中心二项式分布得到，长度为k的列表，
    每一列表元素为一个n次的多项式（即一个长度为n的子列表）
    ——————————————（2）CBD 函数——————————————

    """

    R = {}
    random.seed(seed)
    for i in range(len(attributeSet)):
        R[attributeSet[i]] = cbd(eta, k, n)
    return R


def SKGen(R: dict, userAttributes: list):
    """
    根据用户的属性列表生成用户私钥

    :param R: 密钥参数字典
    :param userAttributes: 用户属性集合
    :return: 用户私钥字典: "用户属性" : "涉及用户属性的密钥参数"
    此处返回的私钥，是根据Setup中存储的字典R进行查找，寻找用户的属性对应的，
    """
    sk = {}
    for userAttribute in userAttributes:
        assert userAttribute in R, "user attribute is invalid, please check again"
        sk[userAttribute] = R[userAttribute]
    return sk
#
# sk = SKGen(R,userAttributes)
# print(len(sk['D'][0]))


def PKGen(R:dict, k: int, eta: int, q: int, n: int, seed=1):
    """
    生成公钥

    :param R: 密钥参数字典
    :param T: 访问策略树：访问策略是为析取式，该T包含的每个列表表示一个范式中的属性
    :param k: kyber k
    :param eta: kyber eta
    :param q: 质数
    :param n: kyber n
    :param seed: 随机数种子
    :return:
    """
    random.seed(seed)
    A = [[[random.randint(0, q) for _ in range(n)] for _ in range(k)] for _ in range(k)]
    t = []
    for Ri in R:
        ei = cbd(eta, k, n)

        A_S = matrix_vector_poly_mul(A,R[Ri])
        t.append(Compress(matrix_addition(A_S, ei), q, 27))

    pk = {}
    pk["A"] = A
    pk["T"] = t
    return pk


def Encrypt(pk: dict, M: list, W: np.ndarray, eta: int, k: int, q: int, n: int):
    """
    加密
    :param pk: 公钥 字典 A:随机矩阵A T:压缩后的RLWE多项式
    :param M: 加密信息
    :param W: 策略矩阵
    :param eta: kyber eta
    :param k: kyber k
    :param q: 质数
    :param n: kyber n
    :return: 返回加密密文
    """

    a, l = W.shape
    A = pk['A']
    c2 = []
    c1 = []      #vi
    C = {}

    # generate V: (s,d2,...,dl)
    V = []
    for i in range(l):
        V.append(cbd(eta, k, n))

    round_q = round(q / (2 ** 17))
    M_q = [round_q * item for item in M]

    for i in range(l):
        tii = Decompress(pk["T"][i], q, 27)    # 1: Decompress(pk, q, dt)
        ei1 = cbd(eta, 1, n)           # 4: e1 <-- beta_n

        tii_dot_s = poly_dotprod(tii, V[0])
        c1.append(Compress(poly_add(poly_add(tii_dot_s, ei1[0]).tolist(), M_q).tolist(), q, 21))

    for i in range(a):
        lambdaI = getLambda(V, W, i)
        ei0 = cbd(eta,k,n)
        A_T = transpose(A)
        A_lambda = matrix_vector_poly_mul(A_T, lambdaI)
        c2.append(Compress(matrix_addition(A_lambda, ei0), q, 28))    #Compress(z)

    C['c1'] = c1
    C['c2'] = c2

    return C


def Decrypt(C, sk, U, q):

    c1 = C['c1']      #vi
    Z = C['c2']


    r = sk["A"]

    c1_decompress = []
    z_decompress = []

    for i in range(len(c1)):
        c1_decompress.append(Decompress(c1[i], q, 21))
        z_decompress.append(Decompress(Z[i], q, 28))

    w = poly_dotprod(r, z_decompress[0])
    for i in range(1,len(c1)):
        w += poly_dotprod(r, z_decompress[i])
    w = w.tolist()

    c1_s_z = [a - b for a, b in zip(c1_decompress[0][0], w)]
    # print('mod test', poly_mod(v_s_u))
    M_de = Compress(c1_s_z,q,17)

    return M_de















