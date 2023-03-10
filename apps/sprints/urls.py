from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.sprints.views import ProjectView, ProjectAssigneeView, SprintView, TaskView

router = DefaultRouter()
router.register('project', ProjectView)
router.register('project-assignee', ProjectAssigneeView)
router.register('sprint', SprintView)
router.register('task', TaskView)


urlpatterns = [
    path('', include(router.urls)),
]