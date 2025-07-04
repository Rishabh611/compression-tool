from compression_tool.encoder import Encoder

def test_get_frequency_map():
    encoder = Encoder()

    frequency_map = encoder._get_frequency_map("abc")

    assert frequency_map["a"] == 1 
    assert frequency_map["b"] == 1 

def test_huffman_tree():
    encoder = Encoder()

    frequency_map = encoder.get_frequency_map("abc")

    huffman_tree = encoder._get_huffman_tree(frequency_map)

    assert huffman_tree.root.weight == 53

    prefix_code_table = huffman_tree.get_prefix_code_table()
    
    print(prefix_code_table)

    assert prefix_code_table["d"] == "01"
    assert prefix_code_table["p"] == "00"
    assert prefix_code_table["q"] == "101"
    assert prefix_code_table["i"] == "11"

def test_encoded_string():
    encoder = Encoder()

    encoded_string = encoder.encode("tests/test1.txt", prefix_code_table)

    assert encoded_string == 0
