import openai
import requests
import json

with open("input.txt", "r", encoding="utf-8") as f: # 打开文件
    data = f.read() # 读取所有内容
data = data.replace(" ", "")
data = data.replace("\\n", "") 
# 输入问题
question = input("请输入语法问题：")

url = "https://chatgpt-api.shn.hk/v1/"
data = {
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": ""},
    {"role": "user", "content": data}
    ]
}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)

s = response.text # 把Response对象转换成字符串
d = json.loads(s) # 把字符串转换成字典

# 使用response.text

text = d['choices'][0]['message']['content']

with open("grammar.txt", "a", encoding="utf-8") as f:
      now = datetime.datetime.now()
      date = now.strftime("%Y-%m-%d")
      time = now.strftime("%H:%M:%S")
      f.write('\n' + '\n' + f"当前的日期是{date}，当前的时间是{time}\n"+text)
print(text)