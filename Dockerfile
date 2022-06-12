FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN apt update -y && apt install -y libsndfile-dev

COPY ./app /code/app

COPY ./index.html /code/index.html

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
