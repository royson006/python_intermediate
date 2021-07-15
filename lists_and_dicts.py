def run():
  my_list=[1,"Hello",True,4.5]
  my_dict={"firstname":"Rodrigo","lastname":"Lopez"}
  super_list=[
    {"firstname":"Rodrigo","lastname":"Lopez"},
    {"firstname":"Miguel","lastname":"Torres"},
    {"firstname":"Pepe","lastname":"Rodelo"},
    {"firstname":"Susana","lastname":"Martinez"},
    {"firstname":"Jose","lastname":"Garcia"}
  ]
  super_dic = {
    "natural_nums":[1,2,3,4,5],
    "integer_nums":[-1,-2,0,1,2],
    "floating_nums":[1.1,5.6,0.6,1.8,8.6]
  }

  for key,value in super_dic.items():
    print(key," - ",value)

  for dic in super_list:
    print(dic.items())



if(__name__=='__main__'):
  run()