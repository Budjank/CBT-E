# Author  :  D3n0l  Ganz
# Team    :  Indonesian Sad Cyber
# Version :  1.0
# Date    :  21/09/2018

import sys
import httplib
import socket

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

class cbt():
    print ""
    print bcolors.HEADER + "\t##########################################" + bcolors.ENDC
    print bcolors.HEADER + "\t#     Author  :  D3n0l Ganz              #" + bcolors.ENDC
    print bcolors.HEADER + "\t#     Team    :  Indonesian Sad Cyber    #" + bcolors.ENDC
    print bcolors.HEADER + "\t#     Version :  V.1                     #" + bcolors.ENDC
    print bcolors.HEADER + "\t#     Date    :  21/09/2018              #" + bcolors.ENDC
    print bcolors.HEADER + "\t##########################################" + bcolors.ENDC
    print ""

    def __init__(self):
        self.exploiter()

    def exploiter(self):
        try:
            try:
                site = raw_input(bcolors.BLUE + "Target : " + bcolors.ENDC)
                site = site.replace("http://", "")
                print bcolors.YELLOW + "\n\t[*] Checking the website " +  site + bcolors.ENDC
                conn = httplib.HTTPConnection(site)
                conn.connect()  # Connecting the website
                print bcolors.GREEN + "\t[+] Connection Established, It's Online.\n" + bcolors.ENDC
            except (httplib.HTTPResponse, socket.error) as Exit:
                print bcolors.RED + "\t[!] Cannot Connect the Website, It might be offline or invalid URL.\n" + bcolors.ENDC
                sys.exit()

            print bcolors.YELLOW + "\t[*] Scanning: " + site + bcolors.ENDC + "\n"
            

            # Wordlist CBT Exploit
            wordfile = open("exploit.txt", "r")
            wordlist = wordfile.readlines()
            wordfile.close()

            for word in wordlist:
                upload = word.strip("\n")
                upload = "/" + upload
                target = site + upload
                print bcolors.YELLOW + "[*] Checking: " + target + bcolors.ENDC
                connection = httplib.HTTPConnection(site)
                connection.request("GET", upload)
                response = connection.getresponse()


                
                if response.status == 200:
                    print bcolors.GREEN + "\n\n\t+------------------------------------------------------+" + bcolors.ENDC
                    print "%s %s" % (bcolors.GREEN + "[!] Disini >> " + bcolors.ENDC, bcolors.GREEN + target + bcolors.ENDC)
                    print bcolors.GREEN + "\t+------------------------------------------------------+\n" + bcolors.ENDC
                elif response.status == 302:
                    print bcolors.RED + "[!] 302 Object moved temporarily.\n" + bcolors.ENDC

                elif response.status == 404:
                    print bcolors.RED + "[!] 404 Web Page Not Found.\n" + bcolors.ENDC

                elif response.status == 410:
                    print bcolors.RED + "[!] 410 Object removed permanently.\n" + bcolors.ENDC
                
                else:
                    print "\n[!] ERROR JANCOK [!]\n"
                connection.close()

        except (httplib.HTTPResponse, socket.error):
            print bcolors.RED + "\n\t[!] Session Cancelled, An Error Occured." + bcolors.ENDC
            print bcolors.RED + "\t[!] Check Your Internet Connection" + bcolors.ENDC
        except (KeyboardInterrupt, SystemExit):
            print bcolors.RED + "\t[!] Session Interrupted and Cancelled." + bcolors.ENDC

if __name__ == "__main__":
    cbt()
