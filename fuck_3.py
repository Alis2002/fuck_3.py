import os.path
import tempfile
import wget

link_http = "https://core.nsdigital.ru/stationsLogs/18-01-2022/M0074.txt"
#link_http = "http://91.215.202.217/getfile/test.txt"
local_link = r"C:/prog/quest/text.txt"



def getTextFile(pathFile):
    array_http_s = ["http://", "https://"]
    if any(pathFile.startswith(x)for x in array_http_s):
        print("url")
        try:
            temp_dir = tempfile.TemporaryDirectory()
            r_ead_open = open(wget.download(pathFile, temp_dir.name), "r+").read()
            temp_dir.cleanup()
            return r_ead_open
        except IOError as http_error:
            print(http_error)
            return False
    else:
        if os.path.exists(pathFile):
            r_ead_open = open(pathFile, "r+",encoding='utf-8').read().strip()
            return r_ead_open
        else:
            return



