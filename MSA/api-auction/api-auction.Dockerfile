FROM python:3.8.3-slim

COPY ./api-auction/requirements.txt /api-auction/requirements.txt
COPY ./api-auction/sources /api-auction
WORKDIR /api-auction

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r /api-auction/requirements.txt

ENTRYPOINT ["./start.sh"]

