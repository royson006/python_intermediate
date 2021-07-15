def divisors(num):
    divisor=[]
    for i in range (1, num+1):
        if num % i ==0:
            divisor.append(i)
    return divisor


def run():
    correct=False
    while correct==False:
        try:
            num= int(input("Ingresa un numero: "))
            if(num<0):
                raise ValueError("Ingrese solo numeros positivos")

            print(divisors(num))
            print("Programa terminado")
            correct=True
        except ValueError as nn:
            correct=False
            print("Ingresa un dato numerico positivo",nn)


if(__name__=="__main__"):
    run()