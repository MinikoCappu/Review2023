FROM python:3.12.1

RUN pip install --upgrade pip
RUN apt-get update

RUN apt update
RUN apt install python3.12.1 -y

WORKDIR /usr/app/src
COPY . .

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN npm install -g playwright
RUN playwright install chromium 

CMD ["python", "main.py"]