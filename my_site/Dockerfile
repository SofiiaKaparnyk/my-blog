FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /my_site
COPY . .
RUN pip install --upgrade pip
COPY requirements.txt /my_site/
RUN pip install -r requirements.txt
COPY . /my_site/