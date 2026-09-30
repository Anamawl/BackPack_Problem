import read_entry_data_from_file as rf

filepath = "dane_AG/low-dimensional/f1_l-d_kp_10_269"

# data = rf.EntryData(filepath)
# print(data.bakcpack_capacity)
# print(data.items_amout)
# print(data.backpack_items_list)

backpack_items = rf.BackpackItems(filepath)
print(backpack_items.bakcpack_capacity[0])
#print(backpack_items.item_value)
#test vvs