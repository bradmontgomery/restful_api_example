# A Simple RESTful API in Flask


This repo contains a simple Flask app that illustrates
a RESTful API.


## Usage

0. Set up a virtualenv with `python3 -m venv env`, then run `source env/bin/activate`.
1. Install the requirements with `pip install -r requirements.txt`.
2. Run the flask development server with `./run.sh`.
3. Use of the resources listed below to interact with the API.


## Endpoints

This app has the following API endpoints:

- `/api/users/` GET requests will list all available "user accounts". POST requests
  will create a new user.
- `/api/users/<user_id>/` GET requests with the provided user id will list details
  for a single users. PUT requests allow you to update a user's account. DELETE
  requests will allow you to remove a user account.


## Resources

- [httpie](https://httpie.org/): a command line HTTP client with a nice UI
- [Postman](https://www.getpostman.com/): a desktop app that lets you do just
  about anything you want with an API.
- [curl](https://curl.haxx.se/) is a command-line utility available on most
  unix-like systems that you can also use to interact with this api.


## License

This code is released under an MIT License. See the [LICENSE.txt](LICENSE.txt)
file in this repo for the full license.
