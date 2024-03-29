# Sum-O-Primes

Given:
- `x = p + q`
- `n = p * q`
- Ciphertext `c` and public exponent `e` 
```
x = 1797321ba57f9d58ab3bbaaad0d857748c4fbde6d16447c5b785e16c9a2e69ad30f596b35810499e9b301700ed8d722b5352a867e48283eedfd879ab397bbb36182f38675bb2aa83973c0ea3c2773da576813a004661d3e5db4e03e9a90b4d76693f0daae2730394e7f1977e2587ca71e700c85fcba1c888c128e02fcd23f7dba
n = 8656b782764c0b446ab555e4f1b0a0866f2038f4aaaa26c33f83897805fb1290b762c830ecff842e504e202c3625695768612add7dfee92cb2faaa6e0906d9da0b5c4d5815fd4e2d73b648154f0728c644e2d1fcec8d4bea953e49ad89d2f21d0d240f191a229daeb2c10534542c74f50d1fbb09db7bd4085a36a7870c726219576029c53b9471ffee5f9ab51a713c7a7e44c9a9eee60abcbfdb4461aff4e94c77b0f243f3455b853a32ca0d819c66aef6907c479c127b465b8fbfc77030dc0e59e4c676def55f9787df04c9594bfee6286d4d8c395db30884133693c3ea56e7b4e35709d4e1e65c7ee75fc794025cd8929217f1ae3c4f4a191a7b858cf3f125
c = 7d0c64c4986103c28dcaae49cd3c1c2bdb90b6135b9d6fe01c1dac0d3142548a84594563dd0e598ba2b825ab3fda3f1693a90e7ba807d5e173591a0041fa81857218c7e0be53603e1fa3cb37adae607d91475d31644ff04fdc23150da8d2232d14384fb22ce466e94adf3a47236f9e12a9bf154078ca023a9221a437be01ef6db0c64d5ae3e60cca368b511c327b6c99a8ddde44877d6319127d6fffd0e42da4940eb245babd3af0eb1266ce0b2bb9fce12b30cb2c2bc51bc7e3d7f3927c0fcb870b342af788633226073d33f8355fd27d5f8b46bd38e811608fd9aa155421815707a46f142c95302bf29c82bbdb3fb54bf42d8683581e35d54fd2c487acf03
e = 65537

```

Since `x` the sum of `p` and `q` is known it's easy to calculate `phi(n)` (Euler's totient function) which is used to get the private key part `d`.  
In RSA `d` is the modular inverse of `e mod phi(n)` (or Carmichael's totient instead of Euler's). 

```
phi(n) = (p-1)(q-1)
       = p*q - (p+q) + 1
       = n - x + 1
```


```python
phi_n = n - x + 1
d = pow(e,-1,phi_n)
plaintext = pow(c,d,n)
print(plaintext.to_bytes(((plaintext.bit_length() + 7) //8), "big"))
```

flag: `picoCTF{pl33z_n0_g1v3_c0ngru3nc3_0f_5qu4r35_3921def5}`
