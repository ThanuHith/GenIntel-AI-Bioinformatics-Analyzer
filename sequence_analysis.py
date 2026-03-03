from pprint import PrettyPrinter

from Bio import SeqIO, Entrez
from io import StringIO
Entrez.email="thirdchannel303@gmail.com"
Entrez.tool="GenIntel_Project"

def fetch_nucleotide_sequence(gene_name):
    try:
        handle= Entrez.esearch(
            db="nucleotide",
            term=f"{gene_name}[Gene]AND Homo sapiens[Organism]",
            retmode="xml",
            retmax=1
        )
        record = Entrez.read(handle)
        handle.close()

        if not record["IdList"]:
            return None
        seq_id = record["IdList"][0]
        handle= Entrez.efetch(
            db="nucleotide",
            id=seq_id,
            rettype="fasta",
            retmode="text"
        )
        fasta_data = handle.read()
        handle.close()

        sequence = SeqIO.read(StringIO(fasta_data), "fasta")
        return sequence
    except Exception as e:
        print(e)
def analyze_sequence(sequence):
    seq_str = str(sequence.seq)
    length = len(seq_str)
    g_count = seq_str.count("G")
    c_count = seq_str.count("C")
    gc_count = ((g_count + c_count) / length) * 100 if length > 0 else 0
    return {
        "Length": length,
        "GC_Content": round(gc_count, 2),
    }




