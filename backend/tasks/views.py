from rest_framework import generics ,viewsets,status
from .models import Activity_list,Task_card,Task_CheckList,Task_Member,User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404


from .serializers import Activity_ListSerializer,TaskCardSerializer,TaskCheckListSerializer,TaskMemberSerializer

class Activity_listListCreate(generics.ListCreateAPIView):
    queryset = Activity_list.objects.all()
    serializer_class = Activity_ListSerializer

class Activity_listRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity_list.objects.all()
    serializer_class = Activity_ListSerializer
    
    
class Task_cardListCreate(generics.ListCreateAPIView):
    queryset = Task_card.objects.all()
    serializer_class = TaskCardSerializer

class Task_cardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     queryset = Task_card.objects.all()
     serializer_class = TaskCardSerializer
     
     
# class Activity_listRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Activity_list.objects.all()
#     serializer_class = Activity_ListSerializer
     

     
class Task_CheckListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     queryset = Task_CheckList.objects.all()
     serializer_class = TaskCheckListSerializer     
         
class TaskCheckListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task_CheckList.objects.all()
    serializer_class = TaskCheckListSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        task_id = self.request.query_params.get('task', None)
        if task_id is not None:
            queryset = queryset.filter(task=task_id)
        return queryset
    

class TaskListByActivity(generics.ListAPIView):
    serializer_class = TaskCardSerializer
   
    def get_queryset(self):
        activity_id = self.kwargs['activity_id']
        # print(f" the incoming activity is is {activity_id}")
        return Task_card.objects.filter(activity_id=activity_id)     






# task and Members manage 
     
class Task_MemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
     queryset = Task_Member.objects.all()
     serializer_class = TaskMemberSerializer     
     def delete(self, request, *args, **kwargs):
        assigned_to = kwargs.get('assigned_to')
        task_id = kwargs.get('task')
        print(" ##### At the back end "+str(assigned_to) + " task_id"+str(task_id))
        if not assigned_to or not task_id:
            return Response({'error': 'Both assigned_to and task parameters are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            task_member = Task_Member.objects.get(assigned_to=assigned_to, task=task_id)
            task_member.delete()
            print("after Delete ")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task_Member.DoesNotExist:
            return Response({'error': 'Task_Member not found'}, status=status.HTTP_404_NOT_FOUND) 
class TaskMemberListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task_Member.objects.all()
    serializer_class = TaskMemberSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        task_id = self.request.query_params.get('task', None)
        if task_id is not None:
            queryset = queryset.filter(task=task_id)
        return queryset
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     task_id = self.request.query_params.get('task', None)
    #     if task_id is not None:
    #         queryset = queryset.filter(task=task_id)
    #     return queryset

# class TaskMemberListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Task_Member.objects.all()
#     serializer_class = TaskMemberSerializer
    
#     def create(self, request, *args, **kwargs):
#         assigned_to_ids = request.data.get('assigned_users', [])
#         task_id = request.data.get('task')
#         # try:
#         #     task_obj = Task_card.objects.get(pk=task_id)
#         # except Task_card.DoesNotExist:
#         #     return Response({"error": "Task does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        
#         for user_id in assigned_to_ids:
#             print("@@@@@ user "+ str(user_id) +" and task id "+ str(task_id))
#             task_member_data = {
#                 'assigned_to': user_id,  # Assuming 'assigned_to' field is ForeignKey to User model
#                 'task': task_id,
#             }
#             serializer = self.get_serializer(data=task_member_data)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
        
#         return Response({"message": "Task members created successfully."}, status=status.HTTP_201_CREATED)