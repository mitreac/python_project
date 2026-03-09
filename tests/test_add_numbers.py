import sys 
import os
from cm_pkg import module1


def test_addn_pos():
	assert module1.add_numbers(2,5) == 7, "Adding 2 and 5 should result in 7"

def test_multiplication():
	assert module1.multiply_numbers(2,5) == 10, "Multiplying 2 and 5 should result in 10"


cd = os.path.dirname(os.getcwd())
ccd = os.path.join(cd, "cm_pkg")
print(ccd)
sys.path.insert(0, ccd) 

