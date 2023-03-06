import requests
import json
import openai
import datetime
with open("ANKI-input.txt", "r", encoding="utf-8") as f: # 打开文件
    data = f.read() # 读取所有内容
    
# 输入问题
question = data

url = "https://chatgpt-api.shn.hk/v1/"
data = {
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": "请根据我提供的文本，制作一套抽认卡。在制作抽认卡时，请遵循下述要求：- 保持抽认卡的简单、清晰，并集中于最重要的信息。- 确保问题是具体的、不含糊的。- 使用清晰和简洁的语言。使用简单而直接的语言，使卡片易于阅读和理解。- 答案应该只包含一个关键的事实/名称/概念/术语。制作抽认卡时，让我们一步一步来：第一步，使用简单的中文改写内容，同时保留其原来的意思。第二步，将内容分成几个小节，每个小节专注于一个要点。第三步，利用小节来生成多张抽认卡，对于超过 15 个字的小节，先进行拆分和概括，再制作抽认卡。"},
    {"role": "user", "content": question}
    ]
}
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=data, headers=headers)
s = response.text # 把Response对象转换成字符串
d = json.loads(s) # 把字符串转换成字典

# 使用response.text

text = d['choices'][0]['message']['content']
with open("ANKI-output.txt", "a", encoding="utf-8") as f:
      now = datetime.datetime.now()
      date = now.strftime("%Y-%m-%d")
      time = now.strftime("%H:%M:%S")
      f.write('\n' + '\n' + f"当前的日期是{date}，当前的时间是{time}\n"+text)
print(text)