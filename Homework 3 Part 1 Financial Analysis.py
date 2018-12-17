
#Homework #3 Part 1 Financial Analysis

fn = 'Resources/budget_data.csv'
f = open(fn)
contents = f.read()
f.close()

# split contents on \n
lines = contents.split('\n')
#print(lines)

# number of months
num_of_months = len(lines)-1
print('Number of months:', num_of_months)
print()

# total net P/L
lines = lines[1:]

total_pl = 0
pl_list = []
dates = []
for line in lines:
    if line == '':
        continue  # skip this line
    items = line.split(',')
    date = items[0]
    dates.append(date)
    pl_string = items[1]
    pl = int(pl_string)
    pl_list.append(pl)
    total_pl = total_pl + pl
    print(pl)

print('Total PL =', total_pl)
print()

# drop last line if empty
if lines[-1] == 0:
    del(lines[-1])

# avg PL change
changes = []
largest_profit_change = 0
lpc_month = None
largest_loss_change = 0
llc_month = None
for index in range(len(pl_list)-1):
    chg = pl_list[index+1] - pl_list[index]
    print(pl_list[index], pl_list[index+1], chg)
    #largest profit?
    if chg > largest_profit_change:
        largest_profit_change = chg
        lpc_month = dates[index+1]
    if chg < largest_loss_change:
        largest_loss_change = chg
        llc_month = dates[index+1]
    changes.append(chg)

avg_change = sum(changes) / len(changes)
print('Avg PL Change', avg_change)
print('Greatest Increase in Profits: '
      +lpc_month+ ' (' + str(largest_profit_change) + ')')
print('Greatest Decrease in Profits: '
      +llc_month+ ' (' + str(largest_loss_change) + ')')


Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
