class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        list = []
        if self.head is None:
            return list
        node = self.head
        while node:
            list.append(node.data)
            node = node.next_node
        return list

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f'{str(node.data)} ->'
            node = node.next_node
        ll_string += 'None'
        print(ll_string)

    """ll = LinkedList()
    node4 = Node('data4',None)
    node3 = Node('data3', node4)
    node2 = Node('data2', node3)
    node1 = Node('data1', node2)
    ll.head = node1
    ll.print_ll()
    data1 -> data2 -> data3 -> data4 -> None
    """

    def insert_beggining(self, data):
        # if the list is empty the same node we insert will be the fisrt and last node
        # so we can take an advantage of that to keep track ofthe last node so we dont have to traverse all the time
        #to add at the end
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        # i give the new node its data and the pointer of the new node will be
        # the head so the head that was before now is the second node
        else:
            new_node = Node(data, self.head)
            # now the new head is the new node
            self.head = new_node

    """ll = LinkedList()
    ll.insert_beggining('data')
    ll.print_ll()
    data -> None

    ll.insert_beggining('not data')
    ll.print_ll()
    not data -> data -> None
    """

    def insert_at_the_end(self, data):
        # if the list is empty insert in the beginning
        if self.head is None:
            self.insert_beggining(data)
            return
        #if there is no last node yet we have to traverse until last node
        # if self.last_node is None:
            # (WELL ALWAYS BE TRACKING THE LAST NODE SO THIS IF WILL NEVER HAPPEN
            # BECAUSE NOW WE ADDED KEEPING TRACK OF THE LAST NODE AS SOON AS WE INSERT IN THE BEGGINING, 
            # WE WONT HAVE TO TRAVERSE)
            # now i take the head an iterate through the next nodes until the next node
            # is None, that way we know it was the last node
            # node = self.head
            # while node.next_node:
                # node = node.next_node
            # we have the last node so the next node to he last it's the one we created
            # node.next_node = Node(data, None)
            # last node is the one we created
            # now we also keep track of the last node so we dont have to traverse anymore
            # self.last_node = node.next_node

        # we aply the same idea without having to traverse
        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

        """ll = LinkedList()
        ll.insert_beggining('beggining')
        ll.insert_beggining('beggining 2')
        ll.insert_at_the_end('end')
        ll.insert_at_the_end('end 2')
        ll.print_ll()
        beggining 2 ->beggining ->end ->end 2 ->None"""

    def get_user_by_id(self,user_id):
        if self.head is None:
            return None
        else:
            node = self.head
            while node:
                if node.data['id'] is int(user_id):
                    return node.data
                else:
                    node = node.next_node
            return None