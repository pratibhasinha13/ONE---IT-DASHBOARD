import matplotlib.pyplot as plt
import csv

x = []
y = []
with open("C:\\Users\\Pratibha Sinha\\Downloads\\data.csv", 'r') as csvfile:
        plots = csv.reader(csvfile,delimiter =',')
        for row in plots:
                x.append((row[0]))
                y.append((row[7]))

plt.plot(x,y ,label = 'loaded from file!')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('TATA STEEL')
plt.show()
