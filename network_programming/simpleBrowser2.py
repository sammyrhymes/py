# import the neccesary urllib modules(request, parse and error)
import urllib.request , urllib.parse , urllib.error

# use urllib.request and urlopen() to open the link and get the encoded data 
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# decode the data and print it : remember to shred the empty lines using strip() function 
for line in fhand:
    print(line.decode().strip())