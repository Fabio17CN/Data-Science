import matplotlib.pyplot as plt

y= [1, 2, 5]
x= [2, 3, 7]

# Titulo
plt.title('Meu primeiro gráfico com python')

# Eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.plot(x,y)
plt.show()