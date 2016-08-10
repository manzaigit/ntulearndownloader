import os, requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from settings import NTULEARN_URL

# insert loginmethod here
def ntu_login(username, password):

    auth = {'user_id': username, 'password': password}

    s = requests.Session()
    s.post(NTULEARN_URL, data=auth)

    return s


givenurl = input("Enter URL: ")

html_code = requests.get(givenurl)
clean_html = BeautifulSoup(html_code.content,"html.parser")

valid_filelinks = []

for link in clean_html.find_all("a", href=True):
    parsed_link = urlparse(link.get('href'))
    if parsed_link.path[-4:] == '.pdf':
        valid_filelinks.append(link.get('href'))

for valid_links in valid_filelinks:
    print(valid_links)
print("%d file(s) discovered." % len(valid_filelinks))

if(len(valid_filelinks)):
    decide_to_save = input("Would you like to save them all? (Y/N): ")

    if decide_to_save.upper() == 'Y':

        download_path = input("Enter download path: ")

        for file in valid_filelinks:
            download_link = urljoin(givenurl, file)

            f = open(download_path + "\\" + os.path.basename(file), mode = 'wb')
            f.write(requests.get(download_link).content)
            f.close()

    else: print("byebye! :)")
else:
    print("There aren't any files to download. Byebye!")