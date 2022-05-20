
from operator import truediv


def primo(n:int) -> True:
    for i in range(2,n):
        if n%i==0:
            print("no es primo")
            return False
        print("es primo")
        return True

if __name__ == '__main__':
    primo(7)
    