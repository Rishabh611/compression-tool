from compression_tool.huffman_node import HuffmanLeafNode
from compression_tool.huffman_tree import HuffmanTree
from collections import defaultdict

import heapq

class Encoder:
    def __init__(self):
        pass

    def _read_input(self, file_path: str) -> str:
        with open(file_path, "r") as file:
            return file.read()

    def _get_frequency_map(self, file_content) -> dict[str, int]:
        frequency_map: dict[str, int] = defaultdict(int)

        for character in file_content:
            frequency_map[character] += 1
        
        print("| Character | Frequency |")
        for character, frequency in frequency_map.items():
            print(f"| {character} | {frequency} |")
        return frequency_map
    
    def _get_huffman_tree(self, frequency_map: dict[str, int]):
        priority_queue = []
        for character, frequency in frequency_map.items():
            heapq.heappush(priority_queue, HuffmanLeafNode(character, frequency))   # type: ignore
        huffman_tree = HuffmanTree(priority_queue) # type: ignore

        return huffman_tree
        
    def _get_prefix_code_table(self, file_content) -> dict[str, str]:
        '''
        from the file contents generate the prefix code table
        '''
        frequency_map = self._get_frequency_map(file_content)
        huffman_tree = self._get_huffman_tree(frequency_map)
        return huffman_tree.get_prefix_code_table()

    def _get_encoded_string(self, file_content):
        '''
        From the file contents generate the encoded file string
        '''
        prefix_code_table = self._get_prefix_code_table(file_content)

        encoded_string = ""

        for character in file_content:
            encoded_string += prefix_code_table[character]

        padding_count = 8 - (len(encoded_string) % 8)

        for _ in range(padding_count):
            encoded_string += "0"

        return int(encoded_string, 2)

    def encode(self, file_path: str, output_file_path: str):
        '''
        Encode the file contents and store it in another file
        '''
        file_contents = self._read_input(file_path)

        encoded_contents = self._get_encoded_string(self, file_contents)

        if not output_file_path:
            out_file_path = file_path + ".huff"

        with open(out_file_path, "w") as file:
            file.write(str(encoded_contents))
