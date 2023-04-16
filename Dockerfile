FROM python:3.10.10

WORKDIR /test_webhook

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY bot.py ./bot.py
COPY .env ./.env

EXPOSE 5000

CMD [ "python", "bot.py" ]