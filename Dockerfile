FROM ubuntu:14.04
MAINTAINER Kyle Luce <kylegluce@gmail.com>

# Adding ppa for Python3.5
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:fkrull/deadsnakes
RUN apt-get update

# Installing required software
RUN apt-get install -y \
    python3.5 \
    git wget \
    nodejs \
    npm

# Installing pip on 3.5
RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && \
    python3.5 /tmp/get-pip.py
RUN rm /tmp/get-pip.py

# Cloning code from github
RUN git clone \
    https://github.com/nomadmtb/utldr.git \
    /opt/utldr

# Install required python packages
RUN pip3.5 install --upgrade pip
WORKDIR /opt/utldr
RUN pip install -r requirements.txt

# Install npm packages and hash the static files
RUN ln -fs /usr/bin/nodejs /usr/local/bin/node
RUN npm install -g grunt-cli
RUN npm install --save-dev

# Installing fs-extra manually until cache-bust is updated
RUN npm install --save-dev fs-extra

RUN grunt --verbose cacheBust

# Run the program
CMD ["python3.5", "run.py"]
