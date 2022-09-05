from django.db import models
from faker import Faker

class Groups(models.Model):
    name_group = models.CharField(max_length=50)
    people_group = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'Name group: {self.name_group} people in group {self.people_group}'

    @staticmethod
    def gen_group(cnt=5):
        f=Faker()
        for i in range(cnt):
            st = Groups(name_group= f.bothify(text='??-###'), people_group= f.random_int(min=10, max=30))
            
            st.save()
