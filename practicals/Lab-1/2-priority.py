def Priority(p,n,bt,priority):
    for i in range(l):
        for j in range(i,l):
            if priority[i]>priority[j]:
                temp=priority[i]
                priority[i]=priority[j]
                priority[j]=temp
                y=p[i]
                p[i]=p[j]
                p[j]=y
                z=bt[i]
                bt[i]=bt[j]
                bt[j]=z
    waitingtime=[]
    turnaaround_time=[]
    for i in range(l):
        if i==0:
            waitingtime.append(0)
        else:
            x=bt[i-1]+ waitingtime[i-1]
            waitingtime.append(x)

    for i in range(l):
        if i==0:
            turnaaround_time.append(bt[i])
        else:
            y=bt[i]+waitingtime[i]
            turnaaround_time.append(y)



    totaltime_waiting=0
    total_turnaround=0
    print( "Processes Burst time " + " Waiting time " + " Turn around time")
    for i in range(l):




        print(" " + str(p[i]) + "\t\t\t"+str(bt[i])+"\t\t\t"+ str(waitingtime[i])+"\t\t\t"+ str(turnaaround_time[i]))
    Average_waiting_time=(totaltime_waiting)/l
    Average_turnaround_time=(total_turnaround)/l


    print("Avg waiting time=",Average_waiting_time)
    print("Avg turnaround time=",Average_turnaround_time)

process=[]
bt=[]
priority=[]
l=int((input("Enter the number of Processes and Burst Time")))
for i in range(l):
    process.append(int(input()))


print('Enter Burst Time:')
for i in range(l):
    bt.append(int(input()))
print('Enter priority value:')
for i in range(l):
    priority.append(int(input()))


print("Process:")
print(process)
print("Burst Time:")
print(bt)
print("Give Priority:")
print(priority)
Priority(process, l, bt, priority)
