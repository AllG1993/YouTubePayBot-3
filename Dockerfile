FROM python:latest

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get clean

USER root
RUN mkdir /YouTubePayBot
WORKDIR /YouTubePayBot
COPY . /YouTubePayBot


RUN pip install --upgrade pip
RUN pip install -U aiogram
RUN pip install -U oauth2client
RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN ls

ENTRYPOINT ["python", "tg_bot/bot.py"]