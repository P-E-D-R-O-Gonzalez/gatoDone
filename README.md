gatoDone: https://test.pypi.org/project/gatoDone-PedroGonzalez/0.0.1/

Make your program play cat sounds at strategic points in your program
To help with:

- debugging
- code completion
- when you hit an error
- whenever you want

You can use it multiple times in the program thanks to gatoLoop function, just run it a different x value so it remains unique

# install: pip install -i https://test.pypi.org/simple/ gatoDone-PedroGonzalez==0.0.1

# example code
from gatoDone import gatoDone

for i in range(1000000):
    print(i+1)
gatoDone()

