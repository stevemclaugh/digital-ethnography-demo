
Change your current directory:

	cd ~/Documents/Digital_Ethnography_Demo/01 Wget/

Download a list of URLs with the following command:

	wget -i LiveJournal_URLs.txt

To stop Wget, you can press ctrl+C.

Try opening one of the downloaded pages in your browser.

Now turn off your wi-fi and try opening a downloaded page in your browser. Does it look different?

Add a few more useful options to your Wget command:

	wget --wait=1 --continue -i LiveJournal_URLs.txt


Try the same commands with the list of URLs in the file `IG_Bots.txt` and see what happens. Can you find any useful information (such as follower count) in the HTML files you download?

If you want to learn more about Wget, check out this zine: 
https://iffybooks.net/wp-content/uploads/zines/Iffy_Books_Wget_Zine_screen.pdf


