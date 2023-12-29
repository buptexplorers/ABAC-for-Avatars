KYBER_POLY_BYTES = 256   # before: 384
KYBER_N = 256
KYBER_ETAK512 = 3
KYBER_ETAK768_1024 = 2
KYBER_Q_INV = 62209
KYBER_Q = 3329
KYBER_SYM_BYTES = 32
KYBER_POlYVEC_BYTES_512 = 2 * KYBER_POLY_BYTES
KYBER_POlYVEC_BYTES_768 = 3 * KYBER_POLY_BYTES
KYBER_POlYVEC_BYTES_1024 = 4 * KYBER_POLY_BYTES
KYBER_POLY_COMPRESSED_BYTES_512 = 128
KYBER_POLY_COMPRESSED_BYTES_768 = 128
KYBER_POLY_COMPRESSED_BYTES_1024 = 160
KYBER_POLYVEC_COMPRESSED_BYTES_K512 = 2 * 320
KYBER_POLYVEC_COMPRESSED_BYTES_K768 = 3 * 320
KYBER_POLYVEC_COMPRESSED_BYTES_K1024 = 4 * 352
KYBER_INDCPA_PUBLICKEYBYTES_K512 = KYBER_POlYVEC_BYTES_512 + KYBER_SYM_BYTES
KYBER_INDCPA_PUBLICKEYBYTES_K768 = KYBER_POlYVEC_BYTES_768 + KYBER_SYM_BYTES
KYBER_INDCPA_PUBLICKEYBYTES_K1024 = KYBER_POlYVEC_BYTES_1024 + KYBER_SYM_BYTES

# KYBER_512SK_BYTES is a constant representing the byte length of private keys in Kyber-512
KYBER_512SK_BYTES = KYBER_POlYVEC_BYTES_512 + ((KYBER_POlYVEC_BYTES_512 + KYBER_SYM_BYTES) + 2 * KYBER_SYM_BYTES)
KYBER_768SK_BYTES = KYBER_POlYVEC_BYTES_768 + ((KYBER_POlYVEC_BYTES_768 + KYBER_SYM_BYTES) + 2 * KYBER_SYM_BYTES)
KYBER_1024SK_BYTES = KYBER_POlYVEC_BYTES_1024 + ((KYBER_POlYVEC_BYTES_1024 + KYBER_SYM_BYTES) + 2 * KYBER_SYM_BYTES)

KYBER_INDCPA_SECRETKEY_BYTES_K512 = 2 * KYBER_POLY_BYTES
KYBER_INDCPA_SECRETKEY_BYTES_K768 = 3 * KYBER_POLY_BYTES
KYBER_INDCPA_SECRETKEY_BYTES_K1024 = 4 * KYBER_POLY_BYTES


KYBER_SS_BYTES = 32

n = 256
k = 3
q = 4194304001
eta = 4