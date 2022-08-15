import os
import subprocess
from urllib.request import urlopen

if os.getuid():
    raise SystemExit("This script requires root to run. If you don't feel safe with that (as you should), feel free to first inspect the script at 'https://github.com/kevinshome/unixstamp', or manually install UNIXstamp yourself.")

if os.name != 'posix':
    raise SystemExit("Sorry, but this script only works on Linux, MacOS, and other UNIX-like systems at the moment.")

print("\033[1;37mInstalling dependency 'Pillow' via pip...")
subprocess.Popen(["pip", "install", "-U", "Pillow"])
print("\033[1;37mInstalling xkcd script to /usr/local/bin...")
os.chdir("/usr/local/bin")
res = urlopen("https://raw.githubusercontent.com/nhtnr/xkcd/main/xkcd")
with open("/usr/local/bin/xkcd", 'wb') as f:
    f.write(res.read())
os.chmod("/usr/local/bin/xkcd", 0o555)
print("Xkcd has been installed successfully!\nTo test it out, run: 'xkcd latest'.")