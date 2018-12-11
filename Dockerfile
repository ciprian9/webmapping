FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN apt-get update
RUN apt-get install -y -qq python.pyproj
WORKDIR /code
COPY . /code/
RUN pip3 install -r requirements.txt
