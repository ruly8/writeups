---
date: 2022-01-13
keywords: [ctf, picoctf, crypto]
---

# Mind your Ps and Qs

## Description
In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? 

The challenge provides 3 values used in RSA that can be public by design.


```
c= 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n= 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e= 65537
```

`c` is the ciphertext which is most likely going to include the flag we are after. 
`n` is one part of the RSA public key and is the result of multiplying two primes. 
`e` is the other part of the public key with `65537 = 2^16 + 1` being a common value.

## Approach

Based on the challenge description we focus on `n` first. 
`m` will represent the unencrypted message and can be calculated with `c^d mod n`. 
`c` and `n` are known but `d` is not since it represents the private key used to encrypt the original message.

`d` is calculated with the modular inverse of `e`. So `d = e^-1 mod eulerphi(n)`. 
`eulerphi(n)` is Euler's totient of `n` (Carmichael's totient might also work) and there's a few online calculators for Euler's totient function for example [alpertron.com](https://www.alpertron.com.ar/ECM.HTM) and [dcode.fr](https://www.dcode.fr/euler-totient) with the latter not liking large numbers and alpertron.com taking quite some time.
Another method of getting `eulerphi(n)` is by factoring `n` looking for `p` and `q` which are the two primes used to generate `n` initially.

[Factordb.com](http://factordb.com/) is basically exactly what the name suggests. Providing it with `n` as input it returns two values (`p,q`).

`p = 1617549722683965197900599011412144490161` and `q = 475693130177488446807040098678772442581573`

Plugging those 2 values into `(p-1)*(q-1)` gives us the same value as `eulerphi(n)`.


## Solution

Putting all the information in python to actually solve the challenge:

```py
# values provided by challenge
c= 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n= 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e= 65537

# https://www.alpertron.com.ar/ECM.HTM (took 6min)
# phi_n = 769457290801263793712740792519696786146770691257482771401340787987731866151331520 

# factordb http://factordb.com/index.php?query=769457290801263793712740792519696786147248001937382943813345728685422050738403253
p = 1617549722683965197900599011412144490161
q = 475693130177488446807040098678772442581573

phi_n = (p-1)*(q-1)

# d = e^-1 mod phi_n
d = pow(e,-1,phi_n)

# c^d = (m^e)^d = m (mod n)
m = pow(c,d,n)

res = bytes.fromhex(format(m,'x')).decode('ascii')
print("flag:",res)
```

## Flag

`picoCTF{sma11_N_n0_g0od_45369387}`
