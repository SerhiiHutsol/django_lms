from faker import Faker

class Student():

    def gen_students(cnt=10):
        fk = Faker()
        lst=[]
        for _ in range(cnt):
            st = fk.bothify(text='??-###')

            # first_name = fk.first_name(),
            # last_name = fk.last_name(),
            # age = fk.random_int(min=18, max=45)
            
            lst.append(st)
        return lst

f = Student.gen_students(2)
print(f)
# state_1 = {'coord_x': 5.573, 'speed': 10, 'fuel': 0.83}
# for i in state_1.values():
#     print(i)

# print(state_1.values())
# Student.gen_students(20)