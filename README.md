gatoDone

Make your program play cat sounds at strategic points in your program
To help with:

- debugging
- code completion
- when you hit an error
- whenever you want

You can use it multiple times in the program thanks to gatoLoop function, just run it a different x value so it remains unique

# install: python -m pip install git+https://github.com/P-E-D-R-O-Gonzalez/gatoDone.git
# example code
from gatoDone import gatoDone

for i in range(1000000):
    print(i+1)
gatoDone();

