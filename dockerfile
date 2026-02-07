# each line is an instruction

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Give it permission to run
RUN chmod +x start.sh

# Tell Docker to run the script instead of just running the server
CMD ["./start.sh"]
