# list = ['Gota382481','Jagatpur382470','Ranip382480','Sola382425'] In this list 
# saprate 'area' and 'pincode ' and output in two dimensional list

original_list = ['Gota382481', 'Jagatpur382470', 'Ranip382480', 'Sola382425']
two_dimensional_list = []

for item in original_list:
    area = item[:-6]
    pincode = item[-6:]  
    two_dimensional_list.append([area, pincode])
print("Two-dimensional list:", two_dimensional_list)
