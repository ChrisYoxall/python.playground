# make a web request to google.com
import requests

from calculator import sum

from calculator.operations import sum as sum2

import subprocess

print('This line will be printed.')

x = 1
if x == 1:
    print("x is 1")

# response = requests.get("https://www.google.com")
# print(f"Status Code: {response.status_code}")
# for key, value in response.headers.items():
#     print(f"{key}: {value}")

print(f"My sum: {sum(1, 2)}")
print(f"My sum as module: {sum2(1, 2)}")

# Also have Popen.  See https://docs.python.org/3/library/subprocess.html
subprocess.run(["ls", "-l"])
