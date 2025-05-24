import json
import sys
import re
from collections import defaultdict

def build_markov_chain(text, order=1):
    words = re.findall(r"\b\w+\b", text.lower())  # Basic word tokenizer
    markov = defaultdict(list)

    for i in range(len(words) - order):
        key = tuple(words[i:i + order])
        next_word = words[i + order]
        markov[key].append(next_word)

    return { "order": order, "chain": { " ".join(k): v for k, v in markov.items() } }

def main(txt_path, json_path, order=1):
    with open(txt_path, 'r', encoding='utf-8') as f:
        text = f.read()

    chain_data = build_markov_chain(text, order)

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(chain_data, f, indent=2)

    print(f"Markov chain saved to {json_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python txt_to_markov_json.py input.txt output.json [order]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        order = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        main(input_file, output_file, order)
