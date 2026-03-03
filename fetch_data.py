from Bio import Entrez
Entrez.email="thirdchannel303@gmail.com"
def fetch_gene_summary(gene_name):
    try:

        handle= Entrez.esearch(
            db="gene",
            term=f"{gene_name}[Gene Name] AND Homo sapiens[Organism]",
            retmode="xml"

        )
        record = Entrez.read(handle)
        handle.close()

        if not record["IdList"]:
            return None
        gene_id = record["IdList"][0]

        handle = Entrez.esummary(
            db="gene",
            id=gene_id,
            retmode="xml"
        )
        summary_record = Entrez.read(handle)
        handle.close()

        gene_info = summary_record["DocumentSummarySet"]["DocumentSummary"][0]
        return{
            "GeneID":gene_id,
            "Name":gene_info.get("Name","N/A"),
            "Description":gene_info.get("Description" ,"N/A"),
            "Summary":gene_info.get("Summary","N/A")
        }
    except Exception as e:
        return {"error":str(e)}




