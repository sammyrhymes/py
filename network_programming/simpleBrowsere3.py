import urllib.request
import re

# URL 1
url1 = 'http://www.dr-chuck.com/page1.htm'
while True:
    url2 = ''

    # Open the URL and retrieve the HTML content
    fhand = urllib.request.urlopen(url1)

    # Decode the data and print it line by line
    for line in fhand:
        text = line.decode().strip()

        # Check for links using regex
        pattern = r'<a\s+href=(?:"([^"]+)"|\'([^\']+)\'|([^ >]+)).*>'
        match = re.search(pattern, text)
        if match:
            link = match.group(1) or match.group(2) or match.group(3)
            print(link)

            if link == '':
                break

            # Copy the link to URL 2
            url2 = link
            break

    # Compare URL 1 and URL 2
    if url1 == url2:
        break

    url1 = url2  # Assign URL 2 to URL 1 for the next iteration

print("No more links found. Exiting...")
