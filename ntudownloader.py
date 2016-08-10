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

def page_pdf_downloader(givenurl,download_path,s):

    html_code = s.get(givenurl)
    clean_html = BeautifulSoup(html_code.content,"html.parser")
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

    if(len(valid_filelinks)):
        decide_to_save = input("Would you like to save them all? (Y/N): ")

        if decide_to_save.upper() == 'Y':

            for file,name in zip(valid_filelinks,valid_filenames):
                download_link = urljoin(givenurl, file)

                f = open(download_path + "\\" + name, mode = 'wb')    # might not need to import os anymore
                f.write(s.get(download_link).content)
                f.close()

        else: print("byebye! :)")
    else:
        print("There aren't any files to download. Byebye!")
