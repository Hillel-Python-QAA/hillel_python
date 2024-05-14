import abc
from abc import ABC


class Animal:
    def method(self):
        ...


class MultiInheritance(Animal, ABC):
    def method(self):
        ...


multiinheritance = MultiInheritance()
print(MultiInheritance.mro())


multiinheritance.method()


class Parent1:
    def method1(self):
        print('Call method1 from Parent1')


class Parent2:
    def method2(self):
        print('Call method2 from Parent2')


class Child(Parent1, Parent2):
    pass


child = Child()
child.method1()
child.method2()


class Mama:
    common_field = 'Mama\'s common value'


class Dad:
    common_field = 'Dad\'s common value'


class Parent(Mama, Dad):
    pass


class Kid(Parent):
    def access_common_field(self):
        mamas_field = super().Mama.common_field
        dads_field = super().Dad.common_field

        print(mamas_field)
        print(dads_field)


kid = Kid()
print(Kid.mro())
print(kid.common_field)
kid.access_common_field()
