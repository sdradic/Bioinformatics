def lzw_compress_sequence(sequence):
    # Create a dictionary with all possible single characters
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    output = []
    buffer = ''
    
    for char in sequence:
        # Combine current character with buffer if in dictionary
        if buffer + char in dictionary:
            buffer += char
        else:
            # Add code for buffer to output
            output.append(dictionary[buffer])
            # Add new code for buffer + char to dictionary
            dictionary[buffer + char] = next_code
            next_code += 1
            # Reset buffer to current character
            buffer = char
    
    # Add code for last buffer to output
    output.append(dictionary[buffer])
    
    return output
