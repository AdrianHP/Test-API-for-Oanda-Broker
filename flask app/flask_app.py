from flask import Flask
import threading
current = 0
app = Flask(__name__)


def sum():
    global current
    while 1:
        current += 1

@app.route('/')
def hello_world():
    global current
    # thread1 = threading.Thread(target=sum)
    # thread1.start()

    return 'Hello from Flask! '+ str(current)
