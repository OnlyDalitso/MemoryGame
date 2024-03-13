import math
def calcAreaofCircle(radius):
    result = 0.0
    pi = math.pi
    result = pi*radius*radius
    return result

def calcPerimeterofCircle(radius):
    result = 0.0
    pi = math.pi
    result = 2*pi*radius
    return result


def main():
    calcAreaofCircle(12)
    calcPerimeterofCircle(12)



    print(calcAreaofCircle(12))
    print(calcPerimeterofCircle(12))
main()
