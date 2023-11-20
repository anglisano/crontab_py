FROM python:3.8-slim as pro

RUN apt-get -y update && apt-get install

ADD . /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["/usr/local/bin/python"]

# ------------------------------------------------------- dev container specific
FROM pro as dev
RUN pip install -r requirements-dev.txt


# Install git if ssh is used


FROM dev AS dev-vcode
RUN apt-get install -y libgtk2.0-dev
RUN apt install -y libgl1-mesa-glx
RUN apt-get install ffmpeg libsm6 libxext6  -y
# RUN apt-get clean
# WORKDIR /usr/local
# RUN mkdir jdk
# RUN chmod 777 /usr/local/jdk
# WORKDIR /usr/local/jdk
# RUN wget -c https://github.com/adoptium/temurin11-binaries/releases/download/jdk-11.0.13%2B8/OpenJDK11U-jdk_x64_linux_hotspot_11.0.13_8.tar.gz -O - | tar -xz
# RUN apt-get install git
# #RUN ENV JAVA_HOME /usr/local/jdk/jdk-11.0.13+8
# RUN export JAVA_HOME=/usr/local/jdk/jdk-11.0.13+8
# WORKDIR /app

ENTRYPOINT [ "/bin/bash" ]

FROM dev AS dev-pycharm
ENTRYPOINT []

# build image examples:
# docker build -t cron_py:dev -f .devcontainer/Dockerfile . --target dev
# docker build -t cron_py:dev-vcode -f .devcontainer/Dockerfile . --target dev-vcode