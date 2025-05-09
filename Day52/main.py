CREDENTIAL = "" # Your Phone number, Email or Username
PASSWORD = "" # Your Instagram Password
IG_FOLLOW_HANDLE = "tainted_tammy"

from instagram import Instagram
ig = Instagram()

ig.login(credential=CREDENTIAL, password=PASSWORD)
subscribed_to = ig.find_followers(ig_handle=IG_FOLLOW_HANDLE)
print(f"Congratulations, You have followed {subscribed_to} people\nLets Hope they follow back...")

