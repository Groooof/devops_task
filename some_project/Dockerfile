FROM python:3.7

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
EXPOSE 8000

COPY . .
RUN pip install -r requirements.txt
CMD ["uwsgi", "--http", "0.0.0.0:8000", "--module", "some_project.wsgi"]