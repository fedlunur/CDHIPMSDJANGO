from rest_framework import generics ,viewsets
from .models import Activity_list,Task_card,Task_CheckList,Task_Member,User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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


class TaskListByActivity(generics.ListAPIView):
    serializer_class = TaskCardSerializer
   
    def get_queryset(self):
        activity_id = self.kwargs['activity_id']
        print(f" the incoming activity is is {activity_id}")
        return Task_card.objects.filter(activity_id=activity_id)     

class TaskMemberListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task_Member.objects.all()
    serializer_class = TaskMemberSerializer
    
    def create(self, request, *args, **kwargs):
        assigned_to_ids = request.data.get('assigned_users', [])
        
        # Create a new Task_Member instance for each assigned user ID
        for user_id in assigned_to_ids:
            task_member_data = {
                'assigned_to': user_id,
                'task': request.data.get('task'),  # Assuming 'task' is also in the request data
            }
            serializer = self.get_serializer(data=task_member_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        
        return Response(status=status.HTTP_201_CREATED)