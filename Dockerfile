FROM python:3.9.7-slim

WORKDIR /usr/src/app

COPY requirements.txt .
COPY entrypoint.sh .


RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY . /usr/src/app

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]