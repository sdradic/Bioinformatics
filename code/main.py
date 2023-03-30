import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
from utils import read_sequence, run_huffman_compression, run_lzw_compression, remove_words_from_file

def normalize_log_ratio_data(huf_ratio, lzw_ratio, neural_ratio):
    huf_ratio = np.log2(float(huf_ratio))
    lzw_ratio = np.log2(float(lzw_ratio))
    neural_ratio = np.log2(float(neural_ratio))
    return huf_ratio, lzw_ratio, neural_ratio

def graph_dot_compression_ratios(huf_ratio, lzw_ratio, neural_ratio):
    fig = plt.figure(figsize=(10, 5))
    ax = fig.add_subplot(111)
    ax.scatter(huf_ratio, lzw_ratio, color='green', label='Huffman vs LZW')
    ax.scatter(huf_ratio, neural_ratio, color='blue', label='Huffman vs Neural Network')
    ax.scatter(lzw_ratio, neural_ratio, color='red', label='LZW vs Neural Network')
    ax.set_xlabel('Compression Ratio')
    ax.set_ylabel('Compression Ratio')
    ax.title.set_text('Comparison of compression ratios')
    ax.legend()
    plt.show()

if __name__ == "__main__":
    file_path = '../data/test_clean.fasta'
    sequence = read_sequence(file_path)
    print("------------Running huffman------------\n")
    huf_ratio = run_huffman_compression(sequence)
    print("------------Running lzw------------\n")
    lzw_ratio = run_lzw_compression(sequence)
    print("------------Getting neural network data------------\n")
    neural_ratio = '0.01456'
    # print("------------Normalizing data------------\n")
    # huf_ratio, lzw_ratio, neural_ratio = normalize_log_ratio_data(huf_ratio, lzw_ratio, neural_ratio)
    print("------------Graphing results------------\n")
    graph_dot_compression_ratios(huf_ratio, lzw_ratio, neural_ratio)