import time
import threading

class CountdownThread(threading.Thread):
  def __init__(self,count,name):
    threading.Thread.__init__(self)
    self.count=count
    self.name=name
  def run(self):
    while self.count > 0:
      print("Hilo " + self.name + " counting down", self.count)
      self.count -= 1
      time.sleep(5)
    return

fiveCount = CountdownThread(5, "Cinco")
nineCount = CountdownThread(9, "Nueve")
sixCount = CountdownThread(6, "Seis")

nineCount.start()
fiveCount.start()
sixCount.start()