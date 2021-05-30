FROM python:3.9
ENV PYTHONUNBUFFERED 1

ARG UNAME=development
ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

RUN apt-get update -y
RUN apt-get install -y gettext libgettextpo-dev

RUN mkdir /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt

USER $UNAME

WORKDIR /code