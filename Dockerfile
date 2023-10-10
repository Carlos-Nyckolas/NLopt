FROM python:3

# Instalação do cmake
RUN apt-get update && apt-get install -y cmake

COPY . /app

ARG PORT

ENV PORT=$PORT

RUN pip install numpy
RUN pip install nlopt
RUN pip install flask

WORKDIR /app

EXPOSE $PORT

CMD ["python", "app.py"]