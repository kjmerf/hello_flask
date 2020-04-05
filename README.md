# hello flask
The application searches for recipes using the edamam API: https://developer.edamam.com/edamam-recipe-api.

I made it to test docker and flask.

To run locally, you need an app ID and app key from edamam.
Then store your id and key in environment variables called EDAMAM_APP_ID and EDAMAM_APP_KEY respectively.
You also need to install Docker.

To start the application, just run:
```shell
./start.sh
```

Check http://localhost:5000/ to search for recipes!
