import sys 
import time 
import random
import os 
import shutil 
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hi, {event.src_path} has been created")
    
    def on_deleted(self,event):
        print(f"oops! someone deleted {event.src_path}!")

    def on_modified(self,event):
        print(f"hi, {event.src_path} has been modified")
    
    def on_moved(self,event):
        print(f"hi, {event.src_path} has been moved")

event_handler = FileMovementHandler()



from_dir = "C:\Users\puppy\OneDrive - Central Coast Grammar School\Documents"
observer = Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

try: 
   while True: 
    time.sleep(2)
    print("running..")
except KeyboardInterrupt:
   print("stopped!")
   observer.stop()