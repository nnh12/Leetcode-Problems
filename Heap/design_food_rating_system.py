class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foods = defaultdict(set)
        self.cusines = {}
        self.ratings = defaultdict(set)

        for i in range(len(foods)):
            cur_cusine = cuisines[i]
            cur_rating = ratings[i]
            cur_food = foods[i]
            
            self.foods[foods[i]] = [cur_rating , cur_cusine]
            
            if cur_cusine not in self.cusines:
                heap = []
                heapq.heapify(heap)
                self.cusines[cur_cusine] = heap
                heapq.heappush(heap, ( -1*cur_rating, cur_food) )
            else:
                heap = self.cusines[cur_cusine]
                heapq.heappush(heap, (-1*cur_rating, cur_food))  

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        if food in self.foods:
            cur_cusine = self.foods[food][1]
            cur_rating = self.foods[food][0]
            heap = self.cusines[cur_cusine]
            
            self.foods[food][0] = newRating
            heapq.heappush(heap, (-1*newRating, food))
                                  
    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        heap = self.cusines[cuisine]
        while heap:
            heap_rating, food = heap[0]
            if -1*self.foods[food][0] == heap_rating:
                return food
            heapq.heappop(heap)
            
        #print(self.cusines)
        #if cuisine in self.cusines:
        #    heap = self.cusines[cuisine]
        #    return heap[0][1]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
