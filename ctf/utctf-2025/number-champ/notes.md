# Setup

We get a website that hosts a game of comparing numbers.
Users get a `uuid` and a starting `elo` of 1000 and you can give the site
a point on earth described by pair of `lantitude` and `longitude`. This point
is used to calculate the distance to your opponent when looking for a match.
Goal is to find the location (street, city, zip code) of the player with the
highest elo called `geopy`.


# Solve

No matter which number i tried when playing, the opponent always added some and
got a higher number. So it seems we always lose.
Losing we notice that the matches we find are always against players with a
similar elo. Luckily there is no functionality at the `/battle` endpoint that
checks the uuid which means we can boost any given player's elo by using their
uuid as opponent and of course losing.

Once we get a high enough elo we meet the player `geopy`

```json
{
	"distance":5849.500680621647,
	"elo":3000,
	"user":"geopy",
	"uuid":"d0f627bc-ac15-4d45-8e08-73ee3b5fd06c"
}
```

thats the distance from `lat=0`, `lon=0`

Since we have a reliable way to find a match against the target player we can
try different values for `lat` and `lon` to minimize the distance and get an
idea of the location required for the flag.

Manually trying some numbers:

`lat=42.1337&lon=-69.1337` gives us a distance of `739.0933936497996` miles.
Thats pretty good already but we need to go way closer.


Using python's `geopy` library (who would have thought) makes it easy to
calculate a new pair of latitude and longitude given an initial point and a distance.

```py
from geopy import distance

distance.distance(miles=current_distance).destination((lat,lon), bearing=i)
```

With this we can iterate through different values for the
bearing (bascially the directions N/E/S/W rangin from -90 to 270) and get new 
values for `lat` and `lon`.
Using the games `/match` endpoint we can confirm if the new distance is lower
than the previous one.

```py
def getDistance(lat, lon):
    TARGET = f"{URL}/match?uuid={uuid}&lat={lat}&lon={lon}"
    resp_json = requests.post(TARGET).json()
    if resp_json["user"] == "geopy":
        return resp_json["distance"]
    else:
        return current_distance
```

doing this a while (without spamming the servers during the competition) we
eventually arrive at:

```
lat= 39.94045400599625
lon= -82.99668165720544
curr_dis= 0.0025611403163520088
```

Handing over these values to google maps we can see a starbucks being really
close by which seems a reasonable guess for the solution.

`1059 S High St, Columbus, OH 43206, United States`

`utflag{1059-s-high-st-columbus-43206}`
