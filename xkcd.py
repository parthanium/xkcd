import urllib.request,os,random,tkinter.filedialog
import re, argparse

description = '''Romance,Sarcasm,Math and Language
Welcome to xkcd Downloader 1.0
'''
argument_description='''
Accepted Inputs :
all : downloads all xkcd comics from the beginning to the latest one
first : downloads the first xkcd comic
latest : downloads the latest xkcd comic
random : downloads a random xkcd comic
[Any number] : downloads the xkcd comic of that number',' ','Example:67
[Range] : downloads the xkcd comics in that range',' ','Example:5-19
If no input is given : downloads the latest xkcd comic by default
\nYou can also specify the directory you want to download the comic(s) to.
Default directory is the current working directory.
'''

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def f(n):
    # n is expected to be an int, convert to str
    if int(n) <= 0:
        exit("{0} is not a valid comic number")
    n=str(int(n)) # to be really sure
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
            # Remove any title characters that can't be in a filename
            title = re.sub("[/]",'_',title)
            # Clear any additional text before HTTP
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
        #print(newest)
        return int(newest)
    except urllib.error.URLError:
        print('Network Error')
        print('Try again later')
        exit()
        return 0

# Load optional command line arguments with argparse
epilog=argument_description
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,description=description,epilog=epilog)
parser.add_argument("--nogui",default=False,action="store_true",help="use text only input and automatically exit on completion")
parser.add_argument('--dest',default=False, help="destination directory")
parser.add_argument("--comic",default=False,action="store", help="see accepted inputs below")
options = parser.parse_args()

print(description)

print('Latest comic number : '+ str(latest()) + '\n')
#Taking the input
if options.comic:
    number=options.comic
else:
    print(argument_description)
    number = str(input('Enter the xkcd comic number : '))

#Taking the download directory
if options.dest:
    dir=os.path.abspath(options.dest)
else:
    if options.nogui:
        dir = str(input('Enter a destination directory : '))
    else:
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
    f(latest())
elif number == 'first':
    f(1)
elif number == 'random':
    val = str(random.randint(1, latest()))
    f(val)
elif number == 'all':
    for o in range(1,latest()):
        f(o)
            
elif position > 0:
    #For the range input
    ll = int(number[0:position])
    ul = int(number[position+1:len(number)])
    if ul>ll and ul <= (latest()) and ll>0:
        for i in range(ll,ul+1):
            f(i)
            
    elif ul>(latest()) or ll <=0:
        print('Invalid range ...')
    else:
        print('Invalid range ...')
else:
    try:
        if 1 <= int(number) <= (latest()):
            #Calling the function for a direct input
            f(number)
        elif int(number) > (latest()):
            print('Not yet published ...')
        elif int(number) <= 0:
            print('Enter a number between 1 and the latest ...')
    except ValueError:
            print('Invalid input')

if options.nogui:
    print("Download complete")
else:
    x = input('\nPress Enter to exit ...')
