class NoDuplicates:

    list_item = []

    def __init__(self):
        self.list = []

    def __call__(self, new_items):

        for c in new_items:
            if c not in self.list:
                self.list.append(c)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list.list)
my_no_dup_list(['keyboard','mouse'])
print(my_no_dup_list.list)
 
my_no_dup_list(['keyboard','mouse','pendrive'])
print(my_no_dup_list.list)
 
my_no_dup_list(['charger','pendrive'])
print(my_no_dup_list.list)