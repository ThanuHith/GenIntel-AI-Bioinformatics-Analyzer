from datetime import datetime
def generate_report(gene_data,sequence_analysis,ai_explanation):
    filename = f"{gene_data["Name"]}_GenIntel_Report.txt"

    with open(filename,"w",encoding="utf-8") as file:
        file.write("=============================================\n")
        file.write("        GenIntel AI Bioinformatics Report\n")
        file.write("=============================================\n\n")

        file.write(f"Generated on: {datetime.now()}\n\n")

        file.write("===== Gene Information =====\n")
        file.write(f"Gene ID: {gene_data['GeneID']}\n")
        file.write(f"Official Name: {gene_data['Name']}\n")
        file.write(f"Description: {gene_data['Description']}\n")
        file.write(f"Summary: {gene_data['Summary']}\n\n")

        file.write("===== Sequence Analysis =====\n")
        file.write(f"Sequence Length: {sequence_analysis['Length']}\n")
        file.write(f"GC Content: {sequence_analysis['GC_Content']}%\n\n")

        file.write("===== AI Explanation =====\n")
        file.write(ai_explanation)
        file.write("\n\n=============================================\n")
        file.write("End of Report\n")

    return filename