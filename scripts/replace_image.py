import os
import requests
import re
from urllib.parse import urlparse

def file_existed(url):
    destination_path = os.path.join('.\\source\\images\\flickr', *construct_folder(url))
    return os.path.exists(destination_path)

def construct_folder(url):
    paths = urlparse(url).path.split('/')
    return list(filter(lambda s: s.strip(), paths))

def download_file(url, destination_folder):
    response = requests.get(url)
    if response.status_code == 200:
        # filename = os.path.basename(urlparse(url).path)
        destination_path = os.path.join(destination_folder, *construct_folder(url))
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        with open(destination_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded file from {url} to {destination_path}")
    else:
        print(f"Failed to download file from {url}")

def process_text_file(file_path, destination_folder):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        line = line.strip()
        match = re.search(r'\((.*?)\)', line)
        if match:
            url = match.group(1)
            if 'staticflickr' in url:
                if(file_existed(url)):
                    modified_line = re.sub(r'(http://farm\d+\.staticflickr\.com/(\d+)/(\d+)_([a-zA-Z0-9_]+)\.jpg)', r'/images/flickr/\2/\3_\4.jpg', line)
                    modified_lines.append(modified_line)
                # downloaded in step 1
                # else:
                #     download_file(url, destination_folder)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

def main(folder_path, destination_folder):
    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_text_file(file_path, destination_folder)

# Example usage:
folder_path = '.\\source\\_posts'
destination_folder = '.\\test\\'
main(folder_path, destination_folder)