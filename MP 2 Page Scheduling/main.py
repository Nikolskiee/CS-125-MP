
def fifo():
    frames = int(input("Enter the number of frames: "))
    faults = []
    page = []
    
    for x in range (0, frames):
        page.append("")

    reference = []

    while(True):
        try:
            x = int(input("Input a frame (Enter nothing to stop): "))
            reference.append(x)
        except:
            break
    
    rc = 0
    fc = 0
    
    while rc < len(reference):
        if reference[rc] in page:
            copy = []
            for x in range(0, frames):
                copy.append("")
            faults.append(copy)
            rc += 1
        else:
            page[fc] = reference[rc]
            copy = page.copy()
            faults.append(copy)
            fc +=1 

            if (fc == 3):
                fc = 0
            rc += 1
    

    x = 0
    string = ""
    while x < len(reference):
        string = str(reference[x]) + "\t\t"
        for y in faults[x]:
            string += str(y) + "\t"
        
        print(string)
        x += 1



def main():
    print("Page Replacement Algorithm")
    print("by: Ivan Baluyut & Nichol Famadico")
    choice = 0
    print("Pick a Page Replacement Algorithm")
    print("1. FIFO")
    print("2. LRU")
    print("3. LFU")
    print("4. MFU")
    choice = int(input("Your choice is: "))
    print()

    while (choice < 1 or choice > 6):
        print("The input was invalid")
        choice = int(input("Your choice is: "))
    print()

    if choice == 1:
        fifo()
    
    
    
    print("Page Replacement Algorithm")
    print("by: Ivan Baluyut & Nichol Famadico")


main()