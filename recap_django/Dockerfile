FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# docker build -t django_recap .
# docker run -p 8000:8000 django_recap 
# docker run -p 8000:8000 -v $(pwd):/app django_recap 
# docker run --rm --env-file .env -p 8000:8000 django_recap


# docker network create mynetwork
# docker run -v postgres_data:/var/lib/postgressql/data/ --rm --env-file .env --name postgres_db --network mynetwork postgres   ### you can name it what ever u want in place of postgres_data

# docker run --rm --env-file .env -p 8000:8000 --network mynetwork django_recap


# in Docker shell :
# python manage.py shell
# from django.conf import settings
# settings.DATABASES 