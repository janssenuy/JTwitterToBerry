"""
Author: Janssen Uy (berry)
Date Started: 22nd November 2017
App Name: JTwitterToBerry
The purpose of this program is to learn how to use GitHub, Git, as well as
    reinforcing my knowledge of using APIs to get and post HTTP requests
    and use them locally.
The brains behind this was taken from the helpful blog here:
https://www.blog.pythonlibrary.org/2014/09/26/how-to-connect-to-twitter-with-python/
"""

import twitter

#Keys and Tokens are to be kept in plaintext
key = "YT8atFYFMBTRIRFNF20zS7WU7"
secret = "95XlcIGYrl1pvkbuxqRzAPrwPUQp4PwqmeY4WZfzA3bgQoa6J4"
user = "JTwitToBerry"
user_id = "933162378337726464"

#Our access tokens need to be kept too (this doesn't seem safe?)
access_token = "933162378337726464-nQCd7xon3n1uOBgGRgeCWJxxzlnivf7"
ats = open("accessTokenSecret.txt", "r")
access_token_secret = ats.readline()
#Ain't no way you're taking my damn passwords!!
    #DON'T COMMIT THE TXT FILE TO GITHUB YOU DINGUS

#Now let's authorize ourselves!
auth = twitter.OAuth(access_token, access_token_secret, key, secret)
client = twitter.Twitter(auth=auth)

#We have identified ourselves as client, now let's do a test post
##client.statuses.update(status="TEST POST")

#Let's try get a timeline pulled

timeline = client.statuses.user_timeline(screen_name="JTwitToBerry")
for item in timeline :
    print(item["text"], "\n")
    
#There's a small problem, I think it might be because of private accounts
    #if you try and pull a timeline, then it will show up blank
    #it may be because the timeline is only for people that you follow
    #so we have to pull our specific timeline out. no problem
