# Pondering PATH
## The PATH Variable
- ran `PATH=""` in the terminal to set the `PATH` variable to an empty string
- ran `/challenge/run` in the terminal to run the command and got the flag: `pwn.college{Ibwncn81eQiCDC2sj7YUoJCs67M.dZzNwUDL5QTO0czW}`
## Setting PATH
- ran `PATH=/challenge/more_commands` in the terminal to set the `PATH` variable to the directory `/challenge/more_commands`
- ran `/challenge/run` in the terminal to run the command and got the flag: `pwn.college{YLehYvj4mhCiD7nUWxjMABozJ1k.dVzNyUDL5QTO0czW}`
## Adding Commands
- opened the VSCode Workspace and created a new file `win`
- added the following content to the file:  
`cat /flag`
- saved the file and ran `chmod a+x win` in the terminal to make the script executable
- ran `export PATH=$PATH:/home/hacker` in the terminal to add the directory `/home/hacker` to the `PATH` variable
- ran `/challenge/run` in the terminal to run the command and got the flag: `pwn.college{cTJFeRrBMRb7Wofbs-u1IevTcPb.dZzNyUDL5QTO0czW}`
## Hijacking Commands
- this challenge was somewhat tricky but quite fun, brainstormed a bit with SENSAI and figured out the solution
- opened the VSCode Workspace and created a new file `rm`
- added the following content to the file:  
`cat /flag`
- saved the file and ran `chmod a+x rm` in the terminal to make the script executable
- ran `PATH="~:$PATH"` in the terminal to set the `PATH` variable to `~:$PATH` (add `/home/hacker` to the beginning of the `PATH` so that the `rm` script which we created will be executed instead of the system `rm` command)
- ran `/challenge/run` in the terminal to run the command and got the flag: `pwn.college{kWkuT1hQUzmCUoEeJzYBjx0gOpD.ddzNyUDL5QTO0czW}`