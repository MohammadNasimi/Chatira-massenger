Log_in_Post ="""
if every one phone and password wrong or not exist in json ---> error

model post:
{
    "phone": "09305161132",
    "password": "10123456789"
}

"""
Register_create_Post ="""

model post :
{
    "phone": "09305161132",
    "password": "10123456789"
    "email":optional,
    "first_name":optional,
    "last_name": optional
}
if every one phone and password wrong or not exist in json ---> error  please fill phone  or password
if exist phone ---> errors phone exist
"""
profile_detail_Get ="""
add in url int pk profile get all data :
model get:
{
    "id": 2,
    "user": {
        "id": 3,
        "phone": "09305161132",
        "email": "",
        "first_name": "",
        "last_name": ""
    },
    "username": null,
    "bio": null,
    "profile_pic": null
}

"""
profile_detail_put ="""
every user just your profile could update 
 

model post:
{
    "username": null,
    "bio": null,
    "profile_pic": null
}

"""
profile_detail_patch ="""
every user just your profile could update 
 
partial of all field you could update for example

model post:
{
    "username": null
}
"""
usermeta_detail_Get ="""
add in url int pk usermeta get all data :
model get:
{
    "id": 2,
    "profile": 2,
    "personal_theme": "{'color': 'black', 'theme': 'white'}",
    "status": false,
    "last_seen": "2023-02-12T17:17:55.934439+03:30"
}

"""
usermeta_detail_put ="""
every user just your usermeta could update 
 
personal_theme is json and you save every thing in it like key and value

model post:
{
    "personal_theme": "{'color': 'black', 'theme': 'white'}",
    "status": false,
    "last_seen": "2023-02-12T17:17:55.934439+03:30"
}

"""
usermeta_detail_patch ="""
every user just your usermeta could update 
 
partial of all field you could update for example

personal_theme is json and you save every thing in it like key and value

model post:
{
    "personal_theme": "{'color': 'black', 'theme': 'white'}",
}
"""