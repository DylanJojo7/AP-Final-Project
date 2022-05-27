@echo off
color 3
echo Step 1/
echo.
echo Welcome to MP3 Converter Setup! To start, download python. (https://www.python.org/ftp/python/3.6.0/python-3.6.0-amd64.exe). While downloading, 
echo MAKE SURE YOU SELECT ADD TO PATH. If you do not, the application will not work.
echo.
set /p=Press ENTER to continue with installation... 
echo.
echo Now, the python packages needed will be installed. Please wait.
pip install pydub
pip install ffmpeg
echo .
echo Now, you can run the "run.bat" file to run the program.
timeout 5