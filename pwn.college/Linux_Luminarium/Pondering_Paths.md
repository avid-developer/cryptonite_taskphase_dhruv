# Pondering Paths
## The Root
- ran `/pwn` in the terminal and got the flag
## Program and absolute paths
- ran `/challenge/run` in the terminal and got the flag
## Position thy self
- ran `/challenge/run` in the terminal and got prompted to `cd` into the `/var/log` directory
- ran `cd /var/log` in the terminal to change the directory to `/var/log`
- ran `/challenge/run` in the terminal and got the flag
## Position elsewhere
- ran `/challenge/run` in the terminal and got prompted to `cd` into the `/etc/apt/sources.list.d` directory
- ran `cd /etc/apt/sources.list.d` in the terminal to change the directory to `/etc/apt/sources.list.d`
- ran `/challenge/run` in the terminal and got the flag
## Position yet elsewhere
- ran `/challenge/run` in the terminal and got prompted to `cd` into the `/tmp` directory
- ran `cd /tmp` in the terminal to change the directory to `/tmp`
- ran `/challenge/run` in the terminal and got the flag
## implicit relative paths, from /
- ran `cd /` in the terminal to change the directory to `/`
- ran `challenge/run` in the terminal and got the flag
## explicit relative paths, from /
- ran `/challenge/run` in the terminal and got prompted to `cd` into the `/` directory
- ran `cd /` in the terminal to change the directory to `/`
- ran `./challenge/run` in the terminal and got the flag
## implicit relative path
- ran `cd /challenge` in the terminal to change the directory to `/challenge`
- ran `./run` in the terminal and got the flag
## home sweet home
- ran `/challenge/run ~/f` in the terminal and got the flag