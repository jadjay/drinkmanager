FROM python:3
MAINTAINER javond@adista.fr

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code


RUN apt-get update
RUN apt-get install -y python3-pip python3-urllib3 gettext-base apt-utils
#python3 python3-pip pipenv git
#RUN pipenv --three sync
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

