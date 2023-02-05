FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--log-level", "critical", "--loop", "uvloop" ]
EXPOSE 8000



# FROM python:alpine3.10 as builder
# COPY requirements.txt .
# RUN apk update \
#  && apk add build-base \
#  && pip install --no-cache-dir --upgrade pip \
#  && pip install --no-cache-dir setuptools wheel \
#  && pip install --no-cache-dir -r requirements.txt \
#  && rm -rf /var/lib/apt/lists/*

# # CMD [ "ls", "/usr/local/lib/python3.8" ]

# FROM python:alpine3.10
# COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
# COPY --from=builder /usr/local/bin /usr/local/bin
# WORKDIR /app
# COPY ./src/ /app/src
# COPY ./main.py .
# CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--log-level", "critical", "--loop", "uvloop" ]
# EXPOSE 8000