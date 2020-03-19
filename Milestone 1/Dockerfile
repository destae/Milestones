FROM ubuntu:18.04
FROM python:3

COPY requirements.txt ./

RUN apt-get update --fix-missing
RUN apt-get upgrade -y
RUN apt-get install -y python3-pyqt5
RUN apt-get install -y pyqt5-dev-tools
RUN apt-get install -y qttools5-dev-tools
RUN pip3 install --no-cache-dir -r requirements.txt
