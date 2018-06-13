import urllib.request,os,random,tkinter.filedialog
import re
print('Romance,Sarcasm,Math and Language\nWelcome to xkcd Downloader 1.0\n\nAccepted Inputs :')
print('all : downloads all xkcd comics from the beginning to the latest one')
print('first : downloads the first xkcd comic')
print('latest : downloads the latest xkcd comic')
print('random : downloads a random xkcd comic')
print('[Any number] : downloads the xkcd comic of that number',' ','Example:67')
print('[Range] : downloads the xkcd comics in that range',' ','Example:5-19')
print('If no input is given : downloads the latest xkcd comic by default')
print('\nYou can also specify the directory you want to download the comic(s) to.')
print('Default directory is the current working directory.\n')
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def f(n):
    try:

        #Now finding the link of the comic on the page
        if str(n)=="404":
            print("404: comic not found!")
            link='https://www.explainxkcd.com/wiki/images/9/92/not_found.png'
            title='404'
            return
        else:
            page = 'http://xkcd.com/' + n + '/'
            response = urllib.request.urlopen(page)
            text = str(response.read())
            if n=='1037':
                print("UMWELT")
                link='https://www.explainxkcd.com/wiki/images/f/ff/umwelt_the_void.jpg'
                return
            elif n=='1608':
                print("1608 Hoverboard game")
                link='https://www.explainxkcd.com/wiki/images/4/41/hoverboard.png'
                return
            elif n=='1663':
                print("1663 Garden")
                link='https://www.explainxkcd.com/wiki/images/c/ce/garden.png'
                return
            else:
                ls = text.find('embedding')
                le = text.find('<div id="transcript"')
                link = text[ls+12:le-2]
            #Now finding the title of the comic
            ts = text.find('ctitle')
            te = text.find('<ul class="comicNav"')
            title = text[ts+8:te-8]
            title = cleanhtml(title)
            title = re.sub("[/]",'_',title)
            link=re.sub(re.compile(".*http[s]*://",re.I),'https://',link)
        print("Link: {0}".format(link))
        if link[-4:-3]=='.':
            ext=link[-4:]
        else:
            ext=".jpg"
        img = "%04d" % int(n) + '-'+ title + ext
        #Now downloading the image
        print('Now downloading - '+ img)
        urllib.request.urlretrieve(link,img)
        print('Done')
    except urllib.error.URLError:
        print("URL error")
        exit()

def latest():
    try:
        new = urllib.request.urlopen('http://xkcd.com')
        content = str(new.read())
        #Now finding the latest comic number
        ns = content.find('this comic:')
        ne = content.find('<br />\\nImage URL')
        newest = re.sub('[^\d]','',content[ns+28:ne-1])
        print(newest)
        return int(newest)
    except urllib.error.URLError:
        print('Network Error')
        print('Try again later')
        exit()
        return 0

print('Latest comic number : '+ str(latest()) + '\n')
#Taking the input
number = str(input('Enter the xkcd comic number : '))
#Taking the download directory
print('Choose the directory to download the files to : ')
dir = tkinter.filedialog.askdirectory()
try:
    os.chdir(dir)
except OSError:
    print('Invalid directory')
    print('Switching to default ...')
    
#Declaring a variable for the range input
position = number.find('-')

if number == 'latest' or number == '':
    f(str(latest()))
elif number == 'first':
    f(str(1))
elif number == 'random':
    val = str(random.randint(1, latest()))
    f(str(latest()))
elif number == 'all':
    for o in range(1,latest()):
        f(str(o))
            
elif position > 0:
    #For the range input
    ll = int(number[0:position])
    ul = int(number[position+1:len(number)])
    if ul>ll and ul <= (latest()) and ll>0:
        for i in range(ll,ul+1):
            f(str(i))
            
    elif ul>(latest()) or ll <=0:
        print('Invalid range ...')
    else:
        print('Invalid range ...')
else:
    try:
        if 1 <= int(number) <= (latest()):
            #Calling the function for a direct input
            f(str(number))
        elif int(number) > (latest()):
            print('Not yet published ...')
        elif int(number) <= 0:
            print('Enter a number between 1 and the latest ...')
    except ValueError:
            print('Invalid input')

x = input('\nPress Enter to exit ...')
