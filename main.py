# requires Python 3.x
from  collections import namedtuple
from tqdm import tqdm
import requests
import os
import sys
import shutil

def get_int(prompt, lo=None, hi=None):
    while True:
        try:
            val = int(input(prompt))
            if (lo is None or lo <= val) and (hi is None or val <= hi):
                return val
        except ValueError:   # input string could not be converted to int
            pass
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



def do_menu(options):
    print("Welcome to Garuda Linux Installer")
    print("Choose your distro")
    for num,option in enumerate(options, 1):
        print("{num}: {label}".format(num=num, label=option.label))
    prompt = "Please enter the number of your choice (1-{max}): ".format(max=len(options))
    choice = get_int(prompt, 1, len(options)) - 1
    options[choice].fn()    # call the requested function

def gaurda_kde():
    print("\nInstalling Garuda KDE Dr460nized")
    chunk_size = 1024

    url = "https://sourceforge.net/projects/garuda-linux/files/garuda/dr460nized/220131/"

    r = requests.get(url, stream=True)

    total_size = int(r.headers['content-length'])
    filename = url.split('/')[-1]

    with open(filename, 'wb') as f:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
            f.write(data)
    print("Download complete!")
    os.system('chmod +x mover.sh')
    os.system('./mover.sh')

def garuda_gnome():
    print("\n Installing Garuda Linux GNOME")
    chunk_size = 1024

    url = "https://sourceforge.net/projects/garuda-linux/files/garuda/gnome/220131/garuda-gnome-linux-zen-220131.iso"

    r = requests.get(url, stream=True)

    total_size = int(r.headers['content-length'])
    filename = url.split('/')[-1]

    with open(filename, 'wb') as f:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
            f.write(data)
    print("Download complete!")
    os.system('chmod +x mover.sh')
    os.system('./mover.sh')


def garuda_xfce():
    print("\n Installing Garuda Xfce")
    chunk_size = 1024

    url = "https://sourceforge.net/projects/garuda-linux/files/garuda/xfce/220131/garuda-xfce-linux-lts-220131.iso"

    r = requests.get(url, stream=True)

    total_size = int(r.headers['content-length'])
    filename = url.split('/')[-1]

    with open(filename, 'wb') as f:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
            f.write(data)
    print("Download complete!")
    os.system('chmod +x mover.sh')
    os.system('./mover.sh')

def garuda_lxqt():
    print("\n Installing Garuda LXQT-Kwin")
    
    chunk_size = 1024

    url = "https://sourceforge.net/projects/garuda-linux/files/garuda/lxqt-kwin/220131/garuda-lxqt-kwin-linux-zen-220131.iso"

    r = requests.get(url, stream=True)

    total_size = int(r.headers['content-length'])
    filename = url.split('/')[-1]

    with open(filename, 'wb') as f:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
            f.write(data)
    print("Download complete!")
    os.system('chmod +x mover.sh')
    os.system('./mover.sh')

def garuda_sway():
    print("\n Installing Garuda Sway")
 
    chunk_size = 1024

    url = "https://sourceforge.net/projects/garuda-linux/files/garuda/sway/220131/garuda-sway-linux-zen-220131.iso"

    r = requests.get(url, stream=True)

    total_size = int(r.headers['content-length'])
    filename = url.split('/')[-1]

    with open(filename, 'wb') as f:
        for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
            f.write(data)
    print("Download complete!")
    os.system('chmod +x mover.sh')
    os.system('./mover.sh')  

def garuda_qtile():
        print("\n Installing Garuda Qtile")
 
        chunk_size = 1024

        url = "https://sourceforge.net/projects/garuda-linux/files/garuda/qtile/220131/garuda-qtile-linux-zen-220131.iso"

        r = requests.get(url, stream=True)

        total_size = int(r.headers['content-length'])
        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
                        f.write(data)
        print("Download complete!")
        os.system('chmod +x mover.sh')
        os.system('./mover.sh')  
  
def garuda_i3wm():
        print("\n Installing Garuda i3WM")
 
        chunk_size = 1024

        url = "https://sourceforge.net/projects/garuda-linux/files/garuda/i3/220131/garuda-i3-linux-zen-220131.iso"

        r = requests.get(url, stream=True)

        total_size = int(r.headers['content-length'])
        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
                        f.write(data)
        print("Download complete!")
        os.system('chmod +x mover.sh')
        os.system('./mover.sh')  

def garuda_bspwm():
        print("\n Installing Garuda BSPWM")
 
        chunk_size = 1024

        url = "https://sourceforge.net/projects/garuda-linux/files/garuda/bspwm/220131/garuda-bspwm-linux-zen-220131.iso"

        r = requests.get(url, stream=True)

        total_size = int(r.headers['content-length'])
        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
                        f.write(data)
        print("Download complete!")
        os.system('chmod +x mover.sh')
        os.system('./mover.sh')

def garuda_mate():
        print("\n Installing Garuda Mate")
 
        chunk_size = 1024

        url = "https://sourceforge.net/projects/garuda-linux/files/community/mate/220131/garuda-mate-linux-zen-220131.iso"

        r = requests.get(url, stream=True)

        total_size = int(r.headers['content-length'])
        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
                        f.write(data)
        print("Download complete!")
        os.system('chmod +x mover.sh')
        os.system('./mover.sh')

def garuda_cinnamon():
        print("\n Installing Garuda Cinnamon")
 
        chunk_size = 1024

        url = "https://sourceforge.net/projects/garuda-linux/files/community/cinnamon/220131/garuda-cinnamon-linux-zen-220131.iso"

        r = requests.get(url, stream=True)

        total_size = int(r.headers['content-length'])
        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
                        f.write(data)
        print("Download complete!")
        os.system('chmod +x mover.sh')
        os.system('./mover.sh')
    
def garuda_barebone():
        print("\n Installing Garuda Barebone")
 
        chunk_size = 1024

        url = "https://sourceforge.net/projects/garuda-linux/files/garuda/kde-barebones/220131/garuda-kde-barebones-linux-lts-220131.iso"

        r = requests.get(url, stream=True)

        total_size = int(r.headers['content-length'])
        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
                        f.write(data)
        print("Download complete!")
        os.system('chmod +x mover.sh')
        os.system('./mover.sh')

def garuda_kdegit():
        print("\n Installing Garuda Kde-Git")
 
        chunk_size = 1024

        url = "https://mirrors.fossho.st/garuda/iso/community/kde-git/220101/garuda-kde-git-linux-zen-220101.iso"

        r = requests.get(url, stream=True)

        total_size = int(r.headers['content-length'])
        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='MB'):
                        f.write(data)
        print("Download complete!")
        os.system('chmod +x mover.sh')
        os.system('./mover.sh')

Option = namedtuple("Option", ["label", "fn"])
options = [
    Option("Garuda KDE Dr460nized ", gaurda_kde),
    Option("Garuda Linux GNOME", garuda_gnome),
    Option("Garuda Xfce", garuda_xfce),
    Option("Garuda LXQT-Kwin", garuda_lxqt),
    Option("Garuda Sway", garuda_sway),
    Option("Garuda Qtile", garuda_qtile),
    Option("Garuda i3WM", garuda_i3wm),
    Option("Garuda BSPWM", garuda_bspwm),
    Option("Garuda Mate", garuda_mate),
    Option("Garuda Cinnamon", garuda_cinnamon),
    Option("Garuda Linux Barebones", garuda_barebone),
    Option("Garuda Linux KDE-Git", garuda_kdegit)
]

def main():
    clearConsole()
    num = get_int("Please enter the number of iterations: ")
    for i in range(num):
        clearConsole()
        do_menu(options)

if __name__=="__main__":
    main()
