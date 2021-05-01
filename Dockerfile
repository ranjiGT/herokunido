FROM python:3.7-alpine

RUN mkdir -p /home/regorapp

COPY . /home/regorapp

CMD ["python", "app.py"]
