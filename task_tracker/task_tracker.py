import time
import json
from .get_task import GetTaskList

class TaskTracker():
    def __init__(self,
                task_requester,
                get_task_list: GetTaskList,
                callback):
        self.task_requester = task_requester
        self.get_task_list = get_task_list
        self.task_id = None
        self.task_completed = False
        self.task_failed = False
        self.callback = callback
    
    def completed_task_cb(self):
        # do something
        print("Executing complete task callback")
        self.callback()
        return

    def wait_for_task(self):
        task_list_json = json.loads(self.get_task_list.get_task_list().text)
        for task in task_list_json:
            if task['task_id'] == self.task_id:
                if task['state'] == 'Completed':
                    print(f"Task of task id {self.task_id} completed!")
                    self.task_completed = True
                    return
                elif task['state'] == 'Failed':
                    print(f"Task of task id {self.task_id} failed!")
                    self.task_failed = True
                    return
                else:
                    print(f"Waiting for task of task id: {self.task_id} to complete")
                    return
        print(f"Task of task id: {self.task_id} not in task list!")
            

    def execute_task(self):
        resp = json.loads(self.task_requester.post_request().text)
        err_msg = resp["error_msg"]
        if (err_msg != ""):
            print("Error dispatching task!")
            return err_msg
        self.task_id = resp["task_id"]
        return err_msg
    
    # TODO: Return true or false depending if the task failed
    def start(self):
        err_msg = self.execute_task()
        if (err_msg!= ""):
            print(f"Error message: {err_msg}")
            return False
        while (not self.task_completed and not self.task_failed):
            self.wait_for_task()
            time.sleep(0.2)
        if self.task_completed:
            self.completed_task_cb()
            print("Task completed and exiting loop!")
            return True
        elif self.task_failed:
            print("Task failed and exiting loop!")
            return False
        