import threading
import time

class MyTread(threading.Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(1)


thread1 = MyTread()
thread2 = MyTread()

thread1.start()
thread2.start()