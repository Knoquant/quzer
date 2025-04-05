def decode_byte_pairs(pairs):
    decoded_pairs = []
    for pair in pairs:
        single_byte_part = [b for b in pair if b <= 127]
        multi_byte_part = [b for b in pair if b > 127]
        single_decoded = "".join(chr(b) for b in single_byte_part) if single_byte_part else ""
        multi_decoded = bytes(multi_byte_part).decode("utf-8", errors="ignore") if multi_byte_part else ""
        decoded_pairs.append((single_decoded, multi_decoded))
    return decoded_pairs

def build_vocabulary(decoded_pairs, decoded_multibyte_pairs):
    vocabulary = {}
    vocab_id = 1
    for single, multi in decoded_pairs:
        token = f"{single}{multi}"
        if token not in vocabulary:
            vocabulary[token] = {"id": vocab_id, "frequency": 1}
            vocab_id += 1
        else:
            vocabulary[token]["frequency"] += 1

    for token in decoded_multibyte_pairs:
        if token not in vocabulary:
            vocabulary[token] = {"id": vocab_id, "frequency": 1}
            vocab_id += 1
        else:
            vocabulary[token]["frequency"] += 1
    return vocabulary