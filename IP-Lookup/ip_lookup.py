import requests

#Single ip request.

def single_request():
    Address=str(input("Please enter IP address: "))
    ip="http://ip-api.com/json/"+Address
    response=requests.get(ip).json()

    print(response['country'])
    print(response['countryCode'])
    print(response['region'])
    print(response['regionName'])
    print(response['city'])
    print(response['lat'])
    print(response['lon'])
    print(response['timezone'])
    print(response['isp'])

    
#Batch ip request.

def batch_request():
    IP1=str(input("Please enter IP1 address(enter none for no IP): "))
    IP2=str(input("Please enter IP2 address(enter none for no IP): "))
    IP3=str(input("Please enter IP3 address(enter none for no IP): "))
    IP4=str(input("Please enter IP4 address(enter none for no IP): "))
    IP5=str(input("Please enter IP5 address(enter none for no IP): "))
    
    response = requests.post("http://ip-api.com/batch", json=[
      {"query": IP1},
      {"query": IP2},
      {"query": IP3},
      {"query": IP4},
      {"query": IP5}
    ]).json()

    for IP_info in response:
        for k,v in IP_info.items():
            print(k,v)
        print("**************************************************\n")
