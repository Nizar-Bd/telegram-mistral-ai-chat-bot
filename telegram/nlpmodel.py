""" Load LLM model from huggingface"""
import torch
from transformers import pipeline
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

def load_model(model_name):
    """ Load particular model from hugginface with name
        Return the llm model pipe """

    pipe = pipeline("text-generation", model=model_name, torch_dtype=torch.bfloat16, device_map="auto")

    return pipe


def answer_query(pipe, text):
    """ Take a model and its tokenizer and process a query for specified text
        Return the answer as a string"""

    message = [{"role":"user",
                "content":text}]
    prompt = pipe.tokenizer.apply_chat_template(message, tokenize=False, add_generation_prompt=True)
    outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)

    return outputs[0]['generated_text'][len(text)+28:]
