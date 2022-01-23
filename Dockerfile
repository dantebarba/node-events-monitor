FROM python:3.8.2-alpine

ENV AUTH_KEY="CHANGE_YOUR_KEY"

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Expose the Flask port
EXPOSE 5000

RUN chmod +x app.py

CMD [ "python", "./app.py" ]