# from abc import ABC,abstractmethod

# class person(ABC):
#     @abstractmethod
#     def add(self,x,y):
#         pass
#     @abstractmethod
#     def isPrime(self,n):
#         pass
# class person2(person):
#     def add (self,x,y):
#         return x+y
# class person3(person2):

#     def isPrime (self,n):
#         return True


# ob=person2()
from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    pass
com=computer()
com1=laptop()
com.process()