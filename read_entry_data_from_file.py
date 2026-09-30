
class BackpackItems:
    def __init__(self, filepath):
        self.filepath = filepath

        self.backpack_capacity = self.read_line(0,0)
        self.amount_of_items_to_choose = self.read_line(0,1)

        self.item_value = self.read_file(0)
        self.item_size = self.read_file(1)

    def read_line(self,id,column):
        with open(self.filepath, "r") as f:

            line = f.read().split("\n")
            
            return int(line[id].split(" ")[column])

    def read_file(self,value_or_size=0): #0 for value, 1 for size 
        with open(self.filepath, "r") as f:
            item_data = []

            for i in f.read().split("\n"):
                item_data.append(i.split(" ")[value_or_size])
            del item_data[0]
                
            return item_data