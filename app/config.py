import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_PATH: str = os.getenv("MODEL_PATH")
    RULES_LIST = ['']
    system_prompt = '''You are given a comment from reddit and a rule. 
        Your task is to classify whether the comment violates the rule. 
        Only respond Yes/No.'''
    positive = "Yes"
    negative = "No"
    judge_words = "Violation:"
    subreddit = "politic"

settings = Settings()