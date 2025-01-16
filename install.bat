@echo off
echo Installing required Python packages...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Failed to install some packages. Please check the error messages above.
    pause
    exit /b %ERRORLEVEL%
)
echo All packages installed successfully!
pause
