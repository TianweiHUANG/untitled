import time, threading
from threading_t1_TEST_20190815 import music
from threading_t2_TEST_20190815 import movie

t1 = threading.Thread(target=music, args=("青花瓷", ))
t2 = threading.Thread(target=movie, args=("英雄远征", ))
t1.setDaemon(True) # 设置守护线程
t2.setDaemon(True) # 设置守护线程
t1.start()
t2.start()

time.sleep(30)
print("困了,想睡觉了...")