import requests
import json
from datetime import datetime

DINGTALK_WEBHOOK = os.getenv('DINGTALK_WEBHOOK_URL')  # 从 Secret 读取

def send_to_dingtalk(content):
    data = {
        "msgtype": "text",
        "text": {"content": content}
    }
    requests.post(DINGTALK_WEBHOOK, json=data)

print("=== 上市公司舆情简报 ===")
print(datetime.now().strftime("%Y年%m月%d日"))

content = """客户舆情信息快报
信息科技处	""" + datetime.now().strftime("%Y年%m月%d日") + """

法律与合规风险方面
本期公开渠道暂未发现。

经营与财务风险方面
本期公开渠道暂未发现。

...（其他分类）

测试成功！Webhook 正常。
"""

send_to_dingtalk(content)
print("已推送至钉钉")
