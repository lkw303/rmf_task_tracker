import argparse
import sys
import time
from task_tracker.loop_task_requester import LoopTaskRequester
from task_tracker.get_task import GetTaskList
from task_tracker.task_tracker import TaskTracker

        
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
                        default=8000)
    args = parser.parse_args(argv[1:])
    task_requestor = LoopTaskRequester(args.start, 
                                       args.finish, 
                                       args.num_loops, 
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
    while(not task_tracker.task_completed and not task_tracker.task_failed):
        time.sleep(0.1)
        print('waiting for task')
    task_tracker.join()

if __name__ == '__main__':
    main(argv=sys.argv)

