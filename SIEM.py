import time
class SIEM:

    def __init__(self):

        self.events = []
    def log_event(self, event_type, message):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        event = {
            'timestamp': timestamp,
            'event_type': event_type,
            'message': message,
        }
        self.events.append(event)
        self.process_event(event)
    def process_event(self, event):
        print(f"Received event [{event['event_type']}]: {event['message']}")
if __name__ == "__main__":
    siem = SIEM()
    siem.log_event("Login Failed", "User 'admin' failed to log in.")
    siem.log_event("Access Denied", "Unauthorized access attempt detected.")
    siem.log_event("Malware Detected", "Malware 'TrojanXYZ' detected on host.")
    print("Logged Events:")
    for event in siem.events:
        print(event)

