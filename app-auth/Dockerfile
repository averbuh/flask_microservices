FROM python:3.7-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.orgi -r requirements.txt

EXPOSE 5000

CMD ["python", "src/auth.py"]
