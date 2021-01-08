from transformers import pipeline, set_seed
from transformers.pipelines import TextGenerationPipeline
from transformers import *

class TextGenerator:
    def __init__(self):
        self.generator: TextGenerationPipeline
        self.tokenizer = AutoTokenizer.from_pretrained("./finetuned_models")
        self.model = AutoModelWithLMHead.from_pretrained("./finetuned_models")   

    def load_generator(self) -> None:
        self.generator = pipeline('text-generation', model= self.model, tokenizer = self.tokenizer)

    def generate_text(self, starting_text: str, min_length=10, max_length=50, temperature=0.9) -> str:
        return self.generator(starting_text, min_length = min_length, max_length = max_length, temperature = temperature, top_k=50, top_p=0.95, no_repeat_ngram_size = 3, repetition_penalty=1.2)[0]['generated_text']


