from nanonets import OCR
import os, sys

API_KEY = os.environ.get('NANONETS_API_KEY')
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')
CATEGORIES = ['name', 'sex', 'date_of_birth', 'address', 'dl_number', 'issue_date', 'exp_date', 'class', 'height', 'restrictions', 'eyes']

IMAGE_PATH = sys.argv[1]

model = OCR(API_KEY, CATEGORIES, model_id=MODEL_ID)

result = model.predict_for_file(IMAGE_PATH)
print(result)

