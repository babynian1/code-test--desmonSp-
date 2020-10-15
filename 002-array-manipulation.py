
def sumArray(d,d1):
  data1 = []
  data2 = []
  for i in range(0, d): 
    ele = int(input("Masukan Nilai " )) 
    data1.append(ele)

  for a in range(0,d1):
    tmbh = int(input("Masukan Nilai "))
    data2.append(tmbh)

  jmlh = arr.array('i', data1)
  jmlh = arr.array('i', data2)

  print(sum(jmlh[1:d],jmlh1[1:d1]))


sumArray(d = int(input("Masukan Data 1 : ")), d1=int(input("Masukan Data 2 : ")))