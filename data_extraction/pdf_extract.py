from langchain_unstructured import UnstructuredLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import copy

def extract(file_path, context_window=4000):

    loader = UnstructuredLoader(
        file_path=file_path,
        strategy="hi_res",
        extract_images_in_pdf=True,
        extract_image_block_to_payload=False,
        extract_image_block_output_dir="us_images"
    )

    docs = []
    for doc in loader.lazy_load():
        docs.append(doc)

    structured_data = []
    for doc in docs:
        if doc.metadata.get("category") == 'Title':
            try:
                structured_data.append(curent_dic)
            except:
                pass

            curent_dic = {'image': []}
            curent_dic["title"] = doc.page_content

        elif doc.metadata.get("category") in ['NarrativeText', 'ListItem']:
            try:
                try:
                    curent_dic["content"] += doc.page_content
                except:
                    curent_dic["content"] = doc.page_content
            except UnboundLocalError:
                curent_dic = {'image': [], 'title': '', 'content': doc.page_content}

        elif doc.metadata.get("category") == "Image":
            imagepath = doc.metadata.get("image_path")
            curent_dic["image"].append(imagepath)

    structured_data.append(curent_dic)

    # merge title and content by /n
    structured_data = [doc for doc in structured_data if "content" in doc]
    final_data = []

    for doc in structured_data:
        try:
            added_content = "\n".join([doc["title"], doc["content"]])
            if len(added_content) > context_window:
                header = doc["title"]
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=context_window, chunk_overlap=0, separators=["\n\n",".", ",", "\n"])
                splitted_content = text_splitter.split_text(doc["content"])
            
                for split in splitted_content:
                    # Create a copy of doc to avoid modifying the original reference
                    new_doc = copy.deepcopy(doc)
                    new_doc["content"] = "\n".join([header, split])
                    try:
                        new_doc.pop("title")
                    except:
                        pass
                    final_data.append(new_doc)

            else:
                doc["content"] = doc["title"] + "\n" + doc["content"]
                doc.pop("title")
                final_data.append(doc)
        
        except:
            pass
    return final_data

