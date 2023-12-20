FROM python:3.12.1

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update && apt-get install -y \
    google-chrome-stable
    
RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY main.py ./
COPY db.py ./
COPY config.py ./
COPY parse_true.py ./
COPY handlers.py ./
COPY kb.py ./
COPY states.py ./
COPY text.py ./
COPY utils.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "main.py"]