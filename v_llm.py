from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info
import os


model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-2B-Instruct", torch_dtype="auto", device_map="auto"
)

# default processer
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-2B-Instruct")

messages = [
    {
        "role": "user",
        "content": [
        ],
    }
]

def format_string(schema, context):
    s = f"Come up with question/answer pairs using the context and image provided, in the following format:\n```{schema}```\n\nEverything between the ``` must be valid json. Output should not contain anything more than this json.\n Context: {context}"
    return s


def apply_chat_template(image_paths, prompt, schema):
    template = ""

    prompt = format_string(schema, prompt)

    # Starting with the system message
    template += "<|im_start|>system\nYou are a smart assistant designed to help data creation tasks.\nGiven a piece of context and an image, you must come up with a question and answer pair that can be used to train a vision language model<|im_end|>\n"

    # Adding the user message part
    template += "<|im_start|>user\n"

    # Adding each image to the template using the special tokens
    for image_path in image_paths:
        template += "<|vision_start|><|image_pad|><|vision_end|>"

    # Adding the prompt text
    template += prompt
    template += "<|im_end|>\n"

    # Adding the assistant's turn
    template += "<|im_start|>assistant\n"

    return template


def convert_data(data):
    lis = []
    if data.get('image'):
        for img in data.get('image'):
            img = os.path.join(os.getcwd(), img)
            lis.append({"type": "image", "image": img})

    messages[0]["content"] = lis
    return messages

def main(data_json, schema):
    try:

        json_ = convert_data(data_json)

        text = apply_chat_template(data_json['image'], data_json['content'], schema)

        image_inputs, video_inputs = process_vision_info(json_)
        inputs = processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt",
        )
        inputs = inputs.to("cuda")

        # Inference: Generation of the output
        generated_ids = model.generate(**inputs, max_new_tokens=128)
        generated_ids_trimmed = [
            out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
        ]
        output_text = processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )
        return output_text
    except Exception as e:
        return None
