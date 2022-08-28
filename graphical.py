import matplotlib.pyplot as plt
import fibo

li = fibo.getMod(5,64)
print(li)

x_axis = [x for x in range(1,len(li)+1)]
print(x_axis)
plt.plot(x_axis, li, markersize = 12,label =f'5 pissano')
plt.show()