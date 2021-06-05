def fifo(): #First In First Out
    frames = int(input("Enter the number of frames: "))
    faults = []
    page = []
    
    for x in range (0, frames):
        page.append("")

    reference = []

    while(True):
        try:
            x = int(input("Input a reference (Enter nothing to stop): "))
            reference.append(x)
        except:
            break
    
    rc = 0
    fc = 0

    pc = 0
    
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

            if (fc == frames):
                fc = 0
            rc += 1
            pc += 1
    
    print()
    print("FIRST-IN-FIRST-OUT ALGORITHM")
    print()
    pageArr = [[0 for i in range(len(reference))] for j in range(frames+1)]
    for index, value in enumerate(reference):
        pageArr[0][index] = value
        for index1, value1 in enumerate(faults[index]):
            if(value1 == ""):
                pageArr[index1+1][index] = " "
            else:
                pageArr[index1+1][index] = value1

    refLines = "Reference String"
    pageLines = str(frames) + " Page Frames "
    sepLines = ""
    a,b,c =(0,0,0)
    while a < (4*len(reference)) - 16:
        refLines += "="
        a += 1
    while b < (4*len(reference)) - 14:
        pageLines += "="
        b += 1
    while c < 4*len(reference):
        sepLines += "-"
        c += 1
    
    print(refLines)
    for idx, val in enumerate(pageArr):
        if(idx == 1):
            print(sepLines)
        for y in val:
            print(y,end = "   ")
        print()
    print(pageLines)
    print()
    print("The reference string resulted in", str(pc),"page faults.")
    print()


def lru(): #Least Recently Used
    frames = int(input("Enter the number of frames: "))
    faults = []
    page = []
    
    for x in range (0, frames):
        page.append("")

    reference = []

    while(True):
        try:
            x = int(input("Input a reference (Enter nothing to stop): "))
            reference.append(x)
        except:
            break
    
    rc = 0
    pc = 0
    fc = 0
    
    while rc < len(reference):
        if reference[rc] in page:
            copy = []
            for x in range(0, frames):
                copy.append("")
            faults.append(copy)
            rc += 1
        else:
            if (fc < frames):
                page[fc] = reference[rc]
                fc += 1
            else:
                replace = page[0]
                farthest = 0
                i = 0
                while (i < rc):
                    if(reference[i] == replace):
                        farthest = i
                    i += 1
                
                for x in page:
                    recent = 0
                    i = 0
                    while (i < rc):
                        if(reference[i] == x):
                            recent = i
                        i += 1
                    
                    if (recent < farthest):
                        replace = x
                        farthest = recent

                page[page.index(replace)] = reference[rc]

            copy = page.copy()
            faults.append(copy)
            rc += 1
            pc += 1
    
    print()
    print("LEAST RECENTLY USED ALGORITHM")
    print()
    pageArr = [[0 for i in range(len(reference))] for j in range(frames+1)]
    for index, value in enumerate(reference):
        pageArr[0][index] = value
        for index1, value1 in enumerate(faults[index]):
            if(value1 == ""):
                pageArr[index1+1][index] = " "
            else:
                pageArr[index1+1][index] = value1

    refLines = "Reference String"
    pageLines = str(frames) + " Page Frames "
    sepLines = ""
    a,b,c =(0,0,0)
    while a < (4*len(reference)) - 16:
        refLines += "="
        a += 1
    while b < (4*len(reference)) - 14:
        pageLines += "="
        b += 1
    while c < 4*len(reference):
        sepLines += "-"
        c += 1
    
    print(refLines)
    for idx, val in enumerate(pageArr):
        if(idx == 1):
            print(sepLines)
        for y in val:
            print(y,end = "   ")
        print()
    print(pageLines)
    print()
    print("The reference string resulted in", str(pc),"page faults.")
    print()


def lfu(): #Least Frequently Used
    frames = int(input("Enter the number of frames: "))
    faults = []
    page = []
    
    for x in range (0, frames):
        page.append("")

    reference = []

    while(True):
        try:
            x = int(input("Input a reference (Enter nothing to stop): "))
            reference.append(x)
        except:
            break
    
    rc = 0
    pc = 0
    fc = 0

    history = []
    
    while rc < len(reference):
        if reference[rc] in page:
            copy = []
            for x in range(0, frames):
                copy.append("")
            faults.append(copy)
            rc += 1
        else:
            if (fc < frames):
                page[fc] = reference[rc]
                fc += 1
            else:
                i = 0
                span =[]

                while (i < rc):
                    span.append(reference[i])
                    i += 1
                
                replace = page[0]
                least = span.count(replace)

                for x in page:
                    i = span.count(x)
                    if(i < least):
                        replace = x
                        least = i
                    elif (i == least):
                        y = len(history) - 1
                        while (y >= 0):
                            if(not (x in history[y])):
                                break
                            if(not (replace in history[y])):
                                replace = x
                                least = i
                                break
                            y -= 1

                page[page.index(replace)] = reference[rc]

            copy = page.copy()
            faults.append(copy)
            history.append(copy)
            rc += 1
            pc += 1
    
    print()
    print("LEAST FREQUENTLY USED")
    print()
    pageArr = [[0 for i in range(len(reference))] for j in range(frames+1)]
    for index, value in enumerate(reference):
        pageArr[0][index] = value
        for index1, value1 in enumerate(faults[index]):
            if(value1 == ""):
                pageArr[index1+1][index] = " "
            else:
                pageArr[index1+1][index] = value1

    refLines = "Reference String"
    pageLines = str(frames) + " Page Frames "
    sepLines = ""
    a,b,c =(0,0,0)
    while a < (4*len(reference)) - 16:
        refLines += "="
        a += 1
    while b < (4*len(reference)) - 14:
        pageLines += "="
        b += 1
    while c < 4*len(reference):
        sepLines += "-"
        c += 1
    
    print(refLines)
    for idx, val in enumerate(pageArr):
        if(idx == 1):
            print(sepLines)
        for y in val:
            print(y,end = "   ")
        print()
    print(pageLines)
    print()
    print("The reference string resulted in", str(pc),"page faults.")
    print()


def mfu():
    frames = int(input("Enter the number of frames: "))
    faults = []
    page = []
    
    for x in range (0, frames):
        page.append("")

    reference = []

    while(True):
        try:
            x = int(input("Input a reference (Enter nothing to stop): "))
            reference.append(x)
        except:
            break
    
    rc = 0
    pc = 0
    fc = 0

    history = []
    
    while rc < len(reference):
        if reference[rc] in page:
            copy = []
            for x in range(0, frames):
                copy.append("")
            faults.append(copy)
            rc += 1
        else:
            if (fc < frames):
                page[fc] = reference[rc]
                fc += 1
            else:
                i = 0
                span =[]

                while (i < rc):
                    span.append(reference[i])
                    i += 1
                
                replace = page[0]
                great = span.count(replace)

                for x in page:
                    i = span.count(x)
                    if(i > great):
                        replace = x
                        great = i
                    elif (i == great):
                        y = len(history) - 1
                        while (y >= 0):
                            if(not (x in history[y])):
                                break
                            if(not (replace in history[y])):
                                replace = x
                                great = i
                                break
                            y -= 1

                page[page.index(replace)] = reference[rc]

            copy = page.copy()
            faults.append(copy)
            history.append(copy)
            rc += 1
            pc += 1
    
    print()
    print("MOST FREQUENTLY USED")
    pageArr = [[0 for i in range(len(reference))] for j in range(frames+1)]
    for index, value in enumerate(reference):
        pageArr[0][index] = value
        for index1, value1 in enumerate(faults[index]):
            if(value1 == ""):
                pageArr[index1+1][index] = " "
            else:
                pageArr[index1+1][index] = value1

    refLines = "Reference String"
    pageLines = str(frames) + " Page Frames "
    sepLines = ""
    a,b,c =(0,0,0)
    while a < (4*len(reference)) - 16:
        refLines += "="
        a += 1
    while b < (4*len(reference)) - 14:
        pageLines += "="
        b += 1
    while c < 4*len(reference):
        sepLines += "-"
        c += 1
    
    print(refLines)
    for idx, val in enumerate(pageArr):
        if(idx == 1):
            print(sepLines)
        for y in val:
            print(y,end = "   ")
        print()
    print(pageLines)
    print()
    print("The reference string resulted in", str(pc),"page faults.")
    print()


def main():
    print("Page Replacement Algorithm")
    print("by: Ivan Baluyut & Nichol Famadico")
    choice = 0
    print("Pick a Page Replacement Algorithm")
    print("1. First-In-First-Out")
    print("2. Least-Recently-Used")
    print("3. Least-Frequently-Used")
    print("4. Most-Frequently-Used")
    choice = int(input("Your choice is: "))

    while (choice < 1 or choice > 4):
        print()
        print("The input was invalid")
        choice = int(input("Your choice is: "))
    print()

    if choice == 1:
        fifo()
    if choice == 2:
        lru()
    if choice == 3:
        lfu()
    if choice == 4:
        mfu()
    
    
    print()
    print("Page Replacement Algorithm")
    print("by: Ivan Baluyut & Nichol Famadico")
    print()


main()