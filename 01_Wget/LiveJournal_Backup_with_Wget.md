## Download a series of URLs with Wget

To download the example code, go to the following URL. 

	https://github.com/stevemclaugh/digital-ethnography-demo

Click **Code > Download ZIP** to download the code. Then unzip the file on your computer. 

Open a terminal window. Then run the following command to change your current directory to `digital-ethnography-demo/01_Wget`:

	cd ~/Documents/GitHub/digital-ethnography-demo/01_Wget/

The file `LiveJournal_URLs.txt` contains a series of LiveJournal URLs, one URL per line:

	https://imomus.livejournal.com/?skip=0
	https://imomus.livejournal.com/?skip=20
	https://imomus.livejournal.com/?skip=40
	https://imomus.livejournal.com/?skip=60
	https://imomus.livejournal.com/?skip=80
	https://imomus.livejournal.com/?skip=100
	https://imomus.livejournal.com/?skip=120

Use the following **Wget** command to download every URL in the list:

	wget -i LiveJournal_URLs.txt

To stop Wget while it's running, you can press `ctrl+C`.

➡️ Try opening one of the downloaded pages in your browser.

➡️ Now turn off your wi-fi and try opening a downloaded page in your browser. Does it look different?

The `--continue` option will let Wget continue if the connection was previously interrupted. The `--wait=1` option will make Wget wait 1 second between downloads.

	wget --wait=1 --continue -i LiveJournal_URLs.txt


Try the same commands with the list of URLs in the file `IG_Bot_URLs.txt` and see what happens. Can you find any useful information (such as follower count) in the HTML files you download?

If you want to learn more about Wget, check out this zine: 
[https://iffybooks.net/wp-content/uploads/zines/Iffy_Books_Wget_Zine_screen.pdf](https://iffybooks.net/wp-content/uploads/zines/Iffy_Books_Wget_Zine_screen.pdf)


