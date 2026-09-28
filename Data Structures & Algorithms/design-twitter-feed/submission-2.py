class Twitter:

    def __init__(self):
        self.following = [set() for _ in range(501)] 
        self.count = 0 
        self.tweets = [deque([]) for _ in range(501)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.count, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = list(self.tweets[userId])
        
        for x in self.following[userId]:
            feed += list(self.tweets[x])
        heapq.heapify_max(feed)
        res = []
        for i in range(10):
            if len(feed) == 0:
                break
            t = heapq.heappop_max(feed)
            res.append(t[1])
        return res 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)