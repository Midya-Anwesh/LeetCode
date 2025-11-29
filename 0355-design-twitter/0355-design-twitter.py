from collections import defaultdict
from heapq import heappush, heappop
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.time, tweetId))
        if userId not in self.following[userId]:
            self.following[userId].add(userId)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        self.followedNews = []
        for user in self.following[userId]:
            if len(self.tweets[user]):
                heappush(self.followedNews, (*self.tweets[user][-1], user, len(self.tweets[user])-1))
        while len(self.followedNews) and (len(ret) < 10):
            _, tweetId, user, idx = heappop(self.followedNews)
            ret.append(tweetId)
            if idx > 0:
                heappush(self.followedNews, (*self.tweets[user][idx-1], user, idx-1))
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)