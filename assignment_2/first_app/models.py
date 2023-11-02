from django.db import models

# Create your models here.
class TodoTaskModel(models.Model):
    add_status=(('incomplete','incomplete'),
                ('complete','complete'),
                )
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=60)
    status=models.CharField(max_length=20,choices=add_status)