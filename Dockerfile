FROM python:3.10

# Instalação do cmake
RUN apt-get update && apt-get install -y cmake

COPY . /app

ARG PORT

ENV PORT=$PORT

RUN pip install -r requirements.txt

WORKDIR /app

EXPOSE $PORT

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "${PORT}"]