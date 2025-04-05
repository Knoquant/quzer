import json

def is_single_byte_utf8(byte):
    return 0 <= byte <= 127

def detect_multibyte_ranges(data):
    positions = []
    start_position = None
    i = 0
    while i < len(data):
        if data[i] > 127:
            if start_position is None:
                start_position = i
            if (data[i] & 0xE0) == 0xC0:
                char_length = 2
            elif (data[i] & 0xF0) == 0xE0:
                char_length = 3
            elif (data[i] & 0xF8) == 0xF0:
                char_length = 4
            else:
                char_length = 1
            i += char_length - 1
        else:
            if start_position is not None:
                positions.append((start_position, i))
                start_position = None
        i += 1
    if start_position is not None:
        positions.append((start_position, len(data)))
    return positions

def generate_multibyte_pairs(data, positions):
    pairs = []
    for start, end in positions:
        end -= 1
        for i in range(start, end - 5, 3):
            pairs.append(tuple(data[i:i+6]))
    return pairs

def extract_mixed_pairs(data, positions):
    pairs = []
    for i in range(len(data)):
        if is_single_byte_utf8(data[i]):
            if i < len(data) - 1 and data[i + 1] > 127:
                if i + 3 < len(data):
                    pairs.append((data[i], data[i+1], data[i+2], data[i+3]))
            elif i < len(data) - 1 and data[i + 1] <= 127:
                pairs.append((data[i], data[i+1]))
            if i > 0 and data[i - 1] > 127:
                if i - 3 >= 0:
                    pairs.append((data[i-3], data[i-2], data[i-1], data[i]))
    return pairs