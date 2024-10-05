import argparse
import pdf_extract
import getpass

def call():
    path_to_pdf = getpass.getpass("Path to data : ")
    requested_schema = input("Format required : ")
    parser = argparse.ArgumentParser()
    parser.add_argument('-category', required=False, help='Specify the category of use (vision/text)', default= 'text')
    args = parser.parse_args()
    category = args.category

    json_data = pdf_extract.extract(path_to_pdf)
 
    if category == 'vision':
        import v_llm
        data = [v_llm.main(doc, requested_schema) for doc in json_data]
    else:
        import llm
        data = [llm.main(doc, requested_schema) for doc in json_data]


if __name__ == "__main__":
    call()
