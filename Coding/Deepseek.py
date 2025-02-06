# 首先请安装OpenAI SDK: `pip3 install openai`

from openai import OpenAI

# 创建一个OpenAI客户端，需要提供API密钥和基础URL
client = OpenAI(
    api_key="sk-f096000823ae40ba9347f8d77ae46636", 
    base_url="https://api.deepseek.com/v1"
)

# 使用客户端创建一个聊天会话，指定模型和消息
response = client.chat.completions.create(
    model="deepseek-chat",  # 指定使用的模型
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},  # 系统角色，内容是提示信息
        {"role": "user", "content": "Hello"},  # 用户角色，内容是用户的问候
    ]
)

# 打印出响应的第一个选择的内容
print(response.choices[0].message.content)
