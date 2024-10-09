# Chaining Commands
## Chaining with Semicolons
- ran `/challenge/pwn; /challenge/college` in the terminal to run the commands sequentially and got the flag: `pwn.college{0blMw6jRO_MXNX1zGgL1G4fdno7.dVTN4QDL5QTO0czW}`
## Your First Shell Script
- opened the VSCode Workspace and created a new file `x.sh`
- added the following content to the file:
```
/challenge/pwn
/challenge/college
```
- saved the file and ran `bash x.sh` in the terminal to execute the script and got the flag: `pwn.college{MzKreBQGHvvBheH7CqqIGkqr8Vm.dFzN4QDL5QTO0czW}`
## Redirecting Script Output
- ran `bash x.sh | /challenge/solve` in the terminal to execute the script and pass the output to the command `solve` and got the flag: `pwn.college{8McwB5IvrBIIArw0fLEivFZUm8-.dhTM5QDL5QTO0czW}`
## Executable Shell Scripts
- opened the VSCode Workspace and opened the file `x.sh`
- modified the file to have the following content:  
`/challenge/solve`
- saved the file and ran `chmod a+x x.sh` in the terminal to make the script executable
- ran `./x.sh` in the terminal to execute the script and got the flag: `pwn.college{Eodl5kDWh3M9lJvnZQ0IPcbtsTI.dRzNyUDL5QTO0czW}`