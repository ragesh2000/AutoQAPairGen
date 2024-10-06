import argparse
from data_extraction import pdf_extract
import getpass
import os

def call():
    path_to_pdf = getpass.getpass("Path to data : ")

    # check if the path is valid pdf
    if not os.path.exists(path_to_pdf) or not os.path.isfile(path_to_pdf) or not path_to_pdf.endswith('.pdf'): 
        print("Invalid path. Please provide a valid path to a PDF file.")
        return
    
    requested_schema = input("Required output schema : ")
    parser = argparse.ArgumentParser()
    parser.add_argument('-category', required=False, help='Specify the category of use (vision/text)', default= 'text')
    args = parser.parse_args()
    category = args.category
    
    json_data = pdf_extract.extract(path_to_pdf)
 
    if category == 'vision':
        from models import v_llm
        data = [v_llm.main(doc, requested_schema) for doc in json_data]
    else:
        from models import llm
        data = [llm.main(doc, requested_schema) for doc in json_data]


if __name__ == "__main__":
    call()
