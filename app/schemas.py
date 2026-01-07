from pydantic import BaseModel , Field   , field_validator
from app.config import settings


class ToxicityRequest(BaseModel):
    ruleNum: int = Field(ge=0)

    @field_validator('ruleNum')
    @classmethod
    def check_rule_num_exist(cls, v: int) -> int:
        if v >len(settings.RULES_LIST):
            raise ValueError('rule num not found')
        return v
    
    text: str = Field(min_length=1)
    positive_example: str = Field(min_length=1)
    negative_example: str = Field(min_length=1)
    
class ToxicityResponse(BaseModel):
    
    toxicity_score: float= Field(ge=0, le=1)

def build_prompt(request: ToxicityRequest):
    rule = settings.RULES_LIST[request.ruleNum - 1]

    return f"""{settings.system_prompt}
        Subreddit: r/{settings.subreddit}
        Rule: {rule}
        Examples:
        1) {request.positive_example}
        {settings.judge_words} Yes
        2) {request.negative_example}
        {settings.judge_words} No
        Comment: {request.text}
        {settings.judge_words}"""
