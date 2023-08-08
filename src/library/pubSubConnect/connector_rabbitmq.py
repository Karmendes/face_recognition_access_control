import pika
from library.pubSubConnect.main import PubSubConnect

class RabbitConnector(PubSubConnect):
    def __init__(self,host = 'localhost',queue_name='film_maker_to_face_detector'):
        self.host = host
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
    def push_msg(self,data):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=data)
    def pull_msg(self):
        pass
    def close(self):
        self.connection.close()
