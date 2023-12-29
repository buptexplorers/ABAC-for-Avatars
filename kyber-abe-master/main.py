from SPMGen import SPMGen
from params import n, k, q, eta
from ABE import *
from util import timeit, string_to_M, M_to_string, timeit1000
from testPolicyTree import *


def singleAttrTest():
    M1 = "This is an attribute encryption and decryption test text"
    print("明文: {}".format(M1))
    M = string_to_M(M1)

    seed = 1

    W = SPMGen(np.array([[1]]), 0, testTreeSingleAttr.root)
    print("策略矩阵为: \n{}".format(W))

    att_list = ['A']
    R = Setup(n, k, q, eta, att_list, seed)
    timeit(lambda: Setup(n, k, q, eta, att_list), '初始化时间')
    userAttributes = ['A']

    sk = SKGen(R, userAttributes)
    timeit(lambda: SKGen(R, userAttributes), '私钥生成时间')

    pk = PKGen(R, k, eta, q, n, seed)
    timeit(lambda: PKGen(R, k, eta, q, n), '公钥生成时间')

    C = Encrypt(pk, M, W, eta, k, q, n)
    timeit1000(lambda: Encrypt(pk, M, W, eta, k, q, n), '加密时间')

    M_de = Decrypt(C, sk, [" "], q)
    timeit1000(lambda: Decrypt(C, sk, [" "], q), '解密时间')

    print("解密结果: {}".format(M_to_string(M_de[0])))


def andTest():
    M1 = "This is an attribute encryption and decryption test text"
    print("明文: {}".format(M1))
    M = string_to_M(M1)

    seed = 3

    W, _ = SPMGen(np.array([[1]]), 0, testTreeAnd.root)
    print("策略矩阵为: \n{}".format(W))

    att_list = ['A', 'B']
    R = Setup(n, k, q, eta, att_list, seed)
    timeit(lambda: Setup(n, k, q, eta, att_list), '初始化时间')
    userAttributes = ['A', 'B']

    sk = SKGen(R, userAttributes)
    timeit(lambda: SKGen(R, userAttributes), '私钥生成时间')

    pk = PKGen(R, k, eta, q, n, seed)
    timeit(lambda: PKGen(R, k, eta, q, n), '公钥生成时间')

    C = Encrypt(pk, M, W, eta, k, q, n)
    timeit1000(lambda: Encrypt(pk, M, W, eta, k, q, n), '加密时间')

    M_de = Decrypt(C, sk, [" "], q)
    timeit1000(lambda: Decrypt(C, sk, [" "], q), '解密时间')

    print("解密结果: {}".format(M_to_string(M_de[0])))


def orTest():
    M1 = "This is an attribute encryption and decryption test text"
    print("明文: {}".format(M1))
    M = string_to_M(M1)

    seed = 2

    W, _ = SPMGen(np.array([[1]]), 0, testTreeOr.root)
    print("策略矩阵为: \n{}".format(W))

    att_list = ['A', 'B']
    R = Setup(n, k, q, eta, att_list, seed)
    timeit(lambda: Setup(n, k, q, eta, att_list), '初始化时间')
    userAttributes = ['A', 'B']

    sk = SKGen(R, userAttributes)
    timeit(lambda: SKGen(R, userAttributes), '私钥生成时间')

    pk = PKGen(R, k, eta, q, n, seed)
    timeit(lambda: PKGen(R, k, eta, q, n), '公钥生成时间')

    C = Encrypt(pk, M, W, eta, k, q, n)
    timeit1000(lambda: Encrypt(pk, M, W, eta, k, q, n), '加密时间')

    M_de = Decrypt(C, sk, [" "], q)
    timeit1000(lambda: Decrypt(C, sk, [" "], q), '解密时间')

    print("解密结果: {}".format(M_to_string(M_de[0])))

if __name__ == '__main__':
    print("******************* 单属性测试 *******************")
    singleAttrTest()
    print("******************* 双属性或测试 ******************")
    orTest()
    print("******************* 双属性与测试 ******************")
    andTest()

