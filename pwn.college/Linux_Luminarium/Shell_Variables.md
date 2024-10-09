# Shell Variables
## Printing Variables
- ran `echo $FLAG` in the terminal to print the value of the variable `FLAG` and got the flag: `pwn.college{87buZZ0wH393DjwxjhbpkIkQ78o.ddTN1QDL5QTO0czW}`
## Setting Variables
- ran `PWN=COLLEGE` in the terminal to set the variable `PWN` to the value `COLLEGE` and got the flag: `pwn.college{YYyAH6IauQ-dXg_YH4NUTXBdNrk.dlTN1QDL5QTO0czW}`
## Multi-word Variables
- ran `PWN="COLLEGE YEAH"` in the terminal to set the variable `PWN` to the value `COLLEGE YEAH` and got the flag: `pwn.college{gQTkbFmDnxVQAaiQDU66ddfjNuU.dBjN1QDL5QTO0czW}`
## Exporting Variables
- ran `export PWN=COLLEGE` in the terminal to set the variable `PWN` to the value `COLLEGE` and make it available to child processes
- ran `COLLEGE=PWN` in the terminal to set the variable `COLLEGE` to the value `PWN`
- ran `/challenge/run` in the terminal to run the command and got the flag: `pwn.college{4SPBSznQYO4sC7GnGE76u2_9csZ.dJjN1QDL5QTO0czW}`
## Printing Exported Variables
- ran `env` in the terminal to print the environment variables and looked through the output to find the `FLAG` variable: `pwn.college{4RrjJ2rinsxIHv6WXJAQ_H2BVQV.dhTN1QDL5QTO0czW}`
## Storing Command Output
- ran `PWN=$(/challenge/run)` in the terminal to store the output of the command in the variable `PWN`
- ran `echo $PWN` in the terminal to print the value of the variable `PWN` and got the flag: `pwn.college{QW-BOnhXp02VmAFRIHYHY3cUDkG.dVzN0UDL5QTO0czW}`
## Reading Input
- ran `read PWN` in the terminal to read the input from the user and store it in the variable `PWN`
- entered `COLLEGE` in the terminal and got the flag: `pwn.college{UUay7zAEb9wF5HaEYUOSYarsrzH.dhzN1QDL5QTO0czW}`
## Reading Files
- ran `read PWN < /challenge/read_me` in the terminal to read the content of the file `read_me` and store it in the variable `PWN` and got the flag: `pwn.college{4me72AFrzYpbtJXwApugH8YHW45.dBjM4QDL5QTO0czW}`