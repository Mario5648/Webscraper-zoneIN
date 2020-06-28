from bs4 import BeautifulSoup
import requests

"""
How to Use


1. Go to a youtube channel in the video tabs.
2. scroll to the bottom of the channel
3. scroll up to the video and right click the first video title
4. click "inspect"
5. in the element viewer scroll up until you see <div id="contents"
6. right click the <div id="contents" and press copy and then copy element
7. paste it into a local file named htmlText.txt
8. Run the code
9. repeat



"""
htmlFile = open('htmlText.txt','r',encoding="utf8")

entertainmentFile = open('educationTest.txt','a',encoding="utf8")

soup = BeautifulSoup(str(htmlFile.read()),'html.parser')


videoTitles = soup.find_all(id='video-title')

for title in videoTitles:
    entertainmentFile.write(str(title.get_text())+"\n")

htmlFile.close()
entertainmentFile.close()
