#Matplotlib – Histogram
import matplotlib.pyplot as plt
marks = [70, 80, 90, 60, 85]
plt.hist(marks)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

#Scatter Plot
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

#Seaborn – Heatmap (Client Dashboard)
import seaborn as sns
import pandas as pd

data = {
    'Maths': [80, 90, 85],
    'Science': [75, 88, 92],
    'English': [78, 85, 80]
}

df = pd.DataFrame(data)
sns.heatmap(df, annot=True)
plt.title("Student Performance Heatmap")
plt.show()

