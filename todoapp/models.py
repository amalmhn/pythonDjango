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
#tasks=Tasks.objects.all() #this is an orm query to get the details inside the db
    #if it is all you need to use the for loop
#tasks = Tasks.objects.get(id=1/task_name='billpayment')
    #if it is get you can print that directly..eg.. tasks.task_name
    def __str__(self): #this is standard.You should always put this to print the object or hexadecimel
        return self.task_name


