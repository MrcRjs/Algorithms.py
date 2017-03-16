import multiprocessing
import time
import uuid
import random
#import os

def listener(sender, receiver):
    sender.close()
    while True:
        try:
            song = receiver.recv()
        except EOFError:
            break
        print(song)
        #print("Listener: ", os.getpid())
        #print("Listener parent: ", os.getppid())

def songSender(song, listener_p):
    #print("Sender: ", os.getpid())
    #print("Sender parent: ", os.getppid())
    listener_p.send(song)

if __name__ == '__main__':
    sender, receiver = multiprocessing.Pipe()
    pro_listener = multiprocessing.Process(target=listener, args=(sender, receiver))
    pro_listener.start()

    # Close songSender input
    receiver.close()
    for n in range(0, 100):
        songSender({"id": uuid.uuid4(), "duration": random.randint(3,8)}, sender)
        time.sleep(3)
    sender.close()
