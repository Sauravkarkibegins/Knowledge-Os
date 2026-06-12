from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        subprocess.run(["python", "scripts/index_notes.py"])

observer = Observer()
observer.schedule(Handler(), "notes", recursive=False)

observer.start()

while True:
    time.sleep(1)