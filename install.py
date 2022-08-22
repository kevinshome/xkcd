import os
import sys
import subprocess

requires_dist = []
pass_xkcd_installed_checker = False
xkcd_installed = False

if sys.argv[1] == "--install-db":
    pip_list_proc = subprocess.Popen("pip3 list 2>&1 | awk '/xkcd-comicdb/' | grep . >/dev/null 2>&1", shell=True)
    if pip_list_proc.wait() != 0:
        requires_dist.append("xkcd-comicdb")
        pass_xkcd_installed_checker = True
    else:
        print("'xkcd-comicdb' already installed. Ignoring '--install-db' flag...")

if os.path.exists("/usr/local/bin/xkcd") and not pass_xkcd_installed_checker:
    print("\033[1;31mxkcd already installed. Aborting...", file=sys.stderr)
    raise SystemExit(1)
elif os.path.exists("/usr/local/bin/xkcd") and pass_xkcd_installed_checker:
    xkcd_installed = True

if os.name != 'posix':
    raise SystemExit("Sorry, but this script only works on Linux, MacOS, and other UNIX-like systems at the moment.")

# check to see if Pillow is installed
pip_list_proc = subprocess.Popen("pip3 list 2>&1 | awk '/Pillow/' | grep . >/dev/null 2>&1", shell=True)
if pip_list_proc.wait() != 0:
    requires_dist.append("Pillow")

for package in requires_dist:
    print(f"\033[1;37mInstalling dependency '{package}' via pip...")
    pip_proc = subprocess.Popen(["pip3", "install", "-U", package])
    if pip_proc.wait() != 0:
        print(f"\033[1;31mAn error occurred in pip, unable to install {package}", file=sys.stderr)
        raise SystemExit(1)

if xkcd_installed:
    raise SystemExit(0)

print(f"\033[1;37mInstalling xkcd script to /usr/local/bin/xkcd...")
curl_proc = subprocess.Popen("sudo curl -fsSL https://raw.githubusercontent.com/nhtnr/xkcd/main/xkcd > /usr/local/bin/xkcd", shell=True)
if curl_proc.wait() != 0:
    print("\033[1;31mAn error occurred in curl, unable to install xkcd", file=sys.stderr)
    raise SystemExit(1)
chmod_proc = subprocess.Popen(["sudo", "chmod", "555", "/usr/local/bin/xkcd"])
if chmod_proc.wait() != 0:
    print("\033[1;31mAn error occurred in chmod, unable to change file permissions.\nThis can be done manually, however, by running \"sudo chmod 555 /usr/local/bin/xkcd\"", file=sys.stderr)
    raise SystemExit(1)
print("Xkcd has been installed successfully!\nTo test it out, run: 'xkcd latest'.")