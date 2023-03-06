import requests
import json
import openai
import datetime
import re
import csv
import pandas as pd
with open("ANKI-input.txt", "r", encoding="utf-8") as f: # 打开文件
    data = f.read() # 读取所有内容
data = data.replace(" ", "")
data = data.replace("\\n", "") 

    
# 输入问题
question = data

url = "https://chatgpt-api.shn.hk/v1/"
data = {
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": "请根据我提供的文本，使用中文制作一套抽认卡，输出格式为”问题“和”答案“。在制作抽认卡时，请遵循下述要求：- 保持抽认卡的简单、清晰，并集中于最重要的信息。- 确保问题是具体的、不含糊的。- 使用清晰和简洁的语言。使用简单而直接的语言，使卡片易于阅读和理解。- 答案应该只包含一个关键的事实/名称/概念/术语。制作抽认卡时，让我们一步一步来：第一步，使用简单的中文改写内容，同时保留其原来的意思。第二步，将内容分成几个小节，每个小节专注于一个要点。第三步，利用小节来生成多张抽认卡，对于超过 15 个字的小节，先进行拆分和概括，再制作抽认卡。"},
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



# 定义问题和答案的关键字
question_keyword = "问题："
answer_keyword = "答案："

# 创建一个空列表来存储问题和答案
result = []

# 使用正则表达式找到所有问题和答案的位置
question_matches = re.finditer(question_keyword, text)
answer_matches = re.finditer(answer_keyword, text)

# 遍历每个匹配，提取文本并添加到列表中
for question_match, answer_match in zip(question_matches, answer_matches):
    # 获取问题和答案的起始和结束位置
    question_start = question_match.end()
    question_end = answer_match.start()
    answer_start = answer_match.end()
    answer_end = text.find("\n", answer_start)

    # 提取问题和答案的文本，并去除多余的空格和换行符
    question_text = text[question_start:question_end].strip()
    answer_text = text[answer_start:answer_end].strip()

    # 将问题和答案作为一个元组添加到列表中
    result.append((question_text, answer_text))

# 将列表转换为pandas数据框，并指定列名为"Question"和"Answer"
df = pd.DataFrame(result, columns=["Question", "Answer"])

# 将数据框写入csv文件，不包含索引或标题行
df.to_csv("output.csv", index=False, header=True, encoding='utf_8_sig')
