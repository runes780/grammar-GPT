import openai
import requests
import json

# 输入问题
question = input("请输入语法问题：")

url = "https://chatgpt-api.shn.hk/v1/"
data = {
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": "You are a good grammar teacher who can solve any grammar question or to analyze structure for sentences. You will try to explain the important grammar rules and concepts in a simple and clear way."},
    {"role": "user", "content": question}
    ]
}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)

s = response.text # 把Response对象转换成字符串
d = json.loads(s) # 把字符串转换成字典

# 使用response.text

text = d['choices'][0]['message']['content']
print(text)







