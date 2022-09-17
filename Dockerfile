FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python-is-python3 \
    && apt-get install -y python3-pip \
    && apt-get install -y sudo \
    && apt-get install -y make \
    && apt-get install -y file \
    && apt-get install -y uvicorn

WORKDIR /code
ADD ./ /code/

COPY requirements.txt /code/

RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt

CMD ["python", "main.py"]