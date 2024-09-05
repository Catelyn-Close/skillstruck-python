#Checkpoint
class Vacation:
    def __init__(self, place, distance, weather):
        self.place = place
        self.distance = distance
        self.weather = weather
    def tuesday(self):
        print("We will be hiking on Tuesday.")
summer = Vacation("Hawaii", 2000, "Sunny")

summer.rating = 10

summer.weather = "rainy"

print(summer)
print(summer.rating)
print(summer.weather)
#Challenges Weekend
class Friday:
    def __init__(self, activity, friend):
        self.activity = activity
        self.friend = friend
    def pictures(self):
        print("We took so many pictures!")

thisWeekend = Friday("Movie", "Charlotte")
thisWeekend.money = 20
thisWeekend.friend = "Shane"

print(thisWeekend)
print(thisWeekend.money)
print(thisWeekend.friend)
#challenges Shopping
