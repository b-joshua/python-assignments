
# DNA Sequence Analyzer

The DNA Sequence Analyzer is a Python program that processes DNA sequences to extract specific features. It supports two main analyses:
1. Finding the longest duplicate subsequence within the DNA sequence.
2. Identifying the longest open reading frame (ORF), which is a sequence starting with a start codon (`ATG`) and ending with a stop codon (`TAA`, `TAG`, or `TGA`) in the same reading frame.

---

## **Input Format**

### **Fasta file**
- The program accepts DNA sequence files in **FASTA** or **GenBank** format.
- Example FASTA file (`example.fasta`):
  ```
  >Example DNA Sequence
  ATGAAATTTTAAATGTAGATGCCCTGAATCGATC
  ```

### **Command-Line Options**
- `--duplicate`: Find the longest duplicate subsequence.
- `--orf`: Find the longest open reading frame (ORF).
```bash
python analyze.py example.fasta --duplicate --orf
```

---
## **Acknowledgements**
Assignment for Day 9 of [Gábor Szabó's](https://szabgab.com) [Python Course](https://github.com/szabgab/wis-python-course-2024-11/) at the [Weizmann Institute of Science](https://www.weizmann.ac.il/pages/)
