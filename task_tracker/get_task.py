import requests
from pprint import pprint


class GetTaskList():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.route = '/task_list'
    
    def get_url(self):
        return f'http://{self.ip}:{self.port}{self.route}'

    def get_task_list(self):
        return requests.get(self.get_url())
        

def main():
    task_requester = GetTaskList('localhost',8083)
    task_list = task_requester.get_task_list()
    pprint(f"Task List: {task_list.text}")
    
if __name__ == '__main__':
    main()