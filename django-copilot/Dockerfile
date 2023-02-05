# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

RUN apt-get update -y
RUN apt-get dist-upgrade -y
RUN apt-get install -y build-essential graphviz-dev graphviz pkg-config

RUN pip install -r requirements.txt
RUN pip install pydotplus
# RUN pip install django-filter 
# RUN pip install django-cors-headers
# RUN pip install django-extensions
COPY . /code/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
