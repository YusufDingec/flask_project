FROM python:3.6.1-alpine

EXPOSE 5000

RUN pip install --upgrade pip

WORKDIR /myfirst-docker

ADD . . 

RUN python3 -m venv env
RUN source env/bin/activate

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
