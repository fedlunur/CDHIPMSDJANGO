from rest_framework import serializers
from .models import *
from api.serializer import UserSerializer


class Activity_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model =Activity_list
        # fields = ['project_name','description','start_date','end_date']
        fields = '__all__'
class Activity_ListSerializer(serializers.ModelSerializer):
    class Meta:
        model =Activity_list
        # fields = ['project_name','description','start_date','end_date']
        fields = '__all__'
 
class TaskCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_card
        # fields = ['task_name', 'description', 'due_date', 'status', 'activity', 'due_date_reminder', 'cover']   
        fields = '__all__'
        

from .models import Task_CheckList

class TaskCheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_CheckList
        fields = '__all__'      
class TaskMemberSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer()
    task = TaskCardSerializer()

    class Meta:
        model = Task_Member
        fields = '__all__'
     