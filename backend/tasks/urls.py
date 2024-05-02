from django.contrib import admin

from tasks.views import *
from django.urls import path,include






urlpatterns = [
  path('api/activitylist/', Activity_listListCreate.as_view(), name='activity-list-create'),
  path('api/activitylist/<int:pk>/', Activity_listRetrieveUpdateDestroy.as_view(), name='activitylist-detail'),
  path('api/taskslist/byactivity/<int:activity_id>/', TaskListByActivity.as_view(), name='task-list-by-activity'),

  path('api/tasklist/', Task_cardListCreate.as_view(), name='task-list-create'),
  path('api/tasklist/<int:pk>/',Task_cardRetrieveUpdateDestroy.as_view(), name='tasklist-detail'),
  path('api/taskslist/byactivity/<int:activity_id>/', TaskListByActivity.as_view(), name='task-list-by-activity'),
   
  path('api/taskmembers/', TaskMemberListCreateAPIView.as_view(), name='task-member-list-create'),


]
 






 