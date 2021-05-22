import re
import json
import requests

res = requests.get("https://xwl.io/archives/")

tags = re.findall(r'href="([a-zA-z]+://[^\s]*)"', str(res.text))

urls = []
for t in tags:
    if t.endswith("css") or t.endswith("js"):continue
    if not t.startswith("https://xwl.io"):continue
    urls.append(t)

urls = "\n".join(urls)

headers = {"Content-Type": "text/plain"}
resp = requests.post("http://data.zz.baidu.com/urls?site=https://xwl.io&token=ZMBvO1Tb3IDz4XUs", headers=headers, data=urls)
print(resp.text)
