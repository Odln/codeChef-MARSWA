# cook your dish here
t=int(input())
for i in range(0,t):
  f=(input())
  f=f.split(" ")
  s1=(int)(f[0])
  s=int(f[1])
  t1=(int)(f[2])
  t2=(int)(f[3])
  x=int(input())
  a=(2**(x-t2))*s
  print(int(a))