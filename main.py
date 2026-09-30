import read_entry_data_from_file as rf

filepath = "dane_AG/low-dimensional/f1_l-d_kp_10_269"

backpack_data = rf.BackpackItems(filepath)


print(backpack_data.item_value)
print(backpack_data.item_size)