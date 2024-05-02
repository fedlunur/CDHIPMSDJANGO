from django.db import models
from api.models  import Profile,User
from projects.models import Project
from django.utils.timezone  import datetime
from api.models import TeamMember



class Activity_list(models.Model):

    list_title=models.CharField(max_length=150)
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.list_title   

class Task_card(models.Model):
    
    duedatereminder_CHOICES = [
        ('1', 'remind 1 days left'),
        ('2', 'remind 2 days left'),
        ('3', 'remind 3 days left'),
    ]
    status_choice =  [
         ('0', 'normal'),
          ('1', 'low'),
          ('2', 'high'),
       
           ]
   
   
    task_name = models.CharField(max_length=100 )
    description = models.TextField(blank=True,null=True)
    due_date = models.DateField(blank=True, null=True)
    status= models.TextField( choices=status_choice,default='0',null=True)
    activity=models.ForeignKey(Activity_list, on_delete=models.CASCADE)
    due_date_reminder=models.CharField(max_length=1, choices=duedatereminder_CHOICES,null=True)
    cover=models.CharField(max_length=200,blank=True,null=True)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task_name
    
    
# class Comment(models.Model):ss
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.user.username} - {self.text[:20]}"

#    created_at = models.DateTimeField(auto_now_add=True)

class Task_Member(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    task = models.ForeignKey(Task_card, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ['assigned_to', 'task']
    def __str__(self) -> str:
        return f"{self.task.task_name}  "

# class TaskAssignment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     task_member = models.ForeignKey(Task_Member, on_delete=models.CASCADE)
    
#     def __str__(self) -> str:
     
#         return f"{self.task_member.task} ===> {self.user.first_name}  "

        
#     class Meta:
#         unique_together = ['user', 'task_member']

class Task_CheckList(models.Model):
   name =models.CharField(max_length=100 )
   status = models.BooleanField(default=False)
   task=models.ForeignKey(Task_card, on_delete=models.CASCADE,null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   def __str__(self) -> str:
        return self.name + self.task


class TaskCard_Attachment (models.Model):
   name =models.CharField(max_length=100 )
   task_card= models.ForeignKey(Task_card, on_delete=models.CASCADE)
   path=models.FileField(upload_to="project_files" )
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
#    created_at = models.DateTimeField( auto_now_add=True, default=datetime.now)
