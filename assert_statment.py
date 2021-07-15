def divisors(num):
    divisor=[]
    for i in range (1, num+1):
        if num % i ==0:
            divisor.append(i)
    return divisor


def run():
    num= input("Ingresa un numero: ")
    assert num.isnumeric(), "Ingresa numero unicamente"
    assert int(num)>0, "Ingresa numero unicamente"
    print(divisors(int(num)))
    print("Programa terminado")



if(__name__=="__main__"):
    run()