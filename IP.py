#
# import regex as re
#
# data = input("Enter data: ")
# ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
#
# ip_addresses = re.findall(ip_pattern, data)
#
# print("IP addresses found in the input data:")
# for ip in ip_addresses:
#     print(ip)


import requests
import time
import logging
from concurrent.futures import ThreadPoolExecutor

API_KEY = 'de37dac1fb285e94b5c475d26d511e28e63fbd03771e4c65a1b155d7cb9e084d'
url = 'https://www.virustotal.com/api/v3/ip_addresses/'

logging.basicConfig(filename='ip_checker.log', level=logging.INFO)

def check_ipv4_with_virustotal(ip):
    headers = {'x-apikey': API_KEY}

    try:
        response = requests.get(url + ip, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error while querying {ip}: {e}")
        return None

    if response.status_code == 200:
        logging.info(f"API Callback for {ip} successful")
        return response.json()
    else:
        logging.error(f"Error while querying {ip}. Status Code: {response.status_code}")
        return None

def process_ip(idx, ip):
    result = check_ipv4_with_virustotal(ip)
    if result is not None:
        status = "Malicious" if result['data']['attributes']['last_analysis_stats']['malicious'] > 0 else "Not Malicious"
        print(f'Processed {idx + 1}/{len(ip)} - {ip} is {status}')
        return (ip,status)
    else:
        print(f'Error processing {ip}. Skipping.')
        return None

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        ips = f.read().splitlines()

    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        for idx, ip in enumerate(ips):
            result = executor.submit(process_ip, idx, ip).result()
            if result is not None:
                results.append(result)
            time.sleep(3)

    with open(output_file, 'w') as f:
        for ip, status in results:
            f.write(f'{ip}: {status}\n')

if __name__ == '__main__':

    input_file = '/home/bhudev/PycharmProjects/pythonProject/ip_checker.log'
    output_file = '/home/bhudev/PycharmProjects/pythonProject/ip_checker (copy).log'

    main(input_file, output_file)


