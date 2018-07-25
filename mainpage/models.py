from django.db import models

class usermodelk1(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    maths=models.IntegerField()
    physics=models.IntegerField()
    english=models.IntegerField()
    computer=models.IntegerField()

    def __str__(self):
        return self.name