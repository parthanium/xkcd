xkcd Downloader
===============

Romance,Sarcasm,Math and Language

<h4>Welcome to xkcd Downloader 1.0 !</h4>
A Python 3 script to download xkcd comics.

<h2>Introduction:</h2>
xkcd Downloader is a very simple Python script I developed to kill time. Built on Python 3 it only depends on standard Python installation modules i.e. <code>urllib</code>,<code>random</code> and <code>os</code>
<h2>Download and Run:</h2>
<ul>
<li>Download this repository and extract it.</li>
<li>Place the file <code>xkcd.py</code> in the Python installation directory on your drive.</li>
<li>Double-click to execute or do it through the command line with the command <code>python xkcd.py</code>.</li>
<li>You will be greeted with a little introduction and help.</li>
<li>Give the required input to download the comics in <code>.jpg</code> format.</li>
<li>You will also be prompted to specify a file path for downloading the comic(s).</li>
<li>If no directory is specified, the comics will be downloaded to the directory of the script</li>
<li>The comic(s) will be downloaded in the same directory as the script with their respective titles</li>
<li>Enjoy !
</ul>
<h2>Dependencies:</h2>
<ul>
<li>Python 3</li>
</ul>
<h2>Accepted Inputs :</h2>

|Input|Action|Example|
|-----|------|-------|
|all | downloads all xkcd comics from the beginning to the latest one|<code>all</code>|
|first | downloads the first xkcd comic|<code>first</code>|
|latest | downloads the latest xkcd comic|<code>latest</code>|
|random | downloads a random xkcd comic|<code>random</code>|
|[Any number] | downloads the xkcd comic of that number|<code>67</code>|
|[Range] | downloads the xkcd comics in that range|<code>5-19</code>|
|[Default]| downloads the latest xkcd comic by default|<code></code>|

All Rights Reserved by Randall Munroe and http://www.xkcd.com
