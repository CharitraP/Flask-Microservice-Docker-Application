FROM python:3.10-slim
LABEL ord.opencontainers.image.soruce=https://github.com/CharitraP/Flask-Microservice-Docker-Application
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python ./run.py
