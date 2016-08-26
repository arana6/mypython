import webbrowser
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "https://api-us02.kurtosys.io/tools/ksys317/fundProfile/ZC1G?locale=en-GB"

if "noRedirect"  not in url and url is not None:
    url=url+"&noRedirect"
else:
    print "YOLo"
webbrowser.open(url,new=new)



# open an HTML file on my own (Windows) computer
url = "https://api-us02.kurtosys.io/tools/ksys317/fundList?locale=en-GB#overview"

if "noRedirect" not in url and url is not None:
    url=url+"&noRedirect"
else:
        print "swag"

webbrowser.open(url,new=new)
