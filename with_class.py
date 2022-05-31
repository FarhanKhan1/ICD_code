class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def Show_list(self):
        if self.head == None:
            print('LIST IS EMPTY')
        else:

            h = self.head
            while h is not None:
                print(h.data)
                h = h.next

    def add_in_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    

L1 = Linked_List()
# L1.add_in_start(10)
# L1.add_in_start(20)
# L1.add_in_start(30)
# L1.add_in_start(40)

L1.Show_list()

