import sys
from quzer.tokenizer import *
from quzer.utils import *

def main():
    text = "सूरज चमकदार रूप से विशाल सुनहरे खेतों के ऊपर चमक रहा था, जब बच्चे नदी के किनारे खेल रहे थे। पक्षी मधुर स्वर में चहचहा रहे थे, उनके गीत सरसराते पत्तों के साथ घुल-मिल रहे थे। हंसी और आनंद के बीच, एक वृद्ध व्यक्ति लकड़ी की बेंच पर बैठा हुआ था, विचारों में खोया हुआ। उसकी झुर्रियों भरी उंगलियाँ एक पुरानी किताब को पकड़े थीं, जिसके पन्ने भूले-बिसरे समय की कहानियाँ फुसफुसा रहे थे। एक हल्की हवा चमेली के खिलते फूलों की खुशबू अपने साथ लिए हुए थी, जबकि दूर कहीं घंटियाँ बीते हुए समय का संकेत दे रही थीं। गाँव के सबसे दूर के कोने में, एक अकेली बिल्ली दुनिया को शांति से देख रही थी, उसकी पूँछ हल्के से हिल रही थी।"
    data = list(text.encode("utf-8"))
    positions = detect_multibyte_ranges(data)
    multi_pairs = generate_multibyte_pairs(data, positions)
    mixed_pairs = extract_mixed_pairs(data, positions)
    decoded_pairs = decode_byte_pairs(mixed_pairs)
    decoded_multi = [bytes(p).decode("utf-8", errors="ignore") for p in multi_pairs]
    vocab = build_vocabulary(decoded_pairs, decoded_multi)

    with open("vocabulary.json", "w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=4)
    print("✅ Vocabulary saved to vocabulary.json")

if __name__ == "__main__":
    main()
