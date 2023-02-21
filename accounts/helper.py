from kavenegar import *
from random import randint
from accounts.models import User
from datetime import datetime,timezone

def get_random_otp():
    return randint(1000,9999)

def send_otp(phone,otp):
    phone = [phone,]
    try:
        api = KavenegarAPI('734C55712B74382F3539777A79754279564D67745076364F70374F34596F583573693275596864356E55493D')
        params = {
            'sender': '1000596446',#optional
            'receptor': phone,#multiple mobile number, split by comma
            'message': 'your otp number {}'.format(otp),
        } 
        response = api.sms_send(params)
        print(response)
        # print(otp)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)
        
def check_otp_expiration(phone):
    try:
        user =User.objects.get(phone=phone)
        now = datetime.now(timezone.utc)
        otp_time = user.otp_create_time
        diff_time = now - otp_time
        print(diff_time)
        if diff_time.seconds > 30:
            return False
        return True
    except User.DoesNotExist:
        return False
