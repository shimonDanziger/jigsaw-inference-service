import os
from llama_cpp import Llama
from app.config import settings

class InferenceEngine():
    def __init__(self):
        self.model = Llama(
            model_path=settings.MODEL_PATH,
            n_threads=8, 
            n_ctx=2048,
            verbose=False
        )
    def predict(self, text: str):
        
        output = self.model(
            text, # Prompt
            max_tokens=1, 
            stop=["Q:", "\n"], 
            echo=False 
        ) 
        