from csv_reader import reader
import matplotlib.pyplot as plt
import numpy as np

reader = reader.Reader('/Users/AntonioShen/PycharmProjects/MAIS200_Code_Challenge/MAIS200_Code_Challenge')

ds_ownership = reader.get_home_ownership_data()
ds_loan = reader.get_loan_data()

dict = {'id': 'state'}
for i in range(0, len(ds_ownership)):
    dict[ds_ownership[i, 0]] = ds_ownership[i, 1]

mor, mor_c, own, own_c, rent, rent_c = 0, 0, 0, 0, 0, 0
for i in range(0, len(ds_loan)):
    state = dict[str(ds_loan[i, 0])]
    if state == 'MORTGAGE':
        mor_c += 1
        mor += ds_loan[i, 1]
    elif state == 'OWN':
        own_c += 1
        own += ds_loan[i, 1]
    elif state == 'RENT':
        rent_c += 1
        rent += ds_loan[i, 1]

mor_avg = float(mor) / mor_c
own_avg = float(own) / own_c
rent_avg = float(rent) / rent_c

fig, axs = plt.subplots(1, 2)
cols = ['home_ownership', 'loan_amount']
rows = ['0', '1', '2']
text = [['MORTGAGE', mor_avg],
        ['OWN', own_avg],
        ['RENT', rent_avg]]
axs[0].table(cellText=text, rowLabels=rows, colLabels=cols, loc='center')
axs[0].axis('tight')
axs[0].axis('off')

val = [mor_avg, own_avg, rent_avg]
bar = ['MORTGAGE', 'OWN', 'RENT']
x = np.arange(len(bar))
plt.bar(x, val)
plt.xticks(x, bar)
plt.xlabel('Home ownership')
plt.ylabel('Average loan amount ($)')
plt.title('Average loan amounts per home ownership')

plt.show()
