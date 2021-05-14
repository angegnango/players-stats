FROM python:3.6-alpine

ENV HOST 0.0.0.0
ENV PORT 3000
ENV DEBUG true
ENV MONGODB_DATABASE database
ENV MONGODB_USERNAME db_user 
ENV MONGODB_PASSWORD db_password 
ENV MONGODB_HOSTNAME mongodb

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 3000

ENTRYPOINT ["python"]

CMD ["run.py"]