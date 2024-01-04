
class BotController:
    current = 0
    run_thread = False
    
    
    def __init__(self):
       # self.bot_thread = threading.Thread(target=self.main_loop)
        pass
     
    
   
    def main_loop(self):
        while self.run_thread:
            self.current += 1
    
    def cycle_switch(self):
        if self.run_thread:
            self.current = 0
            self.run_thread = False
            return 'turned off'
        else:
            self.run_thread =True
            self.bot_thread = threading.Thread(target=self.main_loop)
            self.bot_thread.start()
            return 'turned on'
    
    def thread_state(self)->bool:
        return self.bot_thread.is_alive()
    


from flask import Flask
import threading

app = Flask(__name__)
bot = BotController()



@app.route('/')
def hello_world():
   
   
    return 'Hello from Flask! '+ str(bot.current)

@app.route('/botSwitch')
def change_bot_state():
    return bot.cycle_switch()
    
@app.route('/botState')
def get_bot_state():
    return 'alive' if bot.thread_state()  else 'not alive'


    
    




