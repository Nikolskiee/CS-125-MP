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

    print("Gantt")
    for x in gantt:
        print(x.name, x.completion)

    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    for x in processes:
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)

def sjf(): #Shortest Job First
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

    print("Gantt")
    for x in gantt:
        print(x.name, x.completion)

    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    for x in processes:
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)

def strf(): #Shortest Remaining Time First
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

    print("Gantt")
    print(0)
    for x in gantt:
        print(x)

    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    for x in processes:
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)

def pnp(): #Priority Non-Preemptive
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

    print("Gantt")
    for x in gantt:
        print(x.name, x.completion)

    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    for x in processes:
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)

def pp():
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

    print("Gantt")
    print(0)
    for x in gantt:
        print(x)

    print("Pro \t Bur \t Arr \t Com \t Res \t Wai \t Tur")
    for x in processes:
        print(x.name, "\t", x.burst, "\t", x.arrival, "\t", x.completion, "\t", x.response, "\t", x.waiting, "\t", x.turnaround)


def main():
    print("CPU Process Scheduling")
    print("by: Ivan Baluyut & Nichol Famadico")
    choice = 0
    print("Pick a CPU Scheduling Algorithm")
    print("1. First-Come First-Served")
    print("2. Shortest-Job-First")
    print("3. Shortest-Remaining-Time-First")
    print("4. Priority Scheduling (Non-Preemptive)")
    print("5. Priority Scheduling (Preemptive)")
    print("6. Round Robin")
    choice = int(input("Your choice is: "))
    print()

    while (choice < 1 or choice > 6):
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
    
    print("CPU Process Scheduling")
    print("by: Ivan Baluyut & Nichol Famadico")


main()