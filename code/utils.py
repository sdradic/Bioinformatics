from huffman import huffman_compress, huffman_decompress
from lzw import lzw_compress_sequence

def read_sequence(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def remove_words_from_file():
    with open("../data/test.fasta", "r") as file:
        lines = file.readlines()

    with open("../data/test_clean.fasta", "w") as file:
        for line in lines:
            if not line.startswith(">"):
                file.write(line)

def run_huffman_compression(sequence):
    compressed_sequence, codeword_table = huffman_compress(sequence)
    ratio = '%.5f' % (len(compressed_sequence) / len(sequence))
    print('Compressed sequence length: %d' % len(compressed_sequence))
    # print('Codeword table length: %d' % len(codeword_table))
    print('Compression ratio: %.5f' % (len(compressed_sequence) / len(sequence)))
    # print('Codeword table size: %.2f' % (len(codeword_table) * 8 / len(sequence)))
    print('Compression efficiency: %.2f' % (len(compressed_sequence) / (len(codeword_table) * 8)))
    # print('Compression efficiency: %.2f' % (len(compressed_sequence) / (len(codeword_table) * 8) / len(sequence)))
    return ratio

def run_lzw_compression(sequence):
    compressed_sequence = lzw_compress_sequence(sequence)
    ratio = '%.5f' % (len(compressed_sequence) / len(sequence))
    print('Compressed sequence length: %d' % len(compressed_sequence))
    print('Compression ratio: %.5f' % (len(compressed_sequence) / len(sequence)))
    print('Compression efficiency: %.2f' % (len(compressed_sequence) * 8 / len(sequence)))
    return ratio