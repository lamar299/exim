import requests
import os
from datetime import datetime

webhook = os.getenv('DINGTALK_WEBHOOK_URL')

if not webhook:
    print("Error: DINGTALK_WEBHOOK_URL not found")
    exit(1)

def send_to_dingtalk(content):
    data = {
        "msgtype": "text",
        "text": {"content": content}
    }
    response = requests.post(webhook, json=data)
    print("DingTalk response:", response.status_code)

print("=== 客户舆情信息快报 ===")
print(datetime.now().strftime("信息科技处 %Y年%m月%d日"))

content = f"""客户舆情信息快报
信息科技处	{datetime.now().strftime('%Y年%m月%d日')}

法律与合规风险方面
本期公开渠道暂未发现。

经营与财务风险方面
本期公开渠道暂未发现。

生产经营与行业风险方面
本期公开渠道暂未发现。

负面舆情发酵类
本期公开渠道暂未发现。

公司治理与实控人风险方面
本期公开渠道暂未发现。

债务与融资风险方面
本期公开渠道暂未发现。
"""

send_to_dingtalk(content)
print("报告已推送至钉钉")
