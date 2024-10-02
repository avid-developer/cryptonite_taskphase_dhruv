# Digesting Documentation
## Learning From Documentation
- ran `/challenge/challenge --giveflag` in the terminal and got the flag
## Learning Complex Usage
- ran `/challenge/challenge --printfile /flag` in the terminal and got the flag
## Reading Manuals
- ran `man challenge` in the terminal to read the manual of the `challenge` command
- found the following information in the `SYNOPSIS` and `DESCRIPTION` section:
> SYNOPSIS  
challenge OPTION

> DESCRIPTION  
--ighsvp NUM  
print the flag if NUM is 653
- ran `/challenge/challenge --ighsvp 653` in the terminal and got the flag
## Searching Manuals
- ran `man challenge` in the terminal to read the manual of the `challenge` command
- used `/` to search for `flag` in the manual
- found the following information in the `DESCRIPTION` section:
> --udjw This argument will give you the flag!
- used `q` to exit the manual
- ran `/challenge/challenge --udjw` in the terminal and got the flag
## Searching For Manuals
- ran `man man` in the terminal to read the manual of the `man` command
- used `/` to search for `search` in the manual
- used `n` to find the next occurrences of `search` in the manual until i found the following result: 
> ...skipping  
Search for text in all manual pages.  This is a  brute-force  search,  and  is
likely  to  take some time; if you can, you should specify a section to reduce
the number of pages that need to be searched.   Search  terms  may  be  simple
strings (the default), or regular expressions if the --regex option is used.

> Note  that  this  searches  the  <u>sources</u> of the manual pages, not the rendered
text, and so may include false positives due to things like comments in source
files.  Searching the rendered text would be much slower.
- i realised that i needed to access just the previous line in the manual to get the command to search for text in all manual pages
- used `h` to access the help section of the manual
- found the commands `b` and `ctrl-B` which would help me to go back a screenful of text in the manual
- tried using `b` and `ctrl-B` to go back a screenful of text in the manual but it didn't work
- used `q` to exit the manual
- discussed with an LLM regarding my issue and after a bit of back and forth, i was able to resolve the issue by using `export MANPAGER='less'` to set the `less` command as the pager for the `man` command instead of the default `more` command
- ran `man man` in the terminal to read the manual of the `man` command
- used `/` to search for `search` in the manual
- used `n` to find the next occurrences of `search` in the manual
- since my pager for the `man` command was now set to `less`, i was able to scroll up and down in the manual using the arrow keys
- so i scrolled up in the manual after finding the `brute-force search` section and found the following command:
> -K, --global-apropos  
Search for text in all manual pages.  This is a  brute-force  search,...
- used `q` to exit the manual
- ran `man -K /challenge/challenge` in the terminal to search for the `challenge` command in all manual pages
- found the following information in the `DESCRIPTION` and `SYNOPIS` section of the `krdnzoqruz` manual:
> SYNOPSIS  
challenge OPTION

> DESCRIPTION  
Output the flag when called with the right arguments.

> --krdnzo NUM  
print the flag if NUM is 724
- ran `/challenge/challenge --krdnzo 724` in the terminal and got the flag
## Helpful Programs
- ran `/challenge/challenge --help` in the terminal to get help on the `challenge` command
- i found the following information under the `optional arguments` section:
```
-h, --help            show this help message and exit
  --fortune             read your fortune
  -v, --version         get the version number
  -g GIVE_THE_FLAG, --give-the-flag GIVE_THE_FLAG
                        get the flag, if given the correct value
  -p, --print-value     print the value that will cause the -g option to give you the flag
```

- ran `/challenge/challenge -p` in the terminal to print the value that will cause the `-g` option to give me the flag. It gave me the value `86`
- ran `/challenge/challenge -g 86` in the terminal and got the flag
## Help for Builtins
- ran `help challenge` in the terminal to get help on the `challenge` builtin command. Found the following information:
```
...
This builtin command will read you the flag, given the right arguments!
    
    Options:
      --fortune         display a fortune
      --version         display the version
      --secret VALUE    prints the flag, if VALUE is correct

    You must be sure to provide the right value to --secret. That value
    is "gRJS27zG".
```
- ran `/challenge/challenge --secret gRJS27zG` in the terminal and got the flag