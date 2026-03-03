from fetch_data import fetch_gene_summary
from sequence_analysis import fetch_nucleotide_sequence, analyze_sequence
from ai_explainer import get_ai_explanation
from report_generator import generate_report


def main():
    print("=============================================")
    print("      GenIntel - AI Bioinformatics Analyzer  ")
    print("=============================================\n")

    gene_name = input("Enter gene name (e.g., BRCA1, TP53): ").strip()

    if not gene_name:
        print("Gene name cannot be empty.")
        return

    # =========================
    # Step 1: Fetch Gene Info
    # =========================
    print("\nFetching gene information from NCBI...")
    gene_data = fetch_gene_summary(gene_name)

    if gene_data is None:
        print("Gene not found.")
        return
    elif "error" in gene_data:
        print("Error fetching gene data:", gene_data["error"])
        return

    print("\n===== Gene Information =====")
    print("Gene ID:", gene_data["GeneID"])
    print("Official Name:", gene_data["Name"])
    print("Description:", gene_data["Description"])

    # =========================
    # Step 2: Fetch Sequence
    # =========================
    print("\nFetching nucleotide sequence...")
    sequence = fetch_nucleotide_sequence(gene_name)

    if sequence is None:
        print("No nucleotide sequence found.")
        return
    elif isinstance(sequence, dict) and "error" in sequence:
        print("Error fetching sequence:", sequence["error"])
        return

    # =========================
    # Step 3: Analyze Sequence
    # =========================
    print("Analyzing sequence...")
    analysis = analyze_sequence(sequence)

    print("\n===== Sequence Analysis =====")
    print("Sequence Length:", analysis["Length"])
    print("GC Content:", analysis["GC_Content"], "%")

    # =========================
    # Step 4: AI Explanation
    # =========================
    print("\nGenerating AI explanation...")
    ai_output = get_ai_explanation(gene_data, analysis)

    print("\n===== AI Explanation =====")
    print(ai_output)

    # =========================
    # Step 5: Generate Report
    # =========================
    print("\nGenerating report file...")
    report_file = generate_report(gene_data, analysis, ai_output)

    print(f"\nReport saved successfully as: {report_file}")
    print("\n===== Process Completed Successfully =====")


if __name__ == "__main__":
    main()