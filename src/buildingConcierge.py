from library.Doorman.main import Doorman
from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from library.Doorman.Trustee.votation import VotationTrustee
from library.logger.main import Logger

class BuildingConcierge:
    def __init__(self,doorman,connector):
        self.doorman = doorman
        self.connector = connector

    def run(self):
        
        # Face recognition
        while True:
            # Receiving the face
            method_frame, _, body = self.connector.pull_msg()
            if body is None:
                continue
            # Check entrance is active
            self.doorman.check_active_entrance()
            # Create new entrance if necessary
            self.doorman.create_new_entrance()
            # Save the entrance if necessary
            self.doorman.save_data_entrance()
            # Check the duration of entrance
            if self.doorman.check_time_to_entrance():
                Logger.emit('Checking if has active entrance')
                self.doorman.mark_status(False)
                self.doorman.finish_entrance()
                continue
            # Register steps
            self.doorman.register_steps_entrance(body.decode('utf-8'))
            # Apply Rule
            if self.doorman.check_entry_rule():
                self.doorman.open_door()
                self.doorman.mark_status(True)
                self.doorman.finish_entrance()

if __name__ == '__main__':
    concierge = BuildingConcierge(Doorman(VotationTrustee(7,0.3)),
                                  RabbitConnector(queue_name='FaceRecognition_to_Concierge'))
    concierge.run()
