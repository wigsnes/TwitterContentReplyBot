# Welcome to HACTOBERFEST 2019
Hi, and welcome to this years hacktoberfest.
This repository is made for beginners, 
so if you are new to programming or new to open source projects welcome.

## Requirements:
* Github user
* Git install localy
* A code editor
* python install localy

## Absolutt beginner:
This guide will show you how to install git and get the code down onto your own machine. And explain how to contribute with a pull-request.

https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source

## Here is what I need your help with:

I need your help to fill my twitter bot with content.
This bot replies to users if a particular phrase is found in their tweet.
Let's say someone tweets out that "it was a good day".
The bot will reply with a link to the music video "It was a good day, by ice cube"
Now the bot is only as good as its content, and here is where I need your help.
In the file "content.json" I want you to add your own content that would be a fun reply to any tweet.
Let's say you want to reply with Jim Carrey saying B-E-A-utiful every time a user tweets out a tweet that contains "Beautiful".
Here is how you would insert it to "content.json":

```
{
    "Was A Good Day":"https://www.youtube.com/watch?v=h4UqMyldS7Q",
    "Beautiful":"https://www.youtube.com/watch?v=UPphDSc6ZEE"
}
```

When inserting content always place them at the end, and remember to add a comma on the one above.

You can also add new users you would like to be apart of this twitter-bot by adding them to the file "users.txt",
but if you do you also have to include them in "mock.json" like so:

```
{
    "icecube": [
        {
            "text": "In case y'all didn't know \"It Was A Good Day\"..",
            "id":5455667342234,
            "user": {
                "name": "icecube"
            }
        },
        {
            "text": "In shock this morning. It always hurts a little when...",
            "id":454565576342,
            "user": {
                "name": "icecube"
            }
        }
    ],
    "JimCarrey": [
        {
            "text": "Rise up! Rise up armies of darkness!...",
            "id":442243547875,
            "user": {
                "name": "JimCarrey"
            }
        },
        {
            "text": "Yippie-ki-yay MF!",
            "id":3367879899864,
            "user": {
                "name": "JimCarrey"
            }
        }
    ]
}
```

Here you also should add them last in the list, and remember adding a comma on the one above.
Also, the text can be any random tweet by the user, but it has to be only one line so remove any newlines.
The "ID" is just a random number, try to make this different from the other id's I will later add some tests that will make sure they are all unique.

Bonus points for users that fix my grammar or my instructions if they are unclear.