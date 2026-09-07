import heapq
from collections import defaultdict
class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        h = []

        self.follows[userId].add(userId)

        # get latest tweet from all followee's
        # -> must contain the first tweet in newsfeed
        for f in self.follows[userId]:
            if f in self.tweets: # has tweets?
                count, tweetId = self.tweets[f][-1]
                heapq.heappush(
                    h,
                    [-count, tweetId, f, len(self.tweets[f]) - 1]
                )
        # h --> result; stop when h empty, or result reach target
        # -> "Stop when source is drained, or destination full"
        while h and len(result) < 10:
            _, tweetId, f, i = heapq.heappop(h)
            result.append(tweetId)

            if i > 0:
                prev_count, prev_tweetId = self.tweets[f][i - 1]
                heapq.heappush(
                    h,
                    [-prev_count, prev_tweetId, f, i - 1]
                )
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
