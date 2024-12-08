import sys

def count_bases(seq):
    counts = {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    for char in seq:
        if char in "ACGT":
            counts[char] += 1
        else:
            counts["Unknown"] += 1
    return counts

def get_seqs():
    if len(sys.argv) < 2:
        exit(f"Usage: {sys.argv[0]} FILENAME [FILENAME ...]\n Please include at least one sequence file!")

    files = sys.argv[1:]
    seqs = []
    for filename in files:
        with open(filename, "r") as fh:
            seqs.append(fh.read())
    return files, seqs

def print_table(filename, counts, total):
    print(f"\n{filename}")
    for base in "ACGT":
        print(f"{base}: {counts[base]:12} {counts[base] / total * 100:.1f}%")
    print(f"Unknown: {counts['Unknown']:6} {counts['Unknown'] / total * 100:.1f}%")
    print(f"Total: {total:9}")

if __name__ == "__main__":
    files, seqs = get_seqs()
    counts_all = {"A": 0, "C": 0, "G": 0, "T": 0, "Unknown": 0}
    total_all = 0

    for filename, seq in zip(files, seqs):
        counts = count_bases(seq)
        total = sum(counts.values())
        print_table(filename, counts, total)

        for base, count in counts.items():
            if base in counts_all:
                counts_all[base] += count
            else:
                counts_all["Unknown"] += count
        total_all += total
    
    print("\nAll")
    for base in "ACGT":
        print(f"{base}: {counts_all[base]:12} {counts_all[base] / total_all * 100:.1f}%")
    print(f"Unknown: {counts_all['Unknown']:6} {counts_all['Unknown'] / total_all * 100:.1f}%")
    print(f"Total: {total_all:9}")
