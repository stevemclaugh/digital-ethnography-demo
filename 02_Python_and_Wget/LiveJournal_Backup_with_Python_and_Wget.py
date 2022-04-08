## You'll need to install Wget first: 
## https://iffybooks.net/wp-content/uploads/zines/Iffy_Books_Wget_Zine_screen.pdf

import subprocess
import os
import time
import random

## Change directory to the desktop
os.chdir(os.path.expanduser('~/Desktop/'))

## Initialize pagination variable
skip_value = 0

############################################
## Choose a LiveJournal URL
home_url = "https://imomus.livejournal.com"
############################################

## Removing slash from end of URL
home_url = home_url.strip("/")

## Run the scrape
# If the LiveJournal account has <20K posts, this script will download every post (excluding comments)
for i in range(1000): 
    ## Generate current URL
	current_page_url = f"{home_url}/?skip={skip_value}"
    
    ## Create Wget command as a list
	wget_command_list = ["wget", "-c", "--convert-link", "-np", "--page-requisites", "-erobots=off", '''--tries="inf"''', "--wait=0.6", "--random-wait", '''--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0"''', current_page_url]
    
    ## Call Wget command
	subprocess.call(wget_command_list)
    
    ## Pause 0.5 to 1.5 seconds
	time.sleep(0.5 + random.random())
    
    ## Update pagination variable
	skip_value += 20
