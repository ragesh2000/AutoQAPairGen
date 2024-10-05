from langchain_unstructured import UnstructuredLoader

def extract(file_path):

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
                curent_dic["content"] += doc.page_content
            except:
                curent_dic["content"] = doc.page_content

        elif doc.metadata.get("category") == "Image":
            imagepath = doc.metadata.get("image_path")
            curent_dic["image"].append(imagepath)

    structured_data.append(curent_dic)

    # merge title and content by /n
    structured_data = [doc for doc in structured_data if "content" in doc]

    for doc in structured_data:
        try:
            doc["content"] = doc["title"] + "\n" + doc["content"]
            doc.pop("title")
        except:
            pass
    return structured_data
