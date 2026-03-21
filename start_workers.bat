@echo off
echo Starting AI Content Marketing Engine...
echo.

cd /d "%~dp0"

echo [1/2] Starting Celery Worker...
start "Celery Worker" cmd /k "venv\Scripts\activate && celery -A app.celery_app worker --loglevel=info --pool=solo"

timeout /t 3 /nobreak >nul

echo [2/2] Starting FastAPI Server...
start "FastAPI Server" cmd /k "venv\Scripts\activate && uvicorn app.main:app --reload"

echo.
echo ========================================
echo Both services started!
echo ========================================
echo.
echo Celery Worker: Running in separate window
echo FastAPI Server: Running in separate window
echo API Docs: http://localhost:8000/docs
echo.
echo To stop: Close the Celery and FastAPI windows
echo ========================================
pause