FROM ubuntu:14.04
MAINTAINER Kyle Luce <nomadmtb@gmail.com>

# Adding ppa for Python3.5
RUN apt-get update
RUN apt-get install software-properties-common
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get update

# Installing required software
RUN apt-get install -y \
    python3.5 \
    python3-pip \
    git \
    nodejs \
    npm

# Cloning code from github
RUN git clone \
    https://github.com/nomadmtb/url-tracker.git \
    /opt/url_tracker

# Install required python packages
RUN pip3 install --upgrade pip
WORKDIR /opt/url_tracker
RUN pip install -r requirements.txt

# Install npm packages and hash the static files
RUN npm install --save-dev
RUN grunt --verbose cacheBust

# Run the program
CMD ["python3.5", "run.py"]
