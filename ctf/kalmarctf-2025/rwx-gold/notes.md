# Setup for gold

Same setup as the previous challenges but we only get *3* chars for the command.
Look around the container to see which commands are available. Eventually find
the `photo-viewer` option for `gpg` which allows to specify a command that is
used to view the image that is associated with a key.

try/except and setting a timeout for the request is necessary since `gpg` hangs
if it is called without any arguments.

