import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

torch.random.manual_seed(0)

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3.5-mini-instruct", 
    device_map="cuda", 
    torch_dtype="auto", 
    trust_remote_code=True, 
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3.5-mini-instruct")

sys_prompt = """You are a smart assistant designed to help data creation tasks.\nGiven a piece of context , you must come up with a question and answer pair that can be used to train a language model"""

def format_string(schema, context):
    s = f"Come up with question/answer pairs using the context provided, in the following format:\n```{schema}```\n\nEverything between the ``` must be valid json. Output should not contain anything more than this json.\n Context: {context}"
    return s



def main(data_json, schema):
    try:

        prompt = format_string(schema, data_json['content'])

        messages = [{"role": "system", "content":sys_prompt}, {"role": "user", "content": prompt}]
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
        )

        generation_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "temperature": 0.0,
            "do_sample": False,
        }

        output = pipe(messages, **generation_args)
        return (output[0]['generated_text'])
    except Exception as e:
        return None