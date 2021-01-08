from transformers import pipeline, set_seed
from transformers.pipelines import TextGenerationPipeline
from transformers import *
import re

class TextGenerator:
    def __init__(self):
        self.generator: TextGenerationPipeline
        self.tokenizer = AutoTokenizer.from_pretrained("./finetuned_models")
        self.model = AutoModelWithLMHead.from_pretrained("./finetuned_models")   

    def load_generator(self) -> None:
        self.generator = pipeline('text-generation', model= self.model, tokenizer = self.tokenizer)

    def clean_text(self, quote):
        #Remove extra spaces
        quote = re.sub("\s\s+", " ", quote)
        #Remove space before punctuation
        quote = re.sub(r'\s+([?.!,;])', r'\1', quote)
        #Remove space after punctuation
        quote = re.sub(r'(["\'])\s+', r'\1', quote)
        #Sentence case
        quote  = quote.capitalize().strip()
        return quote

    def generate_text(self, starting_text: str, min_length=10, max_length=50, temperature=0.9) -> str:
        quote = self.generator(starting_text.strip(), min_length = min_length, max_length = max_length, temperature = temperature, top_k=50, top_p=0.95, no_repeat_ngram_size = 3, repetition_penalty=1.2)[0]['generated_text']
        return self.clean_text(quote)


