FROM python:3-alpine

RUN echo '0  22  *  *  *    /usr/local/bin/python /app/manage.py generate_call_list' >> /etc/crontabs/root

RUN echo '0  22  *  *  *    /usr/local/bin/python /app/manage.py reset_should_be_contacted' >> /etc/crontabs/root

WORKDIR /app

RUN apk add --update postgresql-libs postgresql-dev python3-dev gcc musl-dev

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/dumb-init", "/app/entrypoint.sh"]