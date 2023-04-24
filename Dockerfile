FROM python:3.10.10

WORKDIR /test_webhook

COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y postgresql-client

RUN pip install -r requirements.txt

COPY bot.py ./bot.py
COPY .env ./.env

EXPOSE 5000

RUN mkdir -p ./storage/temp
RUN mkdir -p ./storage/backup

CMD [ "python", "bot.py" ]