
import os
import datetime

def send_whatsapp_alert(message, snapshot_path=None):
    """
    Simulates sending a WhatsApp alert to the school security team.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    alert_log = f"[{timestamp}] WHATSAPP ALERT: {message}"
    if snapshot_path:
        alert_log += f" | Snapshot: {snapshot_path}"
    
    print(alert_log)
    
    # In a real implementation, you would use the Twilio API or similar here:
    # client = Client(account_sid, auth_token)
    # client.messages.create(body=message, from_='whatsapp:+14155238886', to='whatsapp:+91...')
    
    return True
