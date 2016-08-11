import sys, getopt
from ntudownloader import ntu_login, page_pdf_downloader

def usage():
    print("Usage: python main.py [-h|help] [-u|username=<args>] [-p|password=<args>]")

def main(argv):
    username = ""
    password = ""

    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["help", "username=", "password="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
        else:
            assert False, "unhandled option"

    s = ntu_login(username, password)
    givenurl = input("Enter NTULearn URL containing links to documents: ")
    download_path = input("Enter download path: ")
    page_pdf_downloader(givenurl, download_path, s)

if __name__ == "__main__":
    main(sys.argv[1:])
