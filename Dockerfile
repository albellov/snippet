FROM python:3.8-slim

RUN apt-get update -y
RUN apt-get install -y libgtk2.0-dev

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY service/app.py requirements.txt setup.py /app/
COPY snippet/*.py /app/snippet/
RUN pip install -e .

ENV PORT 8080

CMD ["python", "app.py"]
