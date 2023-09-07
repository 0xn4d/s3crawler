import requests
import re
import sys
import urllib3
import pyfiglet
# from pysecuritytrails import SecurityTrails, SecurityTrailsError
# from dotenv import load_dotenv
# import os

# load_dotenv()
urllib3.disable_warnings()
file = sys.argv[1]
# SECTRAILS_API_KEY = os.getenv('SECTRAILS_API_KEY') 
# st = SecurityTrails(SECTRAILS_API_KEY)

# try:
#     st.ping()
# except SecurityTrailsError:
#     print('Ping failed')
#     sys.exit(1)

initialBanner = pyfiglet.figlet_format('s3crawler')
print(initialBanner)

with open(file, 'r') as f:
    for domain in f:
        print(f'Testing domain: {domain}')

        try:
            response = requests.get(domain, verify=False)
            response_content = response.content
            response_content_decoded = response_content.decode('utf-8')
            if response.status_code != 200:
                print(f'HTTP Status code: {response.status_code}')
        except requests.exceptions.RequestException:
            print('This one just timed out.')

        patterns = [
            r"https://[a-z0-9.-]{3,63}\.s3-us-east-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-us-east-2\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-us-west-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-us-west-2\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-ap-south-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-ap-south-2\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-ap-northeast-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-ap-northeast-2\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-ap-southeast-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-ap-southeast-2\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-ca-central-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-cn-north-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-cn-northwest-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-eu-central-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-eu-west-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-eu-west-2\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-eu-west-3\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-sa-east-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-us-gov-east-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-us-gov-west-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-me-south-1\.amazonaws\.com/",
            r"https://[a-z0-9.-]{3,63}\.s3-af-south-1\.amazonaws\.com/",
        ]

        matches = []

        for pattern in patterns:
            matches.extend(re.findall(pattern, response_content_decoded))

        print()
        print("Possible Buckets S3 to test:")
        print()
        print(matches)
        print()
            

