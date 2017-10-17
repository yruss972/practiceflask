import os
WTF_CSRF_ENABLED = True
SECRET_KEY = os.getenv('WTF_CSRF_SECRET_KEY','github-is-not-a-place-for-secrets')
HOST = os.getenv('IP','127.0.0.1')
PORT = int(os.getenv('PORT','5000'))
DEBUG = True
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
SITE_TITLE = 'Vendor Escape'
SITE_NAVITEMS = [
        {
            'route':'',
            'button':'',
            'innerHTML':'Home'
        },
        {
            'route':'about',
            'button':'',
            'innerHTML':'About'
        },
        {
            'route':'more-info',
            'button':'warning',
            'innerHTML':'More Info'
        }
    ]