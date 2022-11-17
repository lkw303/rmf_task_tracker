import sys
import requests
import argparse
import json


class LoopTaskRequester():
    def __init__(self, start, finish, num_loops, ip_address, port, start_time=0):
        self.start = start
        self.finish = finish
        self.num_loops = num_loops
        self.start_time = start_time
        self.ip_address = ip_address
        self.port = port
        self.route = '/submit_task'

        self.delivery_task_json = {}
        self.delivery_task_json['task_type'] = 'Loop'
        self.delivery_task_json['start_time'] = self.start_time
        description = {}
        description["start_name"] = self.start
        description["finish_name"] = self.finish
        description["num_loops"] = self.num_loops
        self.delivery_task_json['description'] = description
    
    def get_url(self):
        ip = self.ip_address
        port = self.port
        url = f"http://{ip}:{port}{self.route}"
        return url

    def post_request(self):
        print(f'Sending task request {self.delivery_task_json} to url: {self.get_url()}')
        return requests.post(json=self.delivery_task_json, url=self.get_url())

def main(argv=sys.argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--start', required=True,
                        type=str,
                        help="Start waypoint")
    parser.add_argument('-f', '--finish', required=True,
                        type=str,
                        help="Finish Waypoint")
    parser.add_argument('-nl', '--num_loops', required=True,
                        type=int,
                        help="number of loops")
    parser.add_argument('-st', '--start_time',
                        type=int,
                        help="Start time in seconds. Default is 0",
                        default=0)
    parser.add_argument('-ip', '--ip_address',
                        type=str,
                        help="IP Address",
                        default='localhost')
    parser.add_argument('-pt', '--port',
                        type=str,
                        help="port number",
                        default=8083)
                        
    args = parser.parse_args(argv[1:])
    task_requestor = LoopTaskRequester(args.start, 
                                       args.finish, 
                                       args.num_loops, 
                                       args.ip_address,
                                       args.port,
                                       args.start_time)

    resp = json.loads(task_requestor.post_request().text)
    err_msg = resp['error_msg']
    task_id = resp['task_id']
    print(f'task_id: {task_id}, error_msg: {err_msg}')
    # print(resp.text)

if __name__ == '__main__':
    main(argv=sys.argv)
        