# utldr.co
A URL shortener with built-in tracking features that allows users to see the
click-through data for a particular link. The project is built with Python3,
SQLAlchemy and Flask.

---

## To build the docker image.
To build the docker image simply run the following.
```sh
docker build -t utldr-co .
```

To run the container image in daemon mode run the following. Be sure to pass in
your RECAPCHA_KEY and RECAPCHA_SECRET env variables for Google Recapcha.
```sh
docker run -d \
 -p 127.0.0.1:8080:8080 \
 -e RECAPCHA_KEY='...insert_your_key_here...' \
 -e RECAPCHA_SECRET='...insert_your_secret_here...' \
 -it utldr-co
```

## Requirements
Please take a look at the requirements.txt to see all of the required python
packages.  To install the packages you can run the following.
```sh
pip install -r requirements.txt
```
