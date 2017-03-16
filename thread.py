import threading
def conteo():
  for x in range(1,100):
    print("PID: " + " i: ", x)
hilo1 = threading.Thread()
hilo1.run = conteo
hilo2 = threading.Thread()
hilo2.run = conteo
hilo1.start()
hilo2.start()