This is a punch IN/OUT program designed to keep track of people entering in 
or out of a building. It's meant to be used with an ID card with two 
barcodes that have the persons full name with "IN/OUT" at the end. The 
program saves all the files as .txt files so it should work with any 
windows machine that has python 2.7 installed.


Python 2.7 must be installed on your machine!


Setup:

	1.Create/find the folders you'd like to keep all the data files in.
	
	2.Move "punchout.py","punchoutclasses.py","SETTINGS.txt", and
	"LIVE LIST.txt" into the folder.
	
	3.Open the "SETTINGS.txt" file and change the directories to the ones
	your computer that you will be using. You can also change the file 
	type and time it takes for a check in to expire. But default settings
	are fine. Save the file and close it.

	4.Run the "punchout.py" file in the same folder as "SETTINGS.txt"
	and viola!


Usage:

	* To sign someone in type "Jon Doe IN" [minus qoutes].
	And last names are optional, so you could do "Jon IN" as well.

	* To sign someone out type "Jon Doe OUT" or what ever name you want.
	It just needs to be spelled the same, the program ignores case. The 
	persons name should then disappear from the list.

	* To toggle between viewing modes enter the word "mode" and it will
	display the last 25 logs instead of whose currently checked in. After
	a few more logs entered it will switch back to the default mode or 
	you can type "mode" again and switch it back.

	* If someone has been checked as "IN" for more than half of the
	expiration time it will be displayed as "EXPIRED". If they have been
	checked as "IN" for more than the expiration time they will be 
	checked out automatically and logged as "EXPIRED"



For creating ID cards like the program was intended to be used with, you 
would want two barcodes on the card like this:

Barcode 1: "Jon Doe IN"
Barcode 2: "Jon Doe OUT"

The barcodes should just be those strings as plain text. You can use most 
standard barcode scanners for this. Most barcode scanners also have the 
option to automatically "PRESS ENTER" after a code is scanned. This option 
should be turned ON.

Of course since it's just entering a string you can also manually type the
names as you see them above, minus the qoutes, and then press enter.


Example of what the program looks like:


    DATE       TIME         NAME            SURNAME                 CHECKED
    ------------------------------------------------------------------------
    2016-12-30 13:27:39     MASTER          BLASTER                 EXPIRED
    2016-12-31 13:27:57     HAN             SOLO                    IN
    2016-12-31 13:28:08     DONALD          DUCK                    IN
    2016-12-31 13:28:25     JON             DOE                     IN
    2016-12-31 13:28:36     DONALD          TRUMP                   IN
    2016-12-31 13:28:55     CHARLES         DARWIN                  IN
    2016-12-31 13:32:15     JOE             BLOW                    IN
    ------------------------------------------------------------------------
                                                           07 TOTAL IN
    ------------------------------------------------------------------------



    SCAN ID CARD:


