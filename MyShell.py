import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FeedProject.settings")

import django
django.setup()

from FeedApp.models import Profile,Relationship

'''
to install from requirements.txt
pip install -r requirements.txt
'''

profile = Profile.objects.get(user=1)
friends = profile.friends.all()
#print(friends)
friends_profiles = Profile.objects.filter(user__in=friends)

friends = Profile.objects.values('friends')
posts = Post.objects.filter(username__in=friends).order_by('-date_posted')