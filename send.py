import requests
from teamdetails import team
from datetime import datetime
import multiprocessing


def send_message(set_time, cid):
    print("started")
    while True:
        send_url = "https://discord.com/api/v9/channels/{}/messages"
        send_payload = {
            'content': f"{team}"
        }
        send_header = {
            "authorization": "NTY0MzE1MjMxMDQwNTY5MzU0.GPyldX.tl7GvWElz3J3uIhQBZ6kmTeFfw26qQVEXJcv18"
        }
        issent = True
        checktime = True
        while checktime:
            current_time = datetime.now().strftime("%H:%M:%S")
            if current_time == set_time:
                while issent:
                    response = requests.post(send_url.format(cid), data=send_payload, headers=send_header)
                    if len(response.json()) < 5:
                        continue
                    else:
                        issent = False
                        checktime = False
                        print("Message sent successfully!")



send_message("10:50:00", "907525794992099360")

# p1 = multiprocessing.Process(target=send_message, args=("09:09:00", "907525794992099360"))
# p2 = multiprocessing.Process(target=send_message, args=("09:11:00", "991611117518454784"))
#
# if __name__ == '__main__':
#     p1.start()
#     p2.start()

# OTkyMjk0ODE4NDI2NDAwOTA5.G8-FPO.wdhLX5VyozcukI8gjANk3e9hn0Ud6qvF8FIcIo
