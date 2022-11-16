import argparse
import sys
from task_tracker.task_tracker import TaskTracker
from task_tracker.delivery_task_requester import DeliveryTaskRequester
from task_tracker.get_task import GetTaskList


        
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
                        default=8000)
    args = parser.parse_args(argv[1:])
    task_requestor = DeliveryTaskRequester(args.pickup, 
                                       args.dropoff,
                                       args.dispenser, 
                                       args.ingestor,
                                       args.ip_address,
                                       args.port,
                                       args.start_time)

    task_list_getter = GetTaskList(args.ip_address,args.port)

    def callback():
        print("end loop task callback")
    
    task_tracker = TaskTracker(task_requester=task_requestor,
                                get_task_list=task_list_getter,
                                callback=callback)
    task_tracker.start()
if __name__ == '__main__':
    main(argv=sys.argv)

