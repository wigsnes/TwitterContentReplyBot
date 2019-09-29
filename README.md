# Twitter Content Reply Bot

## Hacktoberfest
Please read the CONTRIBUTING.md on how to contribute to this project.

## How to make it run with your own twitter account.

To make this code work with your own twitter account you first need to apply for a twitter app at https://developer.twitter.com/. This will give you the keys, and tokens needed to make it work. Create a file called config.py and fill them inn like so:

```
API_key = "YOUR OWN API KEY"
API_secret_key = "YOUR OWN API SECRET KEY
Access_token = "YOUR OWN ACCESS TOKEN"
Access_token_secret = "YOUR OWN SECRET ACCESS TOKEN"
```

Also remember to set DEBUG to false in twitter.py