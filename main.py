import threading

from google.protobuf import service

from drive_blackbox.bootup import coldstart
from drive_blackbox.HelperMethods import createFolderForAllUploads,checkIfAutoFolderExists
from listener.watchdog import start_listening
from threading import Thread
import time
def main():
    #check source path
    print(threading.current_thread().name)
    start_listening('G:\TestFiles')
    print('Coldstarting the application......')
    #service=coldstart()
    #createFolderForAllUploads(service)
    #checkIfAutoFolderExists(service)

if __name__ == '__main__':
    print('Welcome')
    print(threading.current_thread().name)
    t=Thread(target=main)
    t.setDaemon(True)
    t.start()
    t.join()
    print('Done executing')
