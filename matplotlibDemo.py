import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

plt.show()

mca_std_list = ["Suraj", "Manoj", "Ramesh", "Shyam"]
mca_std_marks = [98, 45,56,78]

plt.bar(mca_std_list,mca_std_marks,label = 'MCA')
plt.title('MCA Results')
plt.xlabel('MCA Students')
plt.ylabel('MCA Marks Obtained')
plt.legend()
plt.show()
