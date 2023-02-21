
def my_callback(sender, **kwargs):
    print("request finish!")
    
def create_new_user(sender,instance,created,**kwargs):
    if created:
        print("new user create",instance)
        
        