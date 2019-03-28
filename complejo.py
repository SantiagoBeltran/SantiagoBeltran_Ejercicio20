import numpy as np

class Complejo():
    def __init__(self, x, y):
        self.real=x
        self.imaginario=y
        self.norma=np.sqrt(x**2+y**2)
    def conjugado(self):
        self.imaginario=-self.imaginario
    def calcula_norma(self):
        self.norma=np.sqrt(self.real**2+self.imaginario**2)
    def mult(self,y):
        a=(self.real*y.real-self.imaginario*y.imaginario)
        b=self.real*y.imaginario+y.real*self.imaginario
        p=Complejo(a,b)
        return p
    def pow(self, n):
        t=self
        for i in range(n-1):
            t= t.mult(self)
        return t