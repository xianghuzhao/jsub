import datetime

class Task:
    def __init__(self, repo, data={}):
        self.__repo = repo
        self.data = data
        if 'created_at' not in self.data:
            self.data['created_at'] = datetime.datetime.utcnow().isoformat()

    def save(self):
        self.data['updated_at'] = datetime.datetime.utcnow().isoformat()
        self.__repo.save_task(self.data)


class TaskPool:
    def __init__(self, repo):
        self.__repo = repo

    def create(self, props={}):
        task = Task(self.__repo, {'props': props})
        task.save()
        return task

    def all(self):
        tasks = []
        all_data = self.__repo.all_task_data()
        for data in all_data:
            tasks.append(Task(self.__repo, data))
        return tasks

    def find(self, task_id):
        data = self.__repo.task_data(task_id)
        return Task(self.__repo, data)

class Job:
    def __init__(self, repo, props={}):
        pass