class Node:
    def __init__(self, data= None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _insert_recursive(self, data, node):
        # the left subtrees sshould only be lesser thant the root node
        # the right subtrees should only be greater than the root node
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"]  > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            #if the value isnt greater or lessers than node.data means that is equal
            # so the value is already contain in our tree so we dont have to insert
            return
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
    
    def _search_recursive(self, blog_post_id, node):
        if blog_post_id == node.data["id"]:
            return node.data
        if blog_post_id < node.data["id"] and node.left is not None:
            if blog_post_id == node.left.data["id"]:
                return node.left.data
            return self._search_recursive(blog_post_id, node.left)
        if blog_post_id > node.data["id"] and node.right is not None:
            if blog_post_id == node.right.data["id"]:
                return node.right.data
            return self._search_recursive(blog_post_id, node.right)

        return False

    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            return False

        return self._search_recursive(blog_post_id, self.root)