# Setup for silver

The same setup as `bronze` but we only get a command of length **5** or less.

We can use the same code but need to get rid of 1 char since the command used
in bronze was 6 characters. Instead of using `sh` we can use `source` which has
a short form `.`.

