import os
import json
from nanonets import OCR

API_KEY = os.environ.get('NANONETS_API_KEY')
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')
CATEGORIES = ['name', 'sex', 'date_of_birth', 'address', 'dl_number', 'issue_date', 'exp_date', 'class', 'height', 'restrictions', 'eyes']

model = OCR(API_KEY, CATEGORIES, model_id=MODEL_ID)

response = model._check_model_state()

state = json.loads(response.text)["state"]

if state == 5:
	print("NEXT RUN: python ./code/prediction.py ./images/33.jpg")