class EntryData:
    def __init__(self, filepath):
        self.filepath = filepath

       
        self.backpack_items_list = []
    

class BackpackItems:
    def __init__(self, filepath):
        self.filepath = filepath

        self.bakcpack_capacity = self.read_file(0)
        self.items_amout = 1

        self.item_id = 1
        #self.item_value = self.read_file(self.item_id)
        self.item_size = 1

    def read_file(self,id):
        with open(self.filepath, "r") as f:
            line = f.read().split("\n")
            print(type(line[id])) # int(line[1])
            print(line[id])

