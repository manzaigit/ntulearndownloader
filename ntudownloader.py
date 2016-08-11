import os, requests
from bs4 import BeautifulSoup
from settings import NTULEARN_URL
from urllib.parse import urlparse, urljoin


def ntu_login(username, password):

    auth = {'user_id': username, 'password': password}

    s = requests.Session()
    s.post(NTULEARN_URL, data=auth)

    return s


def page_pdf_downloader(download_url, download_path, s):

    html_code = s.get(download_url)
    clean_html = BeautifulSoup(html_code.content, "html.parser")
    valid_filelinks = []
    valid_filenames = []

    for link in clean_html.find_all("a", href=True):
        parsed_link = urlparse(link.get('href'))
        if parsed_link.path[:12] == '/bbcswebdav/':
            valid_filelinks.append(link.get('href'))
            valid_filenames.append(link.text[1:])

    for name in valid_filenames:
        print(name)
    print("%d file(s) discovered." % len(valid_filelinks))

    if len(valid_filelinks) < 1:
        return

    decide_to_save = input("Would you like to save them all? (Y/N): ")
    if decide_to_save.upper() != 'Y':
        return

    num_files_downloaded = len(valid_filelinks)
    for file, name in zip(valid_filelinks, valid_filenames):
        try:
            download_link = urljoin(download_url, file)
            with open(download_path + "\\" + name, mode='wb') as f:
                f.write(s.get(download_link).content)
        except IOError:
            num_files_downloaded -= 1

    print("%d file(s) was downloaded" % num_files_downloaded)
