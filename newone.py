# class Parent:
#     def __init__(self,msg):
#         self.msg = msg
#     def sample(self):
#         return self.msg
# class Child(Parent):
#     def child_sample(self):
#         return "sample child class"
# print("Call parent class")
# obj = Parent("calling parent method")
# print(obj.sample())
# print("call child class method")
# obj1=Child("Calling child method")
# print(obj1.child_sample())
# print(obj1.sample())

class College:
    def __init__(self, name,age,gender,role):
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role
class Staff(College):
    def attendance_sheet(self, present,reason=None):
        if present == 'no':
            print('{} is Absent and the reason is {} '.format(self.name,reason))
        else:
            print('this{}is present'.format(self.name))
obj = College('jhansi','24','Female','Student')
# print(str(obj.name))
obj1 = Staff('jhansi','24','Female','Student')
obj1.attendance_sheet('no', 'not feeling well')


