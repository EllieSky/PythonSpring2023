def register(name, dob, ssn = '000-00-0000', age=99.0):
    print(name, ssn, dob, age)

# register(age=21, dob='12/12/2012', name='Bob')
# register('Bob', '12/12/2012', age=33)

def average_test_scores(teacher, subject='math', *scores):
    print(f"Professon {teacher}'s {subject} class: ")
    print(sum(scores)/len(scores))


# average_test_scores('Smith', 'science', 66.8, 99, 100, 99.2, 78, 85, 100, 70)

def registration2(name, phone_number, **info):
    for k, v in info.items():
        print(k,v)

# registration2(phone_number='1234567890', name='Jane', age=41, iq=120, gpa=3.5, gender='female', veteran=False)

def inputs(i1, i2, i3, name, age):
    print(i1, i2, i3)
    print(name, age)

ls = ['a', 'b', 'c', 'r', 'f']
dic = {'name':'Hue', 'age': 68}


inputs(ls[0], ls[1], ls[2], dic.get('name'), dic.get('age'))


inputs(*ls[:3], **dic)


class Bicycle:
    def __init__(self, speed):
        self.speed = speed

    def bike_faster(self):
        self.speed = self.speed + 2

    def bike_slower(self):
        self.speed = self.speed - 2

    def get_how_fast(self):
        return self.speed

    def stop_biking(self):
        self.speed = 0


blue_bike = Bicycle(15)
red_bike = Bicycle(0)
yellow_bike = Bicycle(10)


blue_bike.bike_faster()
yellow_bike.bike_faster()
yellow_bike.stop_biking()
blue_bike.bike_faster()
blue_bike.bike_faster()
yellow_bike.bike_faster()
blue_bike.bike_slower()
print(f'The bike is going {blue_bike.get_how_fast()}km per hour')
blue_bike.stop_biking()
print(f'The blue bike is going {blue_bike.get_how_fast()}km per hour')
print(f'The red bike is going {red_bike.get_how_fast()}km per hour')
print(f'The yellow bike is going {yellow_bike.get_how_fast()}km per hour')


