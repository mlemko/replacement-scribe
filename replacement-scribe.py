# import only system from os
from os import system, name, remove, path
from sys import version_info as verin


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def overwrite(dtb):
    if path.exists("codes"):
        remove("codes")
    newfile = open("codes", "x+t")
    for k, v in dtb.items():
        newfile.write(str(k) + "=" + str(v) + "\n")
    newfile.close


def decode(dtb):
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
    print("Decoded text (press enter to return):")
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


def analyze(dtb):
    clear()
    print("Enter encoded text:")
    enclist = list(str(input()).lower())
    print("Enter decoded text:")
    declist = list(str(input()).lower())
    if len(enclist) != len(declist):
        print("\nError: The texts are not of equal length! Enter agian please.")
        input()
        return(analyze(dtb))
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
    overwrite(dtb)
    print("Database saved. Press enter to return.")
    input()
    
def view_data(dtb, changes_made = False):
    clear()
    print("Current known replacements:")
    print("Original\x09Actual")
    for char in dtb:
        print(f"'{char}'\x09=>\x09'{dtb[char]}'")
    if changes_made:
        print("Type an original character to replace (save to save changes, empty to exit without saving):")
    else:
        print("Type an original character to replace (empty to exit):")

    plyr = input()
    if len(plyr) == 1:
        if plyr in dtb:
            print("Replace with?")
            repl = input().strip()[0].lower()
            dtb[plyr] = repl
            changes_made = True
            print(f"Replaced with {plyr} => {repl}. Press enter to continue.")
            input()
    elif plyr == "":
        if changes_made:
            if input("Changes made will be lost! Type 'Yes' to confirm: ") != "Yes":
                return(view_data(dtb, changes_made))
        return()
    elif plyr == "save":
        overwrite(dtb)
        print("Database saved. Press enter to return.")
        return()
    return(view_data(dtb, changes_made))    

def main():
    print("Loading database...")
    dtb = init()
    print("Database loaded. Press enter to continue.")
    input()
    while(True):
        clear()
        print("Choose:")
        print("[1] Decode text.")
        print("[2] View/edit codebase.")
        print("[3] Analyze text.")
        print("[4] Exit\n")
        plyr = str(input())
        if verin.major <= 3 or verin.minor <= 10:
            match plyr:
                case "1":
                    decode(dtb)
                case "2":
                    view_data(dtb)
                    dtb = init()
                case "3":
                    analyze(dtb)
                case "4":
                    exit(0)
        else:
            if plyr == "1":
                decode(dtb)
            elif plyr == "2":
                view_data(dtb)
                dtb = init()
            elif plyr == "3":
                analyze(dtb)
            elif plyr == "4":
                exit(0)
        
    
    
    
if __name__ == "__main__":
    main()
