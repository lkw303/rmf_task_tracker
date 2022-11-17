import sys
import requests
import argparse
import json


class DeliveryTaskRequester():
    def __init__(self, pickup, dropoff, dispenser, ingestor, ip_address, port, start_time=0):
        self.pickup = pickup
        self.dropoff = dropoff
        self.dispenser = dispenser
        self.ingestor = ingestor
        self.start_time = start_time
        self.ip_address = ip_address
        self.port = port
        self.route = '/submit_task'

        self.delivery_task_json = {}
        self.delivery_task_json['task_type'] = 'Delivery'
        self.delivery_task_json['start_time'] = self.start_time
        description = {}
        description["pickup_place_name"] = self.pickup
        description["pickup_dispenser"] = self.dispenser
        description["dropoff_place_name"] = self.dropoff
        description["dropoff_ingestor"] = self.ingestor
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
    parser.add_argument('-p', '--pickup', required=True,
                        type=str,
                        help="Pickup name")
    parser.add_argument('-d', '--dropoff', required=True,
                        type=str,
                        help="Dropoff name")
    parser.add_argument('-in', '--ingestor', required=True,
                        type=str,
                        help="Ingestor names")
    parser.add_argument('-di', '--dispenser', required=True,
                        type=str,
                        help="Dispenser names")
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
    task_requestor = DeliveryTaskRequester(args.pickup, 
                                       args.dropoff, 
                                       args.dispenser, 
                                       args.ingestor,
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
        