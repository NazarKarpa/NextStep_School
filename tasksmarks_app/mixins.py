from .models import Task, TestTask

class TaskListMixin:
    def get_task_list_context(self, lesson):
        return {'tasks': Task.objects.filter(task_in_lesson=lesson)}

class TaskDetailMixins:
    def get_task_detail_context(self, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            return {'task_detail': task}
        except Task.DoesNotExist:
            return {'task_detail': None}