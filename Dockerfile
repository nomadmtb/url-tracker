FROM ubuntu:16.04
MAINTAINER Kyle Luce <nomadmtb@gmail.com>

RUN apt-get update && apt-get install -y \
    python3.5 \
    python3-pip \
    git

RUN git clone \
    https://github.com/nomadmtb/url-tracker.git \
    /opt/url_tracker

RUN pip3 install --upgrade pip
WORKDIR /opt/url_tracker
RUN pip install -r requirements.txt

CMD ["python3.5", "run.py"]
