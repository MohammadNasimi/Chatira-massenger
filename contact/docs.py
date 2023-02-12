contact_create_post="""
model post:
{
    "name":optional 
    "phone":"09305161131
}
if exist in your contact ---->
   errors  phone exist in your contact list
if not exist this phone in user ----->
    errors phone does not exist
"""
contact_create_post ="""
with out params get all contact user log in :
like this 

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 6,
            "user": {
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
            },
            "name_contract": "mohammad nasimi",
            "contact": {
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
            },
            "block": false
        }
    ]
}
##############
if you want to use filter  you could add search param
search=m
every thing you write in front of search this title search all phone and name_contact and show all of them 
for example search = a show you all phone and name_contact contain a

"""
contact_detail_get="""
user just could get your contacts with pk 

"""
contact_detail_put="""
user just could get your contacts with pk 
model put:
{
    "name_contact": "ali",
    "block": false
}
"""
contact_detail_patch="""
user just could get your contacts with pk 
model patch:
one of them
{
    "name_contact": "ali",
    "block": false
}
"""
contact_detail_delete="""
user just could get your contacts with pk 

"""