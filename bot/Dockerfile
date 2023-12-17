FROM python:3.12.1

RUN pip install --upgrade pip

COPY . .
RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN npm install -g playwright
RUN playwright install chromium 

COPY . .

CMD ["python", "main.py"]