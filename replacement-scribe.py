# import only system from os
from os import system, name, remove, path


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def overwrite():
    if path.exists("codes"):
        remove("codes")
    newfile = open("codes", "x+t")
    for k, v in dtb.items():
        newfile.write(str(k) + "=" + str(v) + "\n")
    newfile.close


def decode():
    clear()
    print("Enter your encoded text.")
    enctextstr = str(input()).lower()
    print("Decoding...\n")
    enctext = list(enctextstr)
    dectext = ""
    for char in enctext:
        if char in dtb:
            dectext = dectext + dtb[char]
        else:
            dectext = dectext + char
    print("Decoded text (press enter to exit):")
    print(dectext)
    input()


def init():
    dtb = {}
    if path.exists("codes"):
        dtbfile = open("codes")
        dtbraw = []
        for line in dtbfile:
            tmp = line.removesuffix("\n")
            dtbraw.append(tmp)
        dtbfile.close()
        for string in dtbraw:
            tmp = string.split('=')
            dtb[tmp[0]] = tmp[1]
    return(dtb)


def analyze():
    clear()
    print("Enter encoded text:")
    enclist = list(str(input()).lower())
    print("Enter decoded text:")
    declist = list(str(input()).lower())
    if len(enclist) != len(declist):
        print("\nError: The texts are not of equal length! Enter agian please.")
        input()
        analyze()
    print("\nNow analyzing...")
    newinfo = {}
    for i in range(len(enclist)):
        newinfo[enclist[i]] = declist[i]
    oldinfo = []
    for key in list(newinfo):
        if key in dtb and dtb[key] != newinfo[key]:
            oldinfo.append(key)
        elif key in dtb and dtb[key] == newinfo[key]:
            del newinfo[key]
    print("Codes found in text:")
    for k, v in newinfo.items():
        print(str(k) + " => " + str(v))
    if len(oldinfo) > 0:
        print("Conflicts found " + "(" + str(len(oldinfo)) + "):")
        print("Please choose which ones to use (old/new):")
        for char in oldinfo:
            print(char + " => " + str(dtb[char]) +
                  " (old) or " + str(newinfo[char]) + " (new)")
            kpt = str(input()).lower()
            if kpt == "old":
                del newinfo[char]
    print("Press enter to save to file.")
    input()
    for k, v in newinfo.items():
        dtb[k] = v
    overwrite()
    print("Database saved. Press enter to exit.")
    input()


print("Loading database...")
dtb = init()
print("Database loaded. Press enter to continue.")
input()
clear()
print("Choose:")
print("[1] Decode text.")
print("[2] View/edit codebase.")
print("[3] Analyze text.\n")
plyr = str(input())
if plyr == "1":
    decode()
elif plyr == "3":
    analyze()
