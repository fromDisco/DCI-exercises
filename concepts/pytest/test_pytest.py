import os
import pytest
from app import func_val_error, func_type_error

# install pytest if not installed
check = os.popen("pip list | grep pytest")
if "pytest" not in check.read():
    os.system("pip install pytest")

import pytest

# class has to be prefixed with Test*
class TestClass:
    def test_some_primes(self):
        # is 37 in the set of prime numbers?
        assert 37 in {
            num
            for num in range(2, 50)
            if not any(num % div == 0 for div in range(2, num))
        }
        # calculate prime numbers
        # if any of the num % divs == 0, 
        # num is not an prime numbe== 0, 
        return {
            num
            for num in range(2, 50)
            if not any(num % div == 0 for div in range(2, num))
        }

    #print(test_some_primes())

    def test_func_val_error(self):
        with pytest.raises(ValueError):
            func_val_error()

    def test_func_type_error(self):
        with pytest.raises(TypeError):
            func_type_error()