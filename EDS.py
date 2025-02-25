import random

# 4. A) MRT : Use Miller-Rabin Primality Test to choose a prime number with
#       512 bits and check the primality test.
def miller_rabin_test(n, s=5):
    """Perform the Miller-Rabin Primality Test on n with s iterations."""
    # print (f"Running Miller-Rabin Primality test with n: {n}")
    # Write n-1 as 2^u * r
    u, r = 0, n - 1
    while r % 2 == 0:
        u += 1 
        r //= 2

    # Algorithm
    for i in range(s):
        a = random.randint(2, n - 2)
        # print(f"Iteration {i+1}: a = {a}")
        z = pow(a, r, n)
        if z == 1 or z == n - 1:
            continue
        for _ in range(u - 1):
            z = pow(z, 2, n)
            if z == n - 1:
                break
        else:
            return False
    return True

# 4. B) EA : Use Euclidean Algorithm to evaluate gcd.
def EA_gcd(a, b):
    # Euclidean Algorithm to find the GCD.

    # Initially a is r0 and b is r1
    # While ri is not 0
    while b != 0:
        # ri = r(i-2) % r(i-1)
        a, b = b, a % b
    return a

# 4. C) EEA : Use Extended Euclidean Algorithm to find modular inverse of the value.
def EEA_gcd(a, b):
    # Initialize the coefficients
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    # Find the GCD and the coefficients
    while b != 0:
        q = a // b
        a, b = b, a % b
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    gcd = a
    s = s0
    t = t0
    return gcd, s, t

def EEA_mod_inverse(a, m):
    gcd, s, t = EEA_gcd(a, m)
    if gcd != 1:
        print(f"No modular inverse exists for {a} and {m}")
    else:
        # Modular of a is a number x such that (a * x) % m = 1
        # since (a * s) % m = 1, s is the modular inverse of a
        return s % m

# 4. D) powmod_sm : Use Square and Multiply Algorithm to evaluate exponentiation.
def powmod_sm(base, exp, n):
    exp_b = bin(exp)
    value = base
    for i in range(3, len(exp_b)):
        value = (value ** 2) % n
        if exp_b[i] == '1':
            value = (value * base) % n
    return exp_b, value

# 4. Use the above functions to implement ElGamal Digital Signature

# Generate an odd integer with the given number of bits.
def generate_prime_candidate(bits):
    p = random.getrandbits(bits)
    # Check if the number is even and if it is not, generate another number
    while p & 1 != 1:
        p = random.getrandbits(bits)
    return p

# Generate a prime number with given number of bits.
def generate_prime(bits):
    p = generate_prime_candidate(bits)
    while not miller_rabin_test(p):
        p = generate_prime_candidate(bits)
    return p

# Generate ElGamal key pair.
def elgamal_keygen(bits):
    # Choose a large prime number p
    p = generate_prime(bits)
    # Choose a primitive element alpha of Z*p
    alpha = random.randint(2, p - 2)
    # Choose a random integer prk in the range [1, p-2] which becomes our private key
    prk = random.randint(2, p - 2)
    # Compute the public key beta = alpha^d mod p
    exp_b, beta = powmod_sm(alpha,prk, p)
    return p, alpha, beta, prk

# Sign a message using ElGamal algorithm.
def elgamal_sign(p, alpha, d, message):
    #Choose a random ephemeral key k in the range [0, p-2]
    k = random.randint(0, p - 2)
    # Ensure that the greatest common divisor of k and p-1 is 1
    gcd = EA_gcd(k, p - 1)
    while gcd != 1:
        k = random.randint(1, p - 2)
        gcd = EA_gcd(k, p - 1)
    # Compute signature parameters r and s
    r = pow(alpha, k, p)
    k_inv = EEA_mod_inverse(k, p - 1)
    s = (k_inv * (message - d * r)) % (p - 1)
    return r, s

# Verify a signed message using ElGamal algorithm.
def elgamal_verify(p, alpha, pubk, message, r, s):
    t1 = pow(pubk, r, p) * pow(r, s, p) % p
    t2 = pow(alpha, message, p)
    return t1 == t2

# Generate ElGamal key pair
p, alpha, pubk, prk = elgamal_keygen(512)
print(f"ElGamal key pair:\np: {p}\nalpha: {alpha}\Public key: {pubk}\nPrivate key: {prk}\n")

# Sign a message
message = 5049382716
r, s = elgamal_sign(p, alpha, prk, message)
print(f"Signature:\nr: {r}\ns: {s}\n")

# Verify the signature
status = elgamal_verify(p, alpha, pubk, message, r, s)
print(f"Is the signature valid? {status}")
