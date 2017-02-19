from collections import Iterable,Iterator

class WeatherIterrator(Iterator):
    def __init__(self,cities):
        self.cities=cities
        self.index=0

    def next(self):
        if self.index==len(self.cities):
            raise StopIteration
        city=self.cities[self.index]
        self.index+=1
        return self.getWeather(city)

class WeatherIterable(Iterable):
    def __init__(self,cities):
        self.cities=cities


#------------不知道都是是啊乱七八糟的-------------