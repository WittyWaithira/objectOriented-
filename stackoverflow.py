class User:

    def __init__(self,first,second,id):
        self.first=first
        self.second=second
        self.id=id
        self.email=first+'.'+ second+'@gmail.com'

    def fullname(self):
        return '{} {}' .format(self.first,self.second)

#inheritance
class Administrator(User):

    def __init__(self,first,second,id,users=None):
     super().__init__(first,second,id)
     if users is None:
         self.users=[]
     else:
         self.users = users

    def add_user(self,userA):
        if userA not in self.users:
            self.users.append(userA)

    def remove_user(self,userA):
        if userA in self.users:
            self.users.remove(userA)
    def print_user(self):
        for userA in self.users:
            print('--->',userA.fullname())



user_1=User('Jerusha','Waithira',342)
user_2=User('Rachel','Mandi',349)


admin_1= Administrator('Mitch','Mwangi',341,[user_1])



print(admin_1.email)
admin_1.add_user(user_2)
admin_1.remove_user(user_1)

admin_1.print_user()
