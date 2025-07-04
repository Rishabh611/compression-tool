from compression_tool.huffman_node import HuffmanInternalNode, HuffmanLeafNode
import heapq

class HuffmanTree:
    def __init__(self, priority_queue):
        self.priority_queue = priority_queue

        self._build_huffman_tree()

    def _build_huffman_tree(self):
        while len(self.priority_queue) != 1:
            left = heapq.heappop(self.priority_queue)
            right = heapq.heappop(self.priority_queue)
            heapq.heappush(
                self.priority_queue,
                HuffmanInternalNode(left, right, left.weight + right.weight),
            )
        self.root = self.priority_queue[0]

    def get_prefix_code_table(self):
        self.prefix_code_table = {}

        def _dfs(node, code):
            if isinstance(node, HuffmanLeafNode):
                self.prefix_code_table[node.character] = code
                return

            _dfs(node.left, code + "0")
            _dfs(node.right, code + "1")

        _dfs(self.root, "")

        return self.prefix_code_table

    
