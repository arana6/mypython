from urllib2 import Request,urlopen, URLError
import json
from pprint import pprint




request=Request("https://api-us02.kurtosys.io/taxonomygroup/getlist?path=holdings&entityids=1000882844&languageid=6685&countryid=9039&propertyids=8989,40397625,40397627,40396727,40392197,8600,9029,40397736,40397730,40397734,40397732&verbosity=1&entitytypeid=4617&includelinkedobjectproperties=true&includegroupobjectproperties=true&strongpropertytypes=1&_api_key=E7B34B8D-5388-4898-A44D-FB3AF9A9FEC0&_user_token=C8BCB27B-FF2A-4392-B6C8-E5A868AC32EE")

try:
    response=urlopen(request)
    output=response.read()
    jsonvar=output

except URLError, e:
    print URLError

jnewfile=raw_input("Enter name of json file :")
jnewfile=jnewfile+".json"
parsedjsonvar=json.loads(jsonvar)


ofile=open(jnewfile,'w')
ofile.write(json.dumps(parsedjsonvar,indent=2))
ofile.close()

jsonreadagain=open(jnewfile).read()
print jsonreadagain
#parsed=json.loads(jsonreadagain)


#print "open the file manually now"
#print json.dumps(parsed,indent=2)
