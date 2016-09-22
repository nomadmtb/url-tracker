FROM ubuntu:14.04
MAINTAINER Kyle Luce <nomadmtb@gmail.com>

RUN apt-get update && apt-get install -y \
    python3.5 \
    python3-pip \
    git \
    nodejs \
    npm

RUN git clone \
    https://github.com/nomadmtb/url-tracker.git \
    /opt/url_tracker

RUN pip3 install --upgrade pip
WORKDIR /opt/url_tracker
RUN pip install -r requirements.txt
RUN npm install --save-dev

CMD ["python3.5", "run.py"]
