#!/bin/bash

FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

ENV APP_PORT=9000

EXPOSE 9000

CMD ["python", "app.py"]

