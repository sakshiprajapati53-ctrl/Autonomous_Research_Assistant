FROM python:3.11
# working directory /app project root banega
WORKDIR /app 
#Docker caching optimization if code changes but dependencies same , faster rebuilds
COPY requirements.txt
# reduce image size
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000

CMD[
    "uvicorn",
    "main:app",
    "--host",
    "0.0.0.0",
    "--port",
    "8000"
]


