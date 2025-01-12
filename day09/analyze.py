import argparse
import re

def find_longest_duplicate(sequence):
    n = len(sequence)
    for length in range(n, 0, -1):
        for i in range(n - length + 1):
            substring = sequence[i:i + length]
            if re.search(f"(?=({substring}).+\\1)", sequence):
                return substring
    return ""


def find_longest_orf(sequence):
    orf_pattern = re.compile(r"ATG(?:.{3})*?(?:TAA|TAG|TGA)")
    matches = []
    for match in orf_pattern.finditer(sequence):
        start = match.start()
        end = match.end()
        if (end - start) % 3 == 0:
            matches.append(sequence[start:end])
    if not matches:
        return ""
    return max(matches, key=len)


def main():
    parser = argparse.ArgumentParser(description="Analyze DNA sequences for specific features.")
    parser.add_argument("file", help="Path to the input file (FASTA or GenBank format).")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest duplicate subsequence.")
    parser.add_argument("--orf", action="store_true", help="Find the longest open reading frame (ORF).")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        sequence = "".join(line.strip() for line in f if not line.startswith(">"))

    if args.duplicate:
        longest_duplicate = find_longest_duplicate(sequence)
        if longest_duplicate:
            print(f"Longest duplicate subsequence: {longest_duplicate}")
        else:
            print("No duplicate subsequences found.")

    if args.orf:
        longest_orf = find_longest_orf(sequence)
        if longest_orf:
            print(f"Longest open reading frame (ORF): {longest_orf}")
        else:
            print("No open reading frames (ORFs) found.")

    if not args.duplicate and not args.orf:
        print("No analysis selected. Use --duplicate, --orf, or both.")


if __name__ == "__main__":
    main()

