def ipsBetween(start_ip, end_ip):
  arps = [range(int(start_ip),int(end_ip)] 
  def padding(s):
    return s.zfill(3)

  arps = [".".join(list(map(padding, x.split(".")))) for x in arps]
  start_ip = ".".join(list(map(padding, start_ip.split("."))))
  end_ip   = ".".join(list(map(padding, end_ip.split("."))))

  print(sum(start_ip <= x <= end_ip for x in arps))
  
  def find_lt(a, x):
    i = bisect.bisect_right(a, x)
    if i:
        return i - 1
    else:
        return 0

  def find_gt(a, x):
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return i
    else:
        return i

  arps.sort()
  print(find_gt(arps, end_ip) - find_lt(arps, start_ip))

ipsBetween(start_ip = input("masukan alamat ip :"), end_ip = input("masukan alamat Ip akhir :"))