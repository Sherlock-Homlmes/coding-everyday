import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

# create data
data_list = [
['Ngày 1', 10, 20], 
['Ngày 2', 20, 25], 
['Ngày 3', 12, 15],
['Ngày 4', 10, 18], 
['Ngày 5', 20, 25], 
['Ngày 6', 12, 15],
['Hôm nay', 10, 18]
]

df = pd.DataFrame(data_list,
                  columns=['Ngày', 'Tuần này', 'Tuần trước'])
# view data
#print(df)
  
# plot data in stack manner of bar type
df.plot(kind='bar', stacked=True,
        title='7 ngày qua',xlabel='Ngày',ylabel="Giờ học"
        )

#plt.show()
plt.savefig('foo.png', bbox_inches='tight', transparent=True)


def delete_file():
        import os
        if os.path.exists("demofile.txt"):
                os.remove("demofile.txt")
