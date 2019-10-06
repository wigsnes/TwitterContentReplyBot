# Twitter Content Reply Bot

## Hacktoberfest

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file to find out how you can help out.

## Running the bot

### Using mock data

If you wish to use mock data, first make sure that
```
DEBUG = True
```
in the [twitter.py](twitter.py) file.\
If yes, or after setting it to True, run

```
python twitter.py
```
This will go through each users tweet and see if they match with any of the content found in [content.json](content.json).

### Using your own Twitter account

- Apply for a Twitter developer account [here](https://developer.twitter.com/en/apply-for-access)
- This will give you access to your own API keys and access tokens.
- Now, change the file called `config.py` inside the working directory and fill it in

```
API_key = "YOUR OWN API KEY"
API_secret_key = "YOUR OWN API SECRET KEY"
Access_token = "YOUR OWN ACCESS TOKEN"
Access_token_secret = "YOUR OWN SECRET ACCESS TOKEN"
```

Before running the code, make sure that
```
DEBUG = False
```
in [twitter.py](twitter.py).
