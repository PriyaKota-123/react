#abstraction method

from abc import ABC,abstractmethod
@abstractmethod
class boy(ABC):
    def girl(self):
        pass
    def girl1(girl):
        print("name of girl")
class B(boy):
    def girl3(self):
        print("name of girl3")
class C(boy):
    def girl4(self):
        print("name of girl4")
b=B()
b.girl3()
c=C()
c.girl4()

#interface

from abc import ABC,abstractmethod
@abstractmethod
class son(ABC):
    def s1(self):
        pass
    def s2(s1):
        pass

