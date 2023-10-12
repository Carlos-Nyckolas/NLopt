FROM python:3.10

# Instalação do cmake
RUN apt-get update && apt-get install -y cmake

COPY . /app

ARG PORT

ENV PORT=$PORT

RUN pip install numpy
RUN pip install nlopt
RUN pip install fastapi
RUN pip install "uvicorn[standard]"

WORKDIR /app

EXPOSE $PORT

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "${PORT}"]