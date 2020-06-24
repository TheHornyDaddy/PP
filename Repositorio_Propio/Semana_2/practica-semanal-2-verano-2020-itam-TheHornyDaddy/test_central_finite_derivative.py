import math
from pytest import approx

from central_finite_derivative import approx_first_derivative, \
                                      approx_second_derivative

f = math.asin
x = 0.5
h = 1e-6
first_approx_der = approx_first_derivative(f, x, h)
first_der_obj = 1/math.sqrt(1-x**2)
h = 1e-4
second_approx_der = approx_second_derivative(f, x, h)
second_der_obj = x/(1-x**2)**(3/2)
h = 1e-6
second_approx_der_alternative = approx_second_derivative(f, x, h)

def test_aprox_primera_derivada():
     assert first_approx_der == approx(first_der_obj)
    
    
def test_aprox_segunda_derivada():
    assert second_approx_der == approx(second_der_obj)
    
def test_aprox_segunda_derivada_alternative():
    assert second_approx_der_alternative == approx(second_der_obj, rel=1e-4,abs=1e-4)   
    
