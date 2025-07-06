import requests, json, os

def send_slack_alert(webhook_url: str, text: str):
    payload = {"text": text}
    resp = requests.post(webhook_url, data=json.dumps(payload), timeout=5)
    resp.raise_for_status()