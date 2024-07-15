from complex_number import ComplexNumber  

class Calculator:  
    def add(self, a, b):  
        pass  

    def multiply(self, a, b):  
        pass  

    def divide(self, a, b):  
        pass  

class ComplexCalculator(Calculator):  
    def add(self, a, b):  
        return a.add(b)  

    def multiply(self, a, b):  
        return a.multiply(b)  

    def divide(self, a, b):  
        return a.divide(b)