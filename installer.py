print("Welcome To Garuda Linux ISO Downloader!")
print("It is a simple programs (which everyone can make) in python")
print("Made By Ender4Lion")
print("Please follow this project on github. It would really help me!")
print("Installing Garuda Dr460nized!")

import wget

a = "url"
b = "https://sourceforge.net/projects/garuda-linux/files/garuda/dr460nized/220131/garuda-dr460nized-linux-zen-220131.iso/download"
a = b

wget.download(a, 'garuda-dr460nized-linux-zen-220131.iso');


print("Installer Finished!")

