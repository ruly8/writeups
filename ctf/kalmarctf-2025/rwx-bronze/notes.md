# Setup

We have access to 3 endpoints, `write`,`read` and `exec`. All 3 do what you would
think they do. We can write and read files (limited by user permissions) and
execute commands. Though the command has to be **7** characters or less.
We need to execute `/would you be so kind to provide me with a flag` to read
the flag, thats obviously more than 7 chars.

The idea is to write this command into a file that we can then execute with the
`exec` endpoint.

payload would look like this:

```
/would you be so kind to provide me with a flag > /home/user/flag
```

So we write to `/home/user/x`, execute `sh ~/x` and read the output file.
