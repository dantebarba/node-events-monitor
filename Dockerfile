FROM python:3-alpine

ARG BUILD_DATE

# Set labels (see https://microbadger.com/labels)
LABEL org.label-schema.build-date=$BUILD_DATE

ENV AUTH_KEY="CHANGE_YOUR_KEY"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

# Expose the Flask port
EXPOSE 5000

CMD [ "python", "./app.py" ]