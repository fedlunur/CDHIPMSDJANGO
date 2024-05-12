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
   
  # path('api/taskmembers/', TaskMemberListCreateAPIView.as_view(), name='taskmember-list-create'),
  path('api/taskchecklist/', TaskCheckListCreateAPIView.as_view(), name='taskchecklist-create'),
  path('api/taskchecklist/<int:pk>/', Task_CheckListRetrieveUpdateDestroy.as_view(), name='taskchecklist-detail'),

  path('api/taskmembers/', TaskMemberListCreateAPIView.as_view(), name='taskmember-create'),
  # path('api/taskmembers/<int:pk>/', Task_MemberRetrieveUpdateDestroy.as_view(), name='taskmember-detail'),
   path('api/taskmembers/<int:assigned_to>/<int:task>/', Task_MemberRetrieveUpdateDestroy.as_view(), name='taskmember-detail'),


]
 






 