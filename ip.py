••• IP Tracer •••
              
    You can get any one's IP Address Information by giving input their IP.
    
   • Paste the input in the input Box. 
   
   • Input : 
    
        203.39.99.158
    
    Example:
    
   • Enter Your IP Address : 203.39.99.158
    
   • If you did not give any input it will take's IP.
   
   • Run it on other compiler for the best experience and remove the break statement if you are using it on any other compiler.
    
'''
import urllib.request,urllib.parse,urllib.error
import ssl,json

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
while True:
    print('\t\t\t=======================================')
    print('\t\t\t|| Internet Protocol Tracer By LulNazi ||')
    print('\t\t\t=======================================')
    ip=input('Enter IP Address: ')
    print("\nKafeel is Gathering information...\n")
    print('Have Patience ;)\n')
    
    data=urllib.request.urlopen('http://ip-api.com/json/'+ip);
    j=json.loads(data.read())
    if j['status'] == 'success':
        
        country=j['country']
        countryCode=j['countryCode']
        region=j['region']
        regionName=j['regionName']
        city=j['city']
        zip=j['zip']
        lat=j['lat']
        lon=j['lon']
        timezone=j['timezone']
        isp=j['isp']
        ip=j['query']
        print("##########################################\n")
        print("IP Address  : ",ip)
        print("\nCountryCode : ",countryCode)
        print("\nCountry     : ",country)
        print("\nStateCode   : ",region)
        print("\nState       : ",regionName)
        print("\nCity        : ",city)
        print("\nZIP         : ",zip)
        print("\nLatitude    : ",lat)
        print("\nLongitude   : ",lon)
        print("\nTimeZone    : ",timezone)
        print("\nProvider ISP: ",isp)
        print("\n==============================================")
    else:
        print('\nInvalid IP Address')
        c=input('E-Exit N-No\n')
        if c[0].upper() == 'E':
            print('\nQuiting...')
            print("\t\t++++++++++++++++++++++++++")
            print('\t\t!! Programmed By LulNazi!!')
            print("\t\t++++++++++++++++++++++++++")
            quit()
        else:
            continue
    break
