#import these lines to get extra functionality out of Sikuli
from sikuli.Sikuli import *
import os
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)
from groovesharkTest import *

# instantiate the class where we defined the functionality

g = groovesharkTest()

#use try/except to determine whether a part of the test passed or failed
try:
	# open the music player GrooveShark
	g.openFirefox()
	g.inputUrl("http://grooveshark.com/")
	wait(7)
	g.passed("openGrooveshark")

except FindFailed:
	g.criticalError("openGrooveshark")

try:
	# play all of the songs in the favorites playlist
	g.searchForMusic("weezer")
	g.passed("weezerSearch")
except FindFailed:
	g.failed("weezerSearch")

for i in range(len(g.termsArr)):	
	try:
		g.searchForMusic(g.termsArr[i])
		g.passed("MusicSearch term = " + g.termsArr[i])
	except FindFailed:
		g.failed("MusicSearch term = " + g.termsArr[i])

g.closeBrowser()
g.passed("close")
# done
print("TEST COMPLETE")
exit()

