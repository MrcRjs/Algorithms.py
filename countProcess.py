import time
import multiprocessing

class CountdownProcess(multiprocessing.Process):
    def __init__(self, count, name):
        multiprocessing.Process.__init__(self)
        self.count = count
        self.name = name
    def run(self):
        while self.count > 0:
            print("Proceso " + self.name + " counting down", self.count)
            self.count -= 1
            #time.sleep(5)
        return
if __name__ == '__main__':
  sixCount = CountdownProcess(6, "Seis")
  fiveCount = CountdownProcess(5, "Cinco")
  nineCount = CountdownProcess(9, "Nueve")

  nineCount.start()
  fiveCount.start()
  sixCount.start()