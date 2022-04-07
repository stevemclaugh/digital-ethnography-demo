## You'll need to install Wget first: 
## https://iffybooks.net/wp-content/uploads/zines/Iffy_Books_Wget_Zine_screen.pdf

import subprocess
import os
import time
import random

## Change directory to the desktop
os.chdir(os.path.expanduser('~/Desktop/'))

## Initialize pagination value
skip_value = 0

###################################################
## Choose a LiveJournal URL (replace with your own)
home_url = "https://imomus.livejournal.com"
###################################################

## Removing slash from end of URL
home_url = home_url.strip("/")

## Run the scrape
# If your LJ has <20K posts, this script will grab everything (excluding comments)
for i in range(1000): 
	current_page_url = f"{home_url}/?skip={skip_value}"
	wget_command_list = ["wget", "-c", "--convert-link", "-np", "--page-requisites", "-erobots=off", '''--tries="inf"''', "--wait=0.6", "--random-wait", '''--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0"''', current_page_url]
	subprocess.call(wget_command_list)
	time.sleep(0.5 + random.random())
	skip_value += 20
