FROM ubuntu:16.04
MAINTAINER Kyle Luce <nomadmtb@gmail.com>

WORKDIR /opt/url_tracker

RUN apt-get update && apt-get install -y \
    python3 \
    python-pip \
    git

RUN git clone \
    https://github.com/nomadmtb/url-tracker.git \
    /opt/url_tracker

RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]
