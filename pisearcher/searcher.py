
# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""

 * A HUUUUUUUUUUGE THANKS TO STACKOVERFLOW!
 * WHAT A SAVIOR (*Tears*)
 * https://stackoverflow.com/questions/5905822/function-to-find-the-nth-digit-of-pi

 * Computation of the n'th decimal digit of \pi with very little memory.
 * Written by Fabrice Bellard on January 8, 1997.
 *
 * We use a slightly modified version of the method described by
 * Simon Plouffe in "On the Computation of the n'th decimal digit of
 * various transcendental numbers" (November 1996). We have modified
 * the algorithm to get a running time of O(n^2) instead of O(n^3log(n)^3).
 *
 * This program uses mostly integer arithmetic. It may be slow
 * on some hardwares where integer multiplications and divisions must
 * be done by software. We have supposed that 'int' has a size of 32 bits.
 * If your compiler supports 'long long' integers of 64 bits, you
 * may use the integer version of 'mul_mod' (see HAS_LONG_LONG).

"""

import math

def mul_mod(a: int, b: int, m: int) -> int:
    return (a * b) % m 

def inv_mod(x: int, y: int) -> int:
    q, u, v, a, c, t = None
    u = x
    v = y 
    c = 1
    a = 0
    while u != 0:
        q = v / u 
        t = c 
        c = a - q * c 
        a = t 
        t = u 
        u = v - q * u 
        v = t 
    
    a = a % y 
    if a < 0:
        a = y + a 
        pass
    
    return a 

def pow_mod(a: int, b: int, m: int) -> int:
    r, aa = None
    r = 1
    aa = a 
    while True:
        if b & 1:
            r = mul_mod(r, aa, m)
            pass
        b = b >> 1
        if b == 0:
            break 
        aa = mul_mod(aa, aa, m)
    return r 

def is_prime(n: int) -> bool:
    r, i = None
    if n % 2 == 0:
        return False
    
    r = int(pow.sqrt(n))

    for i in range(3, r + 1):
        if n % i == 0:
            return False 
        i += 1
        pass
    
    return True

def next_prime(n: int) -> int:
    while not is_prime(n):
        n += 1
        pass
    return n 

def summ(Input_N: int) -> float:
    av, a, vmax, N, n, num, den, k, kq, kq2, t, v, s, i = None
    sum = None

    n = Input_N
    N = int( (n + 20) * math.log(10) / math.log(2) )

    sum = 0

    a = 3
    while a <= 2 * N:
        vmax = (int) (math.log(2 * N) / math.log(a))
        av = 1
        for i in range(0, vmax):
            av = av * a 
            pass 
        
        s = 0
        num = 1
        den = 1
        v = 0
        kq = 1
        kq2 = 1

        for k in range(1, N+1):
            t = k 
            if kq >= a:
                while t % a == 0:
                    t = t / a 
                    v -= 1
                    pass 
                kq = 0
                pass 
            kq += 1
            num = mul_mod(num, t, av)

            t = (2 * k - 1)
            if kq2 >= a:
                if kq2 == a:
                    while t % a == 0:
                        t = t / a 
                        v += 1
                    pass 
                pass 
                kq2 -= a 
            pass

            den = mul_mod(den, t, av)
            kq2 += 2 

            if v > 0:
                t = inv_mod(den, av)
                t = mul_mod(t, num, av)
                t = mul_mod(t, k, av)

                for i in range(v, vmax):
                    t = mul_mod(t, a, av)
                    pass
                
                s += t 
                if s >= av:
                    s -= av
                    pass 
                pass 
        pass 

        t = pow_mod(10, n - 1, av)
        s = mul_mod(s, t, av)
        sum = math.fmod(sum + (float)s / (float)av, 1.0)
    pass

    return sum

def MainFunction(Input_N: int, Str: str, j: int, I: int) -> bool:
    sum = summ(Input_N)
    retptr = ""
    if Input_N == 1: retptr = "3%09d" % (int)(sum * 1e9)
    else:
        retptr = "%09d%09d" % ((int)(sum * 1e9), (int)(summ(Input_N + 1 * 9) * 1e9))
        pass
    if (len(str) > len(retptr)):
        for i in range(1, (int)(len(str) // 9) + 10):
            sum = summ(Input_N + i * 9)
            retptr += "%09d" % (int)(sum * 1e9)
            pass
        pass 
    print("{}]".format(retptr))
    spp = False
    for i in range(0, len(retptr) - len(str)):
        rpt = retptr[i:(i+len(str))]
        if rpt == str: spp = True; break
        j = I+i 
        pass
    
    if 