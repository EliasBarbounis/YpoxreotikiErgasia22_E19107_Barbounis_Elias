FROM ubuntu:20.04

RUN apt-get update

RUN apt-get install -y python3 python3-pip

ADD . /app

WORKDIR /app

RUN pip3 install flask pymongo 

ENTRYPOINT [ "python3","-u", "app.py" ]