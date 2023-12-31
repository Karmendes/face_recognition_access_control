import os
from uuid import uuid4
from datetime import datetime
from time import time
import json
import shutil
from library.logger.main import Logger

class Doorman:
    def __init__(self,trustee):
        self.data_entrance = None
        self.__trustee = trustee
        self.state_entrance = None

    def check_active_entrance(self,path = 'data/active'):
        self.state_entrance = (len(os.listdir(path)) != 0)

    def create_new_entrance(self):
        if self.state_entrance == False:
            self.data_entrance = {
                "id": str(uuid4()),
                "dh_start": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "dh_end": None,
                "status": None,
                "dh_start_time":time(),
                "steps":[]

            }
            self.state_entrance = True
            Logger.emit('New entrance')
    
    def save_data_entrance(self,path = 'data/active/'):
        with open(path + self.data_entrance['id'] + '.json', 'w') as json_file:
            json.dump(self.data_entrance, json_file)

    def finish_entrance(self,path_active = 'data/active/',path_inactive = 'data/inactive/'):
        self.data_entrance['dh_end'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.save_data_entrance(path_active)
        shutil.move(path_active + self.data_entrance['id'] + '.json', path_inactive)
        Logger.emit('Exiting entrance')

    def check_time_to_entrance(self,duration = 50):
        return time() - self.data_entrance['dh_start_time'] > duration
    
    def register_steps_entrance(self,response_steps):
        self.data_entrance['steps'].append(response_steps)

    def check_entry_rule(self):
        return self.__trustee.apply_rule(self.data_entrance['steps'])

    def open_door(self):
        Logger.emit('Opening the door')

    def mark_status(self,status:bool):
        self.data_entrance['status'] = status