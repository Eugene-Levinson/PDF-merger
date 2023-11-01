from typing import List
import sys
import os
import glob
import PyPDF2

def custom_sort_key(item):
    # Account for windows and linux file path differences
    if "/" in item:
        file = item.split("/")[-1]
    elif "\\" in item:
        ile = item.split("\\")[-1]

    order_number = int(file.split(' ')[0])

    return order_number



def combine_pdfs(files: List[str], output_path: str):
    pdf_merger = PyPDF2.PdfMerger()

    # Iterate through the list of PDF files and append them to the merger
    for pdf_file in files:
        pdf_merger.append(pdf_file)

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

    # Close the PDF merger object
    pdf_merger.close()

    print(f'Merged PDF saved as {output_path}')


if __name__ == "__main__":

    # Check right number of arguments was passed in
    if len(sys.argv) != 3:
        print("Usage: python combine.py <input folder> <output file>")
        sys.exit(1)

    input_directory = sys.argv[1]
    output_file = sys.argv[2]
    
    # Check input directory exists
    if not os.path.exists(input_directory):
        print(f"Input directory '{input_directory}' does not exist.")
        sys.exit(1)

    # Get all input pdfs
    pdf_files = glob.glob(os.path.join(input_directory, "*.pdf"))

    # Sort the files
    pdf_files = sorted(pdf_files, key=custom_sort_key)

    combine_pdfs(pdf_files, output_file)


