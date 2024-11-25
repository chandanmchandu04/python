import pandas as pd
import matplotlib.pyplot as pyt

salary_data = {
    'Chandan': 90000,
    'sanajy': 96000,
    'Tharun': 100000,
    'charanraj': 10000000,
}
salaries = pd.Series(salary_data)
print(salaries) 

salaries.plot()
pyt.show()
