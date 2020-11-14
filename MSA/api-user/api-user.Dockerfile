FROM python:3.8.3-slim

COPY ./api-user/requirements.txt /api-user/requirements.txt
COPY ./api-user/sources /api-user
WORKDIR /api-user

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /api-user/requirements.txt

ENTRYPOINT ["./start.sh"]

