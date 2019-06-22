@ECHO OFF
ECHO.
ECHO.
ECHO ============================= Running tests =============================
ECHO.
ECHO.
SLEEP 1
python -m pytest -v --cov-report html --cov-report term --cov=..\reshade .
ECHO.
ECHO.
ECHO ============================= Checking code style =============================
ECHO.
ECHO.
SLEEP 1
pycodestyle -v ..\reshade\
