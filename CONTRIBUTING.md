# Welcome to HACKTOBERFEST 2019
Hi, and welcome to this years Hacktoberfest.\
This repository is made for beginners, 
so if you are new to programming or open source projects, welcome.

## Requirements:
* Github account
* git
* python
* your favourite text editor

## For beginners with git:

If you are a beginner, you may be interested in the following link, which leads to\
a guide that serves as an introduction to git, teaches you to how to download others' code\
and to submit pull requests of your own.

[**An introduction to open source**](https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source)  
  
  
## Here is what I need your help with:
This bot replies to users if a particular phrase is found in their tweet.\
However, a bot is only as good as its content, and that's where you come in.\
I would appreciate your help in filling my twitter bot with content.

### Example:
Let's say someone tweets out that "it was a good day".\
The bot will reply with a link to the music video *It was a good day* by ice cube.\
I would like you to add content that you consider a fun reply to any tweet to the `content.json` file.\
Let's say you want to reply with Jim Carrey saying B-E-A-utiful every time a user tweets out a tweet that contains "Beautiful".\
Here is how you would insert it into `content.json`:

```
{
    "Was A Good Day":"https://www.youtube.com/watch?v=h4UqMyldS7Q",
    "Beautiful":"https://www.youtube.com/watch?v=UPphDSc6ZEE"
}
```

When inserting content, remember to place the new entry at the very end and separate it\
from the previous one by placing a comma character behind its closing bracket.

You can also add new users you would like to be apart of this twitter-bot by adding them into the `users.txt` file,\
but if you do you also have to include them in `mock.json` like so:

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

Just like when adding content, a new users should be added as the last in the list\
and separated from the previous one by a comma.  

The text can be any tweet by the user that is one line only, so remove any newlines.\
The "ID" is just a random number, try to make this different from the other id's.\
Later on I plan to add tests to make sure they are all unique.

Bonus points for users that fix my grammar or my instructions if they are unclear.