# Created by Russell Tolle
# Created Sept. 26, 2014
# Reddit Account Voter:
# Version 1.0
from sys import argv, exit
from time import sleep
import praw
from praw.objects import Redditor, Submission


class RedditAccountVoter(object):
    """
    All object parameters are passed in via the commandline.
    vote_type = downvote, or upvote.
    target_user = the account that you would to perform an action against.
    account_user_name = the account username that you will use to vote.
    account_password = the account password used to log in.
    """
    def __init__(self, vote_type="", target_user="", account_user_name="", account_password=""):
        self.count = 0
        self.api = praw.Reddit(user_agent="RedditAccountVoter by u/Mac2125 ver 1.0", not_spammer=True)
        if vote_type != "":
            self.vote_type = vote_type
        else:
            raise BaseException("No vote type!")
        if target_user != "":
            self.redditor = self.api.get_redditor(target_user, fetch=False)
        else:
            raise BaseException("No target user!")
        if account_user_name and account_password != "":
            self.api.login(account_user_name, account_password)
        else:
            raise BaseException("Can't log in!")

    def run(self):
        for post in self.redditor.get_overview():
            try:
                if self.vote_type == "upvote":
                    post.upvote()
                    self.count += 1
                    print "upvoted: %s" % post.__unicode__()
                if self.vote_type == "downvote":
                    post.downvote()
                    self.count += 1
                    print "downvoted: %s" % post.__unicode__()
            except:
                raise BaseException("Can't vote!")
        sleep(3)


def main(params):
    rav = RedditAccountVoter(*params)
    try:
        rav.run()
    except:
        raise
    finally:
        print "All Done! %sd %d submissions or comments. " % (rav.vote_type, rav.count)

    return 0

if __name__ == "__main__":
    exit(main(argv[1:]))
