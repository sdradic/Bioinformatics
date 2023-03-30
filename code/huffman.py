from collections import defaultdict
import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(sequence):
    freq_table = defaultdict(int)
    for char in sequence:
        freq_table[char] += 1
    return freq_table

def build_huffman_tree(freq_table):
    heap = []
    for char, freq in freq_table.items():
        node = HuffmanNode(char, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged_node = HuffmanNode(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, merged_node)

    return heap[0]

def build_codeword_table(root):
    codeword_table = {}

    def traverse(node, codeword):
        if node is None:
            return
        if node.char is not None:
            codeword_table[node.char] = codeword
        traverse(node.left, codeword + '0')
        traverse(node.right, codeword + '1')

    traverse(root, '')

    return codeword_table

def huffman_compress(sequence):
    freq_table = build_frequency_table(sequence)
    huffman_tree = build_huffman_tree(freq_table)
    codeword_table = build_codeword_table(huffman_tree)

    compressed_sequence = ''.join(codeword_table[char] for char in sequence)

    return compressed_sequence, codeword_table

def huffman_decompress(compressed_sequence, codeword_table):
    char_table = {codeword: char for char, codeword in codeword_table.items()}

    sequence = ''
    codeword = ''
    for bit in compressed_sequence:
        codeword += bit
        if codeword in char_table:
            sequence += char_table[codeword]
            codeword = ''

    return sequence