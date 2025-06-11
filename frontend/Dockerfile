from python:3.11-slim

WORKDIR app/

COPY frontend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY frontend ./frontend
COPY shared ./shared

EXPOSE 8501

CMD ["streamlit", "run", "frontend/streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]