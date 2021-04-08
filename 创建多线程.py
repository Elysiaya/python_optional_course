import threading
import time


def test(x, y):
    for i in range(x, y):
        print(i)
        time.sleep(1)


thread1 = threading.Thread(name="a1", target=test, args=(1, 20))
thread2 = threading.Thread(name='a2', target=test, args=(20, 40))

thread1.start()
thread2.start()
