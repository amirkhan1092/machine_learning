# @auther amirkhan1092
import matplotlib.pyplot as plt

hours = [2, 6, 3, 2, 11]
activity = ['Eat', 'Sleep', 'Ibadat', 'Social Media', 'coding']

color = ['r', 'k', 'g', 'c', 'b']
plt.pie(hours, labels=activity, colors=color, startangle=90,
        autopct='%.1f%%')
plt.show()
