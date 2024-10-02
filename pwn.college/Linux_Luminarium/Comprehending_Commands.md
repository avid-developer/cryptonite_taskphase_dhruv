# Comprehending Commands
## cat: not the pet, but the command!
- ran `cat flag` in the terminal and got the flag
## catting absolute paths
- ran `cat /flag` in the terminal and got the flag
## more catting practice
- ran `cat /lib/jvm/java-11-openjdk-amd64/flag` in the terminal and got the flag
## grepping for a needle in a haystack
- ran `grep pwn.college /challenge/data.txt` in the terminal and got the flag
## listing files
- ran `ls /challenge` in the terminal to find the random name of the flag file
- it turned out to be `24065-renamed-run-7433` so I ran `/challenge/24065-renamed-run-7433` in the terminal and got the flag
## touching files
- ran `touch /tmp/pwn /tmp/college` in the terminal to create the files `pwn` and `college` in the `/tmp` directory
- ran `/challenge/run` in the terminal and got the flag
## removing files
- ran `rm delete_me` in the terminal to remove the file `delete_me` in the current directory
- ran `/challenge/check` in the terminal and got the flag
## hidden files
- ran `cd /` in the terminal to change the directory to `/`
- ran `ls -a` in the terminal to list all files in the directory, including hidden files
- found the hidden file `.flag-26348490621874` and ran `cat .flag-26348490621874` in the terminal to get the flag
## An Epic Filesystem Quest
- ran `cd /` in the terminal to change the directory to `/`
- ran `ls` in the terminal to list all files in the directory
- found the file `WHISPER` and ran `cat WHISPER` in the terminal to get the next clue:
> The next clue is in: /usr/lib/python3/dist-packages/sympy/calculus/\_\_pycache__

> Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
- ran `ls /usr/lib/python3/dist-packages/sympy/calculus/__pycache__` in the terminal to list all files in the directory
- found the file `CUE-TRAPPED` and ran `cat /usr/lib/python3/dist-packages/sympy/calculus/__pycache__/CUE-TRAPPED` in the terminal to get the next clue:
> Lucky listing!
> The next clue is in: /opt/ghidra/Ghidra/Processors/TI_MSP430/data/manuals
- ran `ls /opt/ghidra/Ghidra/Processors/TI_MSP430/data/manuals` in the terminal to list all files in the directory
- found the file `INSIGHT` and ran `cat /opt/ghidra/Ghidra/Processors/TI_MSP430/data/manuals/INSIGHT` in the terminal to get the next clue:
> Yahaha, you found me!
> The next clue is in: /usr/share/icons/ubuntu-mono-light/animations

> The next clue is **delayed** --- it will not become readable until you enter the directory with 'cd'.
- ran `cd /usr/share/icons/ubuntu-mono-light/animations` in the terminal to change the directory to `/usr/share/icons/ubuntu-mono-light/animations`
- ran `ls` in the terminal to list all files in the directory
- found the file `NOTE` and ran `cat NOTE` in the terminal to get the next clue:
> Tubular find!
> The next clue is in: /opt/linux/linux-5.4/drivers/gpu/drm/nouveau/nvkm/subdev/top

> The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
- ran `ls -a /opt/linux/linux-5.4/drivers/gpu/drm/nouveau/nvkm/subdev/top` in the terminal to list all files in the directory, including hidden files
- found the hidden file `.DOSSIER` and ran `cat /opt/linux/linux-5.4/drivers/gpu/drm/nouveau/nvkm/subdev/top/.DOSSIER` in the terminal to get the next clue:
> Yahaha, you found me!
> The next clue is in: /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Normal
- ran `ls /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Normal` in the terminal to list all files in the directory
- found the file `MEMO` and ran `cat /usr/share/javascript/mathjax/jax/output/SVG/fonts/STIX-Web/Normal/MEMO` in the terminal to get the next clue:
> Yahaha, you found me!
> The next clue is in: /usr/share/javascript/mathjax/unpacked/jax/output/HTML-CSS/fonts/STIX-Web/Size5/Regular

> Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
- ran `ls /usr/share/javascript/mathjax/unpacked/jax/output/HTML-CSS/fonts/STIX-Web/Size5/Regular` in the terminal to list all files in the directory
- found the file `SECRET-TRAPPED` and ran `cat /usr/share/javascript/mathjax/unpacked/jax/output/HTML-CSS/fonts/STIX-Web/Size5/Regular/SECRET-TRAPPED` in the terminal to get the next clue:
> Tubular find!
> The next clue is in: /opt/linux/linux-5.4/drivers/i2c/busses

> The next clue is **hidden** --- its filename starts with a '.' character. You'll need to look for it using special options to 'ls'.
- ran `ls -a /opt/linux/linux-5.4/drivers/i2c/busses` in the terminal to list all files in the directory, including hidden files
- found the hidden file `.MESSAGE` and ran `cat /opt/linux/linux-5.4/drivers/i2c/busses/.MESSAGE` in the terminal to get the next clue:
> The next clue is in: /usr/local/lib/python3.8/dist-packages/tornado-6.4.1.dist-info

> Watch out! The next clue is **trapped**. You'll need to read it out without 'cd'ing into the directory; otherwise, the clue will self destruct!
- ran `ls /usr/local/lib/python3.8/dist-packages/tornado-6.4.1.dist-info` in the terminal to list all files in the directory
- found the file `HINT-TRAPPED` and ran `cat /usr/local/lib/python3.8/dist-packages/tornado-6.4.1.dist-info/HINT-TRAPPED` in the terminal to finally get the flag
## making directories
- ran `mkdir /tmp/pwn` in the terminal to create the directory `pwn` in the `/tmp` directory
- ran `touch /tmp/pwn/college` in the terminal to create the file `college` in the `/tmp/pwn` directory
- ran `/challenge/run` in the terminal and got the flag
## finding files
- ran `find / -name flag` in the terminal to find the file named `flag` in the filesystem
- this returned several results, so I used `cat` to check each one until I found the flag in `/opt/aflplusplus/nyx_mode/QEMU-Nyx/bsd-user/sparc/flag`
## linking files
- ran `ln -s /flag /home/hacker/not-the-flag` in the terminal to create a symbolic link to the flag in the `/home/hacker` directory
- ran `/challenge/catflag` in the terminal and got the flag