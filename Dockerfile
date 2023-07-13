FROM python:3.9.17-slim-bullseye
COPY . .
RUN pip3 install psycopg2

ENV DB_HOST="127.0.0.1"
ENV DB_PORT="5432"
ENV DB_NAME="production"
ENV DB_USER="test"
ENV DB_PASSWORD="test"

CMD [ "python3", "-m" , "app.py"]
