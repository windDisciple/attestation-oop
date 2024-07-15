class ComplexNumber:  
    def __init__(self, real, imaginary):  
        self.real = real  
        self.imaginary = imaginary  

    def add(self, other):  
        new_real = self.real + other.real  
        new_imaginary = self.imaginary + other.imaginary  
        return ComplexNumber(new_real, new_imaginary)  

    def multiply(self, other):  
        new_real = self.real * other.real - self.imaginary * other.imaginary  
        new_imaginary = self.real * other.imaginary + self.imaginary * other.real  
        return ComplexNumber(new_real, new_imaginary)  

    def divide(self, other):  
        denominator = other.real * other.real + other.imaginary * other.imaginary  
        new_real = (self.real * other.real + self.imaginary * other.imaginary) / denominator  
        new_imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator  
        return ComplexNumber(new_real, new_imaginary)