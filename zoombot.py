import subprocess
import time
print(time.ctime())
def sign_in(link):
    if time.ctime() == "Thu Oct  7 17:46:00 2021":
        subprocess.call(['/usr/bin/open', link])
        subprocess.call(['/usr/bin/afplay', '99595927.mp3'])
while True:
    if time.ctime() == "Sun May  10 18:31:00 2021":
        sign_in('https://zoom.us/j/9379547462?pwd=YnRzNGh1VFJnN0pKcVdLQ3ExdnlLUT09')
    