FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENTRYPOINT exec python3 /code/infobackend/manage.py runserver 0.0.0.0:${PORT}

