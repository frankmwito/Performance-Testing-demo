from locust import User, TaskSet, task, between


class MyTaskSet(TaskSet):
    @task(3)
    def web(self):
        print("I am a web user1")

    @task(1)
    def mobile(self):
        print("I am a mobile1")

    @task(2)
    def enter_nested_task_set_1(self):
        print("Entering nested TaskSet 1")
        self.schedule_task(Mytaskset1)  # Move to next TaskSet


class Mytaskset1(TaskSet):
    @task(3)
    def web1(self):
        print("I am a web user2")

    @task(1)
    def mobile1(self):
        print("I am a mobile2")

    @task(2)
    def enter_nested_task_set_2(self):
        print("Entering nested TaskSet 2")
        self.schedule_task(MytaskSet2)  # Move to the next nested TaskSet

    @task(1)
    def stop_nested_1(self):
        print("Stopping nested TaskSet 1")
        self.interrupt()  # Exit back to parent TaskSet


class MytaskSet2(TaskSet):
    @task(3)
    def web2(self):
        print("I am a web user3")

    @task(1)
    def mobile2(self):
        print("I am a mobile3")

    @task(1)
    def stop_nested_2(self):
        print("Stopping nested TaskSet 2")
        self.interrupt()  # Exit back to parent TaskSet


class MyWebUser(User):
    wait_time = between(1, 2)
    tasks = [MyTaskSet]  # Assign the top-level TaskSet to the user