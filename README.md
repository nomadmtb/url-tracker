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

To run the container image in daemon mode run the following.
```sh
docker run -d -p 127.0.0.1:8080:8080 -it utldr-co
```

## Requirements
Please take a look at the requirements.txt to see all of the required python
packages.  To install the packages you can run the following.
```sh
pip install -r requirements.txt
```

## ScreenShots
If you don't want to build the project to see it, here are a few images of the
application.

![HomePage](http://i.imgur.com/zWVl5xz.png)

![DetailsPAge](http://i.imgur.com/LkdsnuY.png)
