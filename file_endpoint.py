'''
upload files

api token ==> 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

curl https://api.openai.com/v1/files \
  -H "Authorization: Bearer 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" \
  -F purpose="fine-tune" \
  -F file="@training_data.jsonl"

file id ==> file-IkMBlS29eCMxBJSqqrby9WK4

read files
curl https://api.openai.com/v1/files/file-IkMBlS29eCMxBJSqqrby9WK4/content \
  -H "Authorization: Bearer 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" > file.jsonl
  
'''

import requests

url = "https://api.openai.com/v1/files/file-ohYKIfrT7XegrdKIYZ0aVdeD/content"
headers = {
    "Authorization": "Bearer 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"}

response = requests.get(url, headers=headers)

with open("file.jsonl", "wb") as f:
    f.write(response.content)

url = "https://api.openai.com/v1/files"
headers = {
    "Authorization": "Bearer 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"
}
params = {
    "purpose": "fine-tune"
}
files = {
    "file": ("data.jsonl", open("data.jsonl", "rb"))
}

response = requests.post(url, headers=headers, params=params, files=files)

if response.status_code == 200:
    print("File upload successful!")
else:
    print(f"Error: {response.json()['error']['message']}")
