# dbd_randomizer_service

This project is the backend API server for the [dbd-randomizer-ui](https://www.cryptorat.com/dbd/) and the dbd\
randomizer [mobile app](https://github.com/CryptoRAT/dbdrandomizer). It is written in Python, using the Django\ 
framework. It is backed by a postgres database.

## Available scripts

### `python manage.py migrate`
Sets up the database with the initial data about killers, survivors, and perks.

### `python manage.py runserver`
Start the server.

### Deployment
This project is autodeployed to a digitalocean app when a merge is made to main. This is accomplished using github\ 
actions and tools provided by digitalocean. 


### TODOs
You can see a list of things I would like to add to this site here: [wish list])(./WISHLIST.md)
