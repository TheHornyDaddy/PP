import numpy as np
from scipy.integrate import quad
from pytest import approx

from numerical_integration import Tcf, GLf, GHf


#Trapezoidal rule
f = np.sin
a = 0
b = np.pi
n = 10**4
trapezoidal_approx = Tcf(f,a,b,n)
trapezoidal_obj, err = quad(f,a,b)

#Gauss-Legendre
f = lambda t: np.exp(-t**2/2)
a = 0
b = 1
n = 4
GL_approx = GLf(f,a,b,n)
GL_obj, err = quad(f,a,b)

#Gauss-Hermite
sigma = 0.25
mu = 0.15
f1 = lambda t: t
GH1_approx = GHf(f1,mu,sigma)
GH1_obj = 0.15
f2 = lambda t: t**2
GH2_approx = GHf(f2, mu,sigma)
GH2_obj = 0.085

def test_Tcf():
    assert trapezoidal_approx == approx(trapezoidal_obj)
    
def test_GL():
    assert GL_approx == approx(GL_obj)

def test_GH1():
    assert GH1_approx == approx(GH1_obj, abs=1e-4, rel=1e-4)
    
def test_GH2():
    assert GH2_approx == approx(GH2_obj, abs=1e-4, rel=1e-4)   
