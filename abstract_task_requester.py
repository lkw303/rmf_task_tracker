from abc import ABC, abstractmethod

class TaskRequster(ABC):
    def __init__(self, args: list):
        self.ip = args.ip_address
        self.port = args.port
        self.route = '/submit_task'
        self.task_json = None

    @abstractmethod
    def set_attributes(self):
        pass        ip = self.ip_address
        port = self.port
        url = f"http://{ip}:{port}{self.route}"
        return url
    
    def get_url(self):
        ip = self.ip_address
        port = self.port
        url = f"http://{ip}:{port}{self.route}"
        return url

    def post_request(self)