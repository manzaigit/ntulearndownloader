import sys, getopt

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

    print("Your ntu username is: " + username)
    print("Your ntu password is: " + password)

if __name__ == "__main__":
    main(sys.argv[1:])
