from django.db import models

# Create your models here.

#task name , date , status ,

class Tasks(models.Model):
    task_name=models.CharField(max_length=200)
    date=models.CharField(max_length=20)
    status=models.CharField(max_length=60)
#insert into tasks values(bill payment,12/2/20,Not completed)
#this is django ORM
#ob = Tasks(task_name='bill payment',date='16/2/21',status='not completed')
#ob.save()
#tasks=Tasks.objects.all()

    def __str__(self): #this is standard.You should always put this
        return self.task_name