from deepmultilingualpunctuation import PunctuationModel
from fastapi import FastAPI, Response
from pydantic import BaseModel

# summary_min_length = 0
# summary_max_length = 150

# generator = pipeline('text-generation', model='gpt2')

model = PunctuationModel()

app = FastAPI()


class Body(BaseModel):
    text: str

@app.get('/')
def root():
    return Response("<h1>An API to interact with punctuation model</h1>")


@app.post('/generate')
def predict(body: Body):
    result = model.restore_punctuation(body.text)
    return result
