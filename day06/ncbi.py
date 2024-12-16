import argparse
import os
import csv
from datetime import datetime
from Bio import Entrez

# Email
Entrez.email = "joshua.bugis@weizmann.ac.il"

# Get the date and time of search
def search_date():
    date_and_time = datetime.now()
    now = date_and_time.strftime("%Y-%m-%d %H:%M:%S")
    return now

# Parse the arguments of the search
def parse_args():
    parser = argparse.ArgumentParser(description = "Download NCBI data")
    parser.add_argument("--database", default = "nucleotide", help = "Enter NCBI database (ex. nucleotide, protein, pubmed, etc.)")
    parser.add_argument("--term", required = True, help = "Enter a search term")
    parser.add_argument("--number", default = 10, help = "Enter number of records to download")
    return parser.parse_args()

def get_database_settings(database):
    settings = {
        "nucleotide": {"rettype": "gb", "suffix": ".gb"},
        "protein": {"rettype": "fasta", "suffix": ".fasta"},
        "pubmed": {"rettype": "abstract", "suffix": ".txt"},
        "gene": {"rettype": "fasta", "suffix": ".fasta"},
        "genome": {"rettype": "fasta", "suffix": ".fasta"},
        "assembly": {"rettype": "docsum", "suffix": ".txt"},
        "bioproject": {"rettype": "docsum", "suffix": ".txt"},
        "biosample": {"rettype": "docsum", "suffix": ".txt"},
        "taxonomy": {"rettype": "xml", "suffix": ".xml"},
        "sra": {"rettype": "runinfo", "suffix": ".csv"},
        "clinvar": {"rettype": "vcf", "suffix": ".vcf"},
        "dbvar": {"rettype": "vcf", "suffix": ".vcf"},
        "structure": {"rettype": "pdb", "suffix": ".txt"},
        "biosystems": {"rettype": "docsum", "suffix": ".txt"},
        "books": {"rettype": "text", "suffix": ".txt"},
    }
    return settings.get(database, {"rettype": "text", "suffix": ".txt"})

# Search the NCBI database of choice
def search_NCBI(database, search_term, number):
    handle = Entrez.esearch(db=database, term = search_term, retmax = number)
    data = Entrez.read(handle)
    handle.close()
    return data

def get_files(database, file_ids):
    settings = get_database_settings(database)
    rettype = settings["rettype"]
    suffix = settings["suffix"]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.join(script_dir, "NCBI_search_results")
    os.makedirs(results_dir, exist_ok=True)

    files = []
    for id in file_ids:
        try:
            handle = Entrez.efetch(db = database, id = id, rettype = rettype, retmode = "text")
            data = handle.read()
            file_name = os.path.join(results_dir, f"{id}_{database}{suffix}")

            with open(file_name, "w") as fh:
                fh.write(data)
            
            files.append(file_name)

        except:
            print(f"Error fetching NCBI file {id}")

    return files

def write_csv(date, database, search_term, number, total):
    file_exists = os.path.isfile("./python-assignments/day06/NCBI_search_metadata.csv")
    with open("./python-assignments/day06/NCBI_search_metadata.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow(["date", "database", "term", "max", "total"])
        writer.writerow([date, database, search_term, number, total])

def main():
    args = parse_args()

    results = search_NCBI(database = args.database, search_term = args.term, number = args.number)
    total_results = int(results["Count"])

    files = get_files(database = args.database, file_ids = results["IdList"])

    write_csv(date = search_date(), database = args.database, search_term = args.term, number = args.number, total = total_results)

if __name__ == "__main__":
    main()



