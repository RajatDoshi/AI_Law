'''
curl --location --request POST 'https://api.openai.com/v1/fine-tunes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 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' \
--data-raw '{
  "training_file": "file-IkMBlS29eCMxBJSqqrby9WK4",
  "model":"ada",
  "suffix":"ai-law-finetune"
}'
'''

import requests

url = 'https://api.openai.com/v1/fine-tunes'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}
data = {
    'training_file': 'file-IkMBlS29eCMxBJSqqrby9WK4',
    'model': 'ada',
    'suffix': 'ai-law-finetune'
}

response = requests.post(url, headers=headers, json=data)
print(response.json())
