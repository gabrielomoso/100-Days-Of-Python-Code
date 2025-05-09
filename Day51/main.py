EMAIL = "" # Your Twitter Email
PASSWORD = "" # Your Twitter Password
TWITTER_HANDLE = "@MTNNG"  # Twitter Handle of your network provider
LOCATION = ""
EXPECTED_DOWNLOAD_SPEED = 2.0 # MB per second
EXPECTED_UPLOAD_SPEED = 2.0 # MB per second










from speedTest import SpeedTest
from twitterBot import TwitterBot

speed_test = SpeedTest()

internetSpeed = speed_test.get_internet_speed()
for key, value in internetSpeed.items():
    print(key, value)


if internetSpeed["download_speed"] < EXPECTED_DOWNLOAD_SPEED and internetSpeed["upload_speed"] < EXPECTED_UPLOAD_SPEED:
    twitter_bot = TwitterBot()
    twitter_bot.tweet_at_provider(internet_speed=internetSpeed, twitter_handle=TWITTER_HANDLE, location=LOCATION, email=EMAIL, password=PASSWORD)