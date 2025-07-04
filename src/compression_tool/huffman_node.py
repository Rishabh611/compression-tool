class BaseNode:
    def __init__(self, weight):
       self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight

class HuffmanLeafNode(BaseNode):
    def __init__(self, character, weight):
        self.character = character
        super().__init__(weight)

class HuffmanInternalNode(BaseNode):
    def __init__(self, left, right, weight):
        self.left = left
        self.right = right
        super().__init__(weight)
