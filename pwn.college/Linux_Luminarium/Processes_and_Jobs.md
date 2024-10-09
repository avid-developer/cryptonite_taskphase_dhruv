# Processes and Jobs
## Listing Processes
- ran `ps -ef` in the terminal to list all processes and their details
- saw the process `/challenge/29105-run-14038` running, so ran `/challenge/29105-run-14038` in the terminal and got the flag: `pwn.college{w2e9Ir2z-cRuOLmp8mq0YZYkGG7.dhzM4QDL5QTO0czW}`
## Killing Processes
- ran `ps -ef` in the terminal to list all processes and their details
- found the process `/challenge/dont_run` running, so noted it's PID (73)
- ran `kill 73` in the terminal to kill the process
- ran `/challenge/run` in the terminal and got the flag: `pwn.college{UOe_cMAOKF53HRwUUExPXC2Dxk2.dJDN4QDL5QTO0czW}`
## Interrupting Processes
- ran `/challenge/run` in the terminal and then hit `Ctrl+C` to interrupt the process and got the flag: `pwn.college{gQBiJo9arX_QK4XxLrkSXiL1Qhu.dNDN4QDL5QTO0czW}`
## Suspending Processes
- ran `/challenge/run` in the terminal and then hit `Ctrl+Z` to suspend the process
- ran `/challenge/run` in the terminal again to launch another copy of the process while the first one was suspended and got the flag: `pwn.college{0zLNrPjaoho6WptuSVjxHPbxehh.dVDN4QDL5QTO0czW}`
## Resuming Processes
- ran `/challenge/run` in the terminal and then hit `Ctrl+Z` to suspend the process
- ran `fg` in the terminal to resume the suspended process and got the flag: `pwn.college{A-CjuK-ui_VdekMgA0PEzWq-K7A.dZDN4QDL5QTO0czW}`
## Backgrounding Processes
- ran `/challenge/run` in the terminal and then hit `Ctrl+Z` to suspend the process
- ran `bg` in the terminal to background the suspended process
- ran `/challenge/run` in the terminal again to launch another copy of the process while the first one was running in the background and got the flag: `pwn.college{kqUHfK6UwhLbV4tXIbFCU1lHmAk.ddDN4QDL5QTO0czW}`
## Foregrounding Processes
- ran `/challenge/run` in the terminal and got the following output:  
`To pass this level, you need to suspend me, resume the suspended process in the 
background, and *then* foreground it without re-suspending it! You can 
background me with Ctrl-Z (and resume me in the background with 'bg') or, if 
you're not ready to do that for whatever reason, just hit Enter and I'll exit!`
- hit `Ctrl+Z` to suspend the process
- ran `bg` in the terminal to background the suspended process and got the following output:  
`Yay, I'm now running the background! Because of that, this text will probably 
overlap weirdly with the shell prompt. Don't panic; just hit Enter a few times 
to scroll this text out. After that, resume me into the foreground with 'fg'; 
I'll wait.`
- ran `fg` in the terminal to foreground the process and got the following output:  
`YES! Great job! I'm now running in the foreground. Hit Enter for your flag!`
- hit `Enter` in the terminal and got the flag: `pwn.college{oXRVebFFUby4h3X0glnsgLIN-Y4.dhDN4QDL5QTO0czW}`
## Starting Backgrounded Processes
- ran `/challenge/run &` in the terminal to start the process in the background and got the flag: `pwn.college{4OBOJSOMHr7SQudXNXEBVruc6HM.dlDN4QDL5QTO0czW}`
## Process Exit Codes
- ran `/challenge/get-code` in the terminal to get the exit error code of the process
- ran `/challenge/submit-code $?` in the terminal to submit the exit error code and got the flag: `pwn.college{cRpHqZJU-Emh3eP7nTviaXYCzFi.dljN4UDL5QTO0czW}`