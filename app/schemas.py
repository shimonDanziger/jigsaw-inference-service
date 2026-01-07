from pydantic import BaseModel , Field



class ToxicityRequest(BaseModel):
    ruleNum: int = Field(ge=0, le=6 , description=)
    text: str = Field(min_length=2, max_length=512)


class ToxicityResponse(BaseModel):
    
    toxicity_score: float= Field(ge=0, le=1)

def build_promt(request: ToxicityRequest)