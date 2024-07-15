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
    
from abc import ABC, abstractmethod  

class Calculator(ABC):  
    @abstractmethod  
    def add(self, a, b):  
        pass  

    @abstractmethod  
    def multiply(self, a, b):  
        pass  

    @abstractmethod  
    def divide(self, a, b):  
        pass  

class ComplexCalculator(Calculator):  
    def add(self, a, b):  
        return a.add(b)  

    def multiply(self, a, b):  
        return a.multiply(b)  

    def divide(self, a, b):  
        return a.divide(b)
    
import logging  

class CalculatorLogger:  
    def __init__(self):  
        logging.basicConfig(level=logging.INFO)  

    def log(self, message):  
        logging.info(message)

from complex_number import ComplexNumber  
from calculator import ComplexCalculator  
from logger import CalculatorLogger  

logger = CalculatorLogger()  
calculator = ComplexCalculator()  

num1 = ComplexNumber(2, 3)  
num2 = ComplexNumber(1, 4)  

sum_result = calculator.add(num1, num2)  
logger.log(f"Sum: {sum_result.real} + {sum_result.imaginary}i")  

product_result = calculator.multiply(num1, num2)  
logger.log(f"Product: {product_result.real} + {product_result.imaginary}i")  

quotient_result = calculator.divide(num1, num2)  
logger.log(f"Quotient: {quotient_result.real} + {quotient_result.imaginary}i")