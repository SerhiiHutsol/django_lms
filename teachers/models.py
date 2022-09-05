from os import major
from django.db import models
from faker import Faker

class Teachers1(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    experience= models.PositiveIntegerField()
    majors= models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name} : Experience {self.experience} year for major {self.majors} '
    
    @staticmethod
    def gen_teachers(cnt=3):
        f = Faker()
        for _ in range(cnt):
            teacher= Teachers1(first_name = f.first_name(), last_name=f.last_name(), experience= f.random_int(min=3,max=15),
            majors= f.job())
            
            teacher.save()
        
