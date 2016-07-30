import json
import praw
import OAuth2Util
import sys
import os
import time
from time import gmtime, strftime

"""
Starting August 2015 reddit will require all logins to be made through OAuth. 
In order to log in through OAuth you'll need to follow a few simple steps 
(see https://github.com/SmBe19/praw-OAuth2Util/blob/master/OAuth2Util/README.md#reddit-config)
The first time you run the script a browser will open and you'll have to log into the account to authorize the app, 
if you don't do this the script will not write any tokens and it simply won't work. Message 
/u/zzqw- if you need help with this.
OAuth changes made by /u/zzqw- + /u/GoldenSights
OAUth2Util.py by /u/SmBe19 (https://github.com/SmBe19/praw-OAuth2Util)
"""

class FlairBot:
    # User blacklist
    with open('flair_list.json') as flair_list:
        data = json.load(flair_list)
    BLACKLIST = data['blacklist']
    possible_flairs = data['flairs']
    # Set a descriptive user agent to avoid getting banned.
    # Do not use the word `bot' in your user agent.
    r = praw.Reddit(user_agent="Flair changer for /r/pokemongo testing")
    o = OAuth2Util.OAuth2Util(r)
    TARGET_SUB = 'pgcsst'
    LOGGING = True
    pms = None
    # Define possible_subject below
        
    def init(self):
        if self.LOGGING:
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
        self.login()

    def login(self):
        try:
            self.o.refresh()  # Refresh the OAuth token, only valid for 1hr
            self.fetch_pms()
        except:
            raise

    def fetch_pms(self):
        self.pms = self.r.get_unread(limit=None)
        if self.pms is not None:
            self.process_pms()

    def process_pms(self):
        for pm in self.pms:
            subject = str(pm.subject)
            if subject.lower() in self.possible_flairs:
                author = str(pm.author)  # Author of the PM
                if author.lower() in (user.lower() for user in self.BLACKLIST):
                    continue
                flair_class = subject.lower()  # Sets flair class according to subject
                subreddit = self.r.get_subreddit(self.TARGET_SUB)
                if flair_class in self.possible_flairs:
                    # Get the flair text that corresponds with the pm body
                    flair_text = str(pm.body)
                    if len(flair_text) > 50:
                        flair_text = ''
                    subreddit.set_flair(author, flair_text, flair_class)
                    if self.LOGGING:
                        self.log(author, flair_class, flair_text)
                pm.mark_as_read()  # Mark processed PM as read
        sys.exit()
        
    def log(self, author, flair_class, flair_text):
        with open('log.txt', 'a') as logfile:
            time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            log_text = 'Added: ' + author + ' : ' \
                + flair_text + ' : ' \
                + flair_class + ' @ ' + time_now + '\n'
            logfile.write(log_text)

FlairBot().init()
