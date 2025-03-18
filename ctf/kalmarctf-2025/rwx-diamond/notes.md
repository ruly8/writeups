# Setup for diamond

Did not solve this challenge during the competition but saw people talking 
about `w|sh` on discord after the event ended.
The setup for this one is slightly different. We get *4* chars for the command
but the user does not get a home directory.

The idea is to execute `w|sh` and write the payload to `/proc/{pid}/fd/0` (stdin)
of the `sh` process. A race condition.

We can use `ps` to get the currently highest process id and use it as base for
the newly created processes during the race.

The solve script goes through ~100 pids to hit the correct order/timing when both 
`pid+4` and `pid+5` are part of the pool. I'm sure one can do it in less 
requests with a different approach or more fine-grained timing.


