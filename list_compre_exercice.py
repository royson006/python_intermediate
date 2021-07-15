def run():

  multiples=[i for i in range(1,10000) if (i%4 == 0 and i% 3 == 0 and i%9 == 0)]
  print(multiples)


if(__name__=='__main__'):
  run()