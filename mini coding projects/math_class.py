"""given integer inva two integer number retun their product and 
if the product is greater than 1000 reurn their sum
Do the exercise using inerited class """

#transpose basic math problem into a simple code
#instead of getting dizy with arguments a,b,c,d use inherit class to override arguments a,b where by 
# attributes from a,b are inherited in the next class, the child class


class x:
    def __init__(self, a,b):
        self.a=a
        self.b=b

    def math(self,a,b):
        if 600>1000:
            return a+b
        else:
            return a*b
p=x(20,30)
print(p.math(20,30))

class y(x):
    def __init__(self,a,b):
        super().__init__(a,b)

        
    def f(self,a,b):
        if 600<1000:
            return a+b
        else:
            return a*b
q=y(30,40)
print(q.f(30,40))










    








