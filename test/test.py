from faker import Faker

class Student():

    def gen_students(cnt=10):
        fk = Faker()
        lst=[]
        for _ in range(cnt):
            st = fk.first_name()
            # first_name = fk.first_name(),
            # last_name = fk.last_name(),
            # age = fk.random_int(min=18, max=45)
            
            lst.append(st)
        return lst

f = Student.gen_students(40)
print(f)
# Student.gen_students(20)