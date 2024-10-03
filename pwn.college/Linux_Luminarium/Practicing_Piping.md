# Practicing Piping
## Redirecting output
- ran `echo PWN > COLLEGE` in the terminal to write the text `PWN` to the file `COLLEGE` and got the flag
## Redirecting more output
- ran `/challenge/run > myflag` in the terminal to run the command and redirect the output to the file `myflag` 
- ran `cat myflag` in the terminal and got the flag
## Appending output
- ran `/challenge/run >> /home/hacker/the-flag` in the terminal to run the command and append the stdout to the file `the-flag`
- ran `cat /home/hacker/the-flag` in the terminal and got the flag
## Redirecting errors
- ran `/challenge/run > myflag 2> instructions` in the terminal to run the command and redirect the stdout to the file `myflag` and stderr to the file `instructions`
- ran `cat instructions` in the terminal to read the feedback and check whether the previous command was successful
- ran `cat myflag` in the terminal and got the flag
## Redirecting input
- ran `echo COLLEGE > PWN` in the terminal to write the text `COLLEGE` to the file `PWN`
- ran `/challenge/run < PWN` in the terminal to run the command and redirect the input from the file `PWN` and got the flag
## Grepping stored results
- ran `/challenge/run > /tmp/data.txt` in the terminal to run the command and store the output in the file `data.txt`
- ran `cat /tmp/data.txt | grep pwn.college` in the terminal to search for the string `pwn.college` in the stored output and got the flag
## Grepping live output
- ran `/challenge/run | grep pwn.college` in the terminal to run the command and filter the output for the string `pwn.college` and got the flag
## Grepping errors
- ran `/challenge/run 2>& 1 | grep pwn.college` in the terminal to run the command and redirect the stderr to stdout and filter the output for the string `pwn.college` and got the flag
## Duplicating piped data with tee
- ran `/challenge/pwn | tee pwn_output | /challenge/college` in the terminal to run the command and intercept the output with `tee` and pass it to the next command
- ran `cat pwn_output` in the terminal to read the output of the first command:
```
Usage: /challenge/pwn --secret [SECRET_ARG]

SECRET_ARG should be "EuAfFCVe"
```
- ran `/challenge/pwn --secret EuAfFCVe | /challenge/college` in the terminal and got the flag
## Writing to multiple programs
- ran `/challenge/hack | tee >(/challenge/the) >(/challenge/planet)` in the terminal to run the command and pass the output to two different programs using `tee` and process substitution and got the flag
## Split-piping stderr and stdout
- ran `/challenge/hack 2> >(/challenge/the) > >(/challenge/planet)` in the terminal to run the command and split the stderr and stdout to two different programs using process substitution and got the flag