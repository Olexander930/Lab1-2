a=0
b=1
for i in range(0,20):
  if i%2==0:
    a+=i
  elif i%2 != 0:
    b*=i
print("Сума усіх парних чисел від 0 до 20:",a)
print("\nДобуток усіх непарних чисел від 0 до 20:",b)
