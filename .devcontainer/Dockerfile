FROM python:3.8-slim as pro

RUN apt-get -y update && apt-get install

ADD . /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "/bin/bash" ]

