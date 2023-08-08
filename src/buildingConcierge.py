from library.Doorman.main import Doorman
from library.pubSubConnect.connector_rabbitmq import RabbitConnector
from library.Doorman.Trustee.votation import VotationTrustee

class BuildingConcierge:
    def __init__(self,doorman,connector):
        self.doorman = doorman
        self.connector = connector

    def run(self):
        
        # Face recognition
        while True:
            # Receiving the face
            method_frame, _, msg = self.connector.pull_msg()
            response_steps = ("Luna",0.8)
            # Check entrance is active
            self.doorman.check_active_entrance()
            # Create new entrance if necessary
            self.doorman.create_new_entrance()
            # Save the entrance if necessary
            self.doorman.save_data_entrance()
            # Check the duration of entrance
            if self.doorman.check_time_to_entrance():
                self.doorman.mark_status(False)
                self.doorman.finish_entrance()
                continue
            else:
                print('Limit not passed')
            # Register steps
            self.doorman.register_steps_entrance(response_steps)
            # Apply Rule
            if self.doorman.check_entry_rule():
                self.doorman.open_door()
                self.doorman.mark_status(True)
                self.doorman.finish_entrance()
            else:
                print('Not able to open yet')

if __name__ == '__main__':
    concierge = BuildingConcierge(Doorman(VotationTrustee(3,0.3)),
                                  RabbitConnector(queue_name='headcut_to_concierge'))
    concierge.run()
