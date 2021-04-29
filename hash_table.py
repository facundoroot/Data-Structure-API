class Node:
    #we create a node as always
    def __init__(self, data= None, next_node= None):
        self.data = data 
        self.next_node = next_node

class Data:
    # now the value of the node will have a key and a value inside
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:
    #create the hash table
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        # for the letter in the key transforms to a number
        for i in key:
            hash_value += ord(i)
            #now we take the module so the number will always be smaller than the size
            #of the hash table
            hash_value = (hash_value * ord(i)) % self.table_size
        return hash_value

    def add_key_value(self, key, value):
        # now we create a hashed 
        hashed_key = self.custom_hash(key)
        # the hashed key will be the index of the element of the table we will be adding a node
        # we add through a linked list:
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key,value), None)

    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is not None:
            node = self.hash_table[hashed_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node
            if key == node.data.key:
                return node.data.value
        return None

    def print_table(self):
        print("{")
        for i, val in enumerate(self.hash_table):
            if val is not None:
                llist_string = ""
                node = val
                if node.next_node:
                    while node.next_node:
                        llist_string += (
                            str(node.data.key) + " : " + str(node.data.value) + " --> "
                        )
                        node = node.next_node
                    llist_string += (
                        str(node.data.key) + " : " + str(node.data.value) + " --> None"
                    )
                    print(f"    [{i}] {llist_string}")
                else:
                    print(f"    [{i}] {val.data.key} : {val.data.value}")
            else:
                print(f"    [{i}] {val}")
        print("}")

        """
        ht = HashTable(4)
        ht.add_key_value("hi", "there")
        ht.add_key_value("hi", "there")
        ht.add_key_value("hit", "there")
        ht.print_table()
        lets see the process:
        we create a hash table [None, None, None, None]
        "h" -> ASCCI= 104 => hash-value = 104 => 104 * 104 =
        ........ = 1
        {
            [0] hit : there
            [1] hi : there --> hi : there --> None
            [2] None
            [3] None
        }
        """
