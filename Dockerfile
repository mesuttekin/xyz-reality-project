FROM python:3.8.0-slim

COPY . /xyz-reality-project
WORKDIR /xyz-reality-project

RUN pip install --user -r requirements.txt

CMD python3 ./manage.py run
