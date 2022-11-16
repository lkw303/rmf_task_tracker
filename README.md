# TaskTracker

## Introduction
The task tracking class allows for users to create instance of the `TaskTracker` and pass in the corresponding `TaskRequester` as well as their desired callback function. The `TaskTracker` would dispatch the task and observe the state of the task by continuously sending GET requests to the RMF API server querying the task states. Upon observing that the task state is completed, the `TaskTracker` class would execute the callback function that user had declared.

## Refactoring
There should be a generic abstract `TaskRequester` class that can be inherited from. The class should implement the `get_url()` and the `post_request` function.
