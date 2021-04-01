import threading
import time

class CricticalSection():
    def _init_(self):
        self.sem = threading.Semaphore()  #initializing semaphore using Semaphore class in threading module

    def process_1(self):
        while True:
            print("Entry Section 1")
            self.sem.acquire()      #decrement the value of semahpore

            self.criticalsection()  #entering crictical section(process 1)
            self.sem.release()

            print("Critical Section over for process 1") #
            time.sleep(3)           #allowing some delay in the process

    def process_2(self):
        while True:
            print("Entry Section-2")
            self.sem.acquire()      #decrement the value of semahpore

            self.criticalsection()  #entering crictical section (process 2)
            self.sem.release()

            print("Critical Section over for process 2")
            time.sleep(3)    #allowing some delay in the process

    def criticalsection(self):
        print(" Entered Critical Section!. Perform operation on shared resource")

    def main(self):
        t1 = threading.Thread(target = self.process_1) #calling process 1
        t1.start()
        t2 = threading.Thread(target = self.process_2) #calling  process 2
        t2.start()
start=time.time()
if _name=="main_":
    c = CricticalSection()
    c.main()

time_taken=time.time()-start
