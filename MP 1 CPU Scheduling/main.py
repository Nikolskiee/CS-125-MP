#PROCESS CLASS
class Process:
    def __init__(self, name, priority, arrival, burst):
        self.name = name
        self.priority = priority
        self.arrival = arrival
        self.burst = burst
        self.completion = 0
        self.response = 0
        self.waiting = 0
        self.turnaround = 0
        self.remaining = self.burst
    

def fcfs(): #First Come First Serve
    print("**********")
    print()
    print("FIRST-COME-FIRST SERVE ALGORITHM")
    print()
    count = int(input("Enter the number of processes: "))
    i = 1
    time = 0
    processes = []
    while(i <= count):
        name = "P" + str(i)
        print(name)
        priority = i
        arrival = int(input("Arrival time: "))
        burst = int(input("Burst time: "))
        time += burst
        
        process = Process(name, priority, arrival, burst)
        processes.append(process)
        i = i + 1

    t = 0 #time
    ready = [] #ready queue
    active = None
    gantt = [] #Gantt Chart

    while (t <= time):
        for x in processes:
            if (x.arrival == t):
                ready.append(x)

        if(active != None):
            if (t == active.completion):
                active.turnaround = active.completion - active.arrival
                active = None
            
        if (len(ready) != 0 and active == None):
            active = ready[0]
            for x in ready:
                if (x.arrival < active.arrival):
                    active = x
                elif((x.arrival == active.arrival) and (x.priority < active.priority)):
                    active = x
                else:
                    continue
            
            ready.remove(active)
            gantt.append(active)
            active.response = (t - active.arrival)
            active.waiting = active.response
            active.completion = t + active.burst
        
        t += 1

    print()
    print("**********")
    print()
    print("FIRST-COME-FIRST SERVE ALGORITHM")
    print()
    print("The Gantt Chart")
    pgantt = "   ______"
    for x in gantt:
        pgantt = pgantt + x.name + "______"
    print(pgantt)

    tgantt = "     00\t "
    for y in gantt:
        if(len(str(y.completion)) == 1):
            tgantt = tgantt + "    0" + str(y.completion) + "\t "
        else:
            tgantt = tgantt + "    " + str(y.completion) + "\t "
    print(tgantt)

    print()
    print("The Table")
    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    rAvr = 0
    wAvr = 0
    tAvr = 0
    for x in processes:
        rAvr += x.response
        wAvr += x.waiting
        tAvr += x.turnaround
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)
    print("AVERAGE-------------------------", round(rAvr/count, 3), "\t", round(wAvr/count, 3), "\t", round(tAvr/count, 3))


def sjf(): #Shortest Job First
    print("**********")
    print()
    print("SHORTEST-JOB-FIRST ALGORITHM")
    print()
    count = int(input("Enter the number of processes: "))
    i = 1
    time = 0
    processes = []
    while(i <= count):
        name = "P" + str(i)
        print(name)
        priority = i
        arrival = int(input("Arrival time: "))
        burst = int(input("Burst time: "))
        time += burst
        
        process = Process(name, priority, arrival, burst)
        processes.append(process)
        i = i + 1

    t = 0 #time
    ready = [] #ready queue
    active = None
    gantt = [] #Gantt Chart

    while (t <= time):
        for x in processes:
            if (x.arrival == t):
                ready.append(x)

        if(active != None):
            if (t == active.completion):
                active.turnaround = active.completion - active.arrival
                active = None
            
        if (len(ready) != 0 and active == None):
            active = ready[0]
            for x in ready:
                if (x.burst < active.burst):
                    active = x
                elif((x.burst == active.burst) and (x.priority < active.priority)):
                    active = x
                else:
                    continue
            
            ready.remove(active)
            gantt.append(active)
            active.response = (t - active.arrival)
            active.waiting = active.response
            active.completion = t + active.burst
        
        t += 1

    print()
    print("**********")
    print()
    print("SHORTEST-JOB-FIRST ALGORITHM")
    print()
    print("The Gantt Chart")
    pgantt = "   ______"
    for x in gantt:
        pgantt = pgantt + x.name + "______"
    print(pgantt)

    tgantt = "     00\t "
    for y in gantt:
        if(len(str(y.completion)) == 1):
            tgantt = tgantt + "    0" + str(y.completion) + "\t "
        else:
            tgantt = tgantt + "    " + str(y.completion) + "\t "
    print(tgantt)

    print()
    print("The Table")
    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    rAvr = 0
    wAvr = 0
    tAvr = 0
    for x in processes:
        rAvr += x.response
        wAvr += x.waiting
        tAvr += x.turnaround
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)
    print("AVERAGE-------------------------", round(rAvr/count, 3), "\t", round(wAvr/count, 3), "\t", round(tAvr/count, 3))


def strf(): #Shortest Remaining Time First
    print("**********")
    print()
    print("SHORTEST-REMAINING-TIME-FIRST ALGORITHM")
    print()
    count = int(input("Enter the number of processes: "))
    i = 1
    time = 0
    processes = []
    while(i <= count):
        name = "P" + str(i)
        print(name)
        priority = i
        arrival = int(input("Arrival time: "))
        burst = int(input("Burst time: "))
        time += burst
        
        process = Process(name, priority, arrival, burst)
        processes.append(process)
        i = i + 1

    t = 0 #time
    ready = [] #ready queue
    active = None
    gantt = [] #Gantt Chart
    gantt.append("0")

    while (t <= time):

        if(len(ready) != 0):
            for x in ready:
                x.waiting += 1
        
        for x in processes:
            if (x.arrival == t):
                ready.append(x)

        if(active != None):
            active.remaining -= 1
            if (active.remaining == 0):
                active.completion = t
                active.turnaround = active.completion - active.arrival
                active = None
                gantt.append(str(t))
            else:
                buffer = active
                for x in ready:
                    if (x.remaining < active.remaining):
                        active = x
                    elif((x.remaining == active.remaining) and (x.priority < active.priority)):
                        active = x
                    else:
                        continue
                
                if(buffer != active):
                    ready.append(buffer)
                    ready.remove(active)
                    gantt.append(str(t))
                    gantt.append(active.name)

                    if(active.remaining == active.burst): 
                        active.response = (t - active.arrival)

            
        if (len(ready) != 0 and active == None):
            active = ready[0]
            for x in ready:
                if (x.remaining < active.remaining):
                    active = x
                elif((x.remaining == active.remaining) and (x.priority < active.priority)):
                    active = x
                else:
                    continue
            
            ready.remove(active)
            gantt.append(active.name)
            if(active.remaining == active.burst): 
                active.response = (t - active.arrival)

        t += 1

    print()
    print("**********")
    print()
    print("SHORTEST-REMAINING-TIME-FIRST ALGORITHM")
    print()
    print("The Gantt Chart")
    pgantt = "   ______"
    for index, value in enumerate(gantt):
        if index%2 != 0:
                pgantt = pgantt + value + "______"
    print(pgantt)

    tgantt = ""
    for index, value in enumerate(gantt):
        if(index%2 == 0):
            if(len(value) == 1):
                if(index == 0):
                    tgantt = tgantt + "     0" + value + "\t "
                else:
                    tgantt = tgantt + "    0" + value + "\t "
            else:
                tgantt = tgantt + "    " + value + "\t "
    print(tgantt)

    print()
    print("The Table")
    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    rAvr = 0
    wAvr = 0
    tAvr = 0
    for x in processes:
        rAvr += x.response
        wAvr += x.waiting
        tAvr += x.turnaround
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)
    print("AVERAGE-------------------------", round(rAvr/count, 3), "\t", round(wAvr/count, 3), "\t", round(tAvr/count, 3))


def pnp(): #Priority Non-Preemptive
    print("**********")
    print()
    print("PRIORITY NON-PREEMPTIVE ALGORITHM")
    print()
    count = int(input("Enter the number of processes: "))
    i = 1
    time = 0
    processes = []
    while(i <= count):
        name = "P" + str(i)
        print(name)
        priority = int(input("Priority: "))
        arrival = int(input("Arrival time: "))
        burst = int(input("Burst time: "))
        time += burst
        
        process = Process(name, priority, arrival, burst)
        processes.append(process)
        i = i + 1

    t = 0 #time
    ready = [] #ready queue
    active = None
    gantt = [] #Gantt Chart

    while (t <= time):
        for x in processes:
            if (x.arrival == t):
                ready.append(x)

        if(active != None):
            if (t == active.completion):
                active.turnaround = active.completion - active.arrival
                active = None
            
        if (len(ready) != 0 and active == None):
            active = ready[0]
            for x in ready:
                if (x.priority < active.priority):
                    active = x
                else:
                    continue
            
            ready.remove(active)
            gantt.append(active)
            active.response = (t - active.arrival)
            active.waiting = active.response
            active.completion = t + active.burst
        
        t += 1

    print()
    print("**********")
    print()
    print("PRIORITY NON-PREEMPTIVE ALGORITHM")
    print()
    print("The Gantt Chart")
    pgantt = "   ______"
    for x in gantt:
        pgantt = pgantt + x.name + "______"
    print(pgantt)

    tgantt = "     00\t "
    for y in gantt:
        if(len(str(y.completion)) == 1):
            tgantt = tgantt + "    0" + str(y.completion) + "\t "
        else:
            tgantt = tgantt + "    " + str(y.completion) + "\t "
    print(tgantt)

    print()
    print("The Table")
    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    rAvr = 0
    wAvr = 0
    tAvr = 0
    for x in processes:
        rAvr += x.response
        wAvr += x.waiting
        tAvr += x.turnaround
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)
    print("AVERAGE-------------------------", round(rAvr/count, 3), "\t", round(wAvr/count, 3), "\t", round(tAvr/count, 3))


def pp():
    print("**********")
    print()
    print("PRIORITY PREEMPTIVE ALGORITHM")
    print()
    count = int(input("Enter the number of processes: "))
    i = 1
    time = 0
    processes = []
    while(i <= count):
        name = "P" + str(i)
        print(name)
        priority = int(input("Priority: "))
        arrival = int(input("Arrival time: "))
        burst = int(input("Burst time: "))
        time += burst
        
        process = Process(name, priority, arrival, burst)
        processes.append(process)
        i = i + 1

    t = 0 #time
    ready = [] #ready queue
    active = None
    gantt = [] #Gantt Chart
    gantt.append("0")

    while (t <= time):
        if (len(ready) != 0):
            for x in ready:
                x.waiting += 1
        
        for x in processes:
            if (x.arrival == t):
                ready.append(x)

        if(active != None):
            active.remaining -= 1
            if (active.remaining == 0):
                active.completion = t
                active.turnaround = active.completion - active.arrival
                active = None
                gantt.append(str(t))
            else:
                buffer = active
                for x in ready:
                    if (x.priority < active.priority):
                        active = x
                    else:
                        continue
                
                if(buffer != active):
                    ready.append(buffer)
                    ready.remove(active)
                    gantt.append(str(t))
                    gantt.append(active.name)

                    if(active.remaining == active.burst): 
                        active.response = (t - active.arrival)
            
        if (len(ready) != 0 and active == None):
            active = ready[0]
            for x in ready:
                if (x.priority < active.priority):
                    active = x
                else:
                    continue
            
            ready.remove(active)
            gantt.append(active.name)
            if(active.burst == active.remaining): 
                active.response = (t - active.arrival)
        
        t += 1

    print()
    print("**********")
    print()
    print("PRIORITY PREEMPTIVE ALGORITHM")
    print()
    print("The Gantt Chart")
    pgantt = "   ______"
    for index, value in enumerate(gantt):
        if index%2 != 0:
                pgantt = pgantt + value + "______"
    print(pgantt)

    tgantt = ""
    for index, value in enumerate(gantt):
        if(index%2 == 0):
            if(len(value) == 1):
                if(index == 0):
                    tgantt = tgantt + "     0" + value + "\t "
                else:
                    tgantt = tgantt + "    0" + value + "\t "
            else:
                tgantt = tgantt + "    " + value + "\t "
    print(tgantt)

    print()
    print("The Table")
    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    rAvr = 0
    wAvr = 0
    tAvr = 0
    for x in processes:
        rAvr += x.response
        wAvr += x.waiting
        tAvr += x.turnaround
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)
    print("AVERAGE-------------------------", round(rAvr/count, 3), "\t", round(wAvr/count, 3), "\t", round(tAvr/count, 3))


def rr():
    print("**********")
    print()
    print("ROUND-ROBIN ALGORITHM")
    print()
    count = int(input("Enter the number of processes: "))
    quantum = int(input("Enter the time quantum: "))
    i = 1
    time = 0
    processes = []
    while(i <= count):
        name = "P" + str(i)
        print(name)
        priority = i
        arrival = int(input("Arrival time: "))
        burst = int(input("Burst time: "))
        time += burst
        
        process = Process(name, priority, arrival, burst)
        processes.append(process)
        i = i + 1

    t = 0 #time
    q = 0 #time quantum
    ready = [] #ready queue
    active = None
    gantt = [] #Gantt Chart
    gantt.append("0")

    while (t <= time):
        if (len(ready) != 0):
            for x in ready:
                x.waiting += 1
        
        for x in processes:
            if (x.arrival == t):
                ready.append(x)

        if(active != None):
            active.remaining -= 1
            if (active.remaining == 0):
                active.completion = t
                active.turnaround = active.completion - active.arrival
                active = None
                gantt.append(str(t))
                q = 0
            elif (q == quantum):
                buffer = active
                if(len(ready) != 0):
                    active = ready[0]
                
                if(buffer != active):
                    ready.append(buffer)
                    ready.remove(active)
                    gantt.append(str(t))
                    gantt.append(active.name)

                    if(active.remaining == active.burst): 
                        active.response = (t - active.arrival)
                    
                
                q = 0
            
        if (len(ready) != 0 and active == None):
            active = ready[0]
            
            ready.remove(active)
            gantt.append(active.name)
            if(active.burst == active.remaining): 
                active.response = (t - active.arrival)
            
            q = 0
        
        t += 1
        q += 1

    print()
    print("**********")
    print()
    print("ROUND-ROBIN ALGORITHM")
    print()
    print("The Gantt Chart")
    pgantt = "   ______"
    for index, value in enumerate(gantt):
        if index%2 != 0:
                pgantt = pgantt + value + "______"
    print(pgantt)

    tgantt = ""
    for index, value in enumerate(gantt):
        if(index%2 == 0):
            if(len(value) == 1):
                if(index == 0):
                    tgantt = tgantt + "     0" + value + "\t "
                else:
                    tgantt = tgantt + "    0" + value + "\t "
            else:
                tgantt = tgantt + "    " + value + "\t "
    print(tgantt)

    print()
    print("The Table")
    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    rAvr = 0
    wAvr = 0
    tAvr = 0
    for x in processes:
        rAvr += x.response
        wAvr += x.waiting
        tAvr += x.turnaround
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)
    print("AVERAGE-------------------------", round(rAvr/count, 3), "\t", round(wAvr/count, 3), "\t", round(tAvr/count, 3))


def main():
    print()
    print("CPU Process Scheduling")
    print("by: Ivan Baluyut & Nichol Famadico")
    print()
    choice = 0
    print("Pick a CPU Scheduling Algorithm")
    print("1. First-Come First-Served")
    print("2. Shortest-Job-First")
    print("3. Shortest-Remaining-Time-First")
    print("4. Priority Scheduling (Non-Preemptive)")
    print("5. Priority Scheduling (Preemptive)")
    print("6. Round Robin")
    print("=======================================")
    choice = int(input("Your choice is: "))

    while (choice < 1 or choice > 6):
        print()
        print("The input was invalid")
        choice = int(input("Your choice is: "))
    print()
    
    if(choice == 1):
        fcfs()
    if(choice == 2):
        sjf()
    if(choice == 3):
        strf()
    if(choice == 4):
        pnp()
    if(choice == 5):
        pp()
    if(choice == 6):
        rr()
    
    print()
    print("**********")
    print()
    print("CPU Process Scheduling")
    print("by: Ivan Baluyut & Nichol Famadico")
    print()


main()