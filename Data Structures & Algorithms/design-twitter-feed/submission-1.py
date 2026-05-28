class Twitter:

    from collections import defaultdict
    import heapq

    def __init__(self):

        self.userTweets = defaultdict(list)
        self.userFollowing = defaultdict(set)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.count, tweetId])
        self.count +=1
        

    def getNewsFeed(self, userId: int) -> List[int]:


        allUsers = self.userFollowing[userId]
        allUsers.add(userId)
        allposts = []

        for user in allUsers:
            for tweet in self.userTweets[user]:
                allposts.append(tweet)
        
        feed = heapq.nlargest(10,allposts)
        
        return [tweetId[1] for tweetId in feed]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.userFollowing[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowing[followerId]:
            self.userFollowing[followerId].remove(followeeId)
        
