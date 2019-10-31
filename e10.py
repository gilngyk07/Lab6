class Pet:
   def __init__(self,fur,breed,call):
      self.f = fur
      self.b = breed
      self.c = call
   def eat(self):
      if self.c == 'Meow':
         print("The pet is eating fish,",self.c)
      elif self.c=='woof':
          print("The pet is chewing bone,",self.c)
class Cat(Pet):
   def __init__(self,fur,breed):
      Pet.__init__(self,fur,breed,'Meow')
class dog(Pet):
     def __init__(self,fur,breed):
        Pet.__init__(self,fur,breed,'woof')
mykitty = Cat('White','siam')
mykitty.eat()
myLassie = dog('white','collar')
myLassie.eat()
