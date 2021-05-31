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
        self.running = False
        self.waiting = False
    

def fcfs():
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

    t = 0

def main():
    print("CPU Process Scheduling")
    print("by: Ivan Baluyut & Nichol Famadico")
    choice = 0
    print("Pick a CPU Scheduling Algorithm")
    print("1. First-Come First-Served")
    print("2. Shortest-Job-First")
    print("3. Shortest-Time-First")
    print("4. Priority Schediling (Non-Preemptive")
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


main()