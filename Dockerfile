FROM python:3.12-slim

WORKDIR /reinas

COPY . /reinas

RUN apt-get update

RUN pip install -r requirements.txt
RUN pip install -r requirements-tests.txt


CMD ["python", "src/queens.py"]