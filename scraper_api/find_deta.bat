@echo off
echo Finding Deta CLI executable...
echo.

REM Try to find deta in PATH
where deta >nul 2>nul
if %errorlevel% == 0 (
    echo Deta CLI found in PATH:
    where deta
    echo.
    echo You can run: deta login
    goto end
)

REM Check common Python Scripts directories
set "scripts_dir1=%LOCALAPPDATA%\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts"
set "scripts_dir2=%USERPROFILE%\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts"

if exist "%scripts_dir1%\deta.exe" (
    echo Deta CLI found at:
    echo %scripts_dir1%\deta.exe
    echo.
    echo You can run: "%scripts_dir1%\deta.exe" login
    goto end
)

if exist "%scripts_dir2%\deta.exe" (
    echo Deta CLI found at:
    echo %scripts_dir2%\deta.exe
    echo.
    echo You can run: "%scripts_dir2%\deta.exe" login
    goto end
)

echo Deta CLI not found.
echo Please install it with: pip install deta

:end
echo.
echo Press any key to continue...
pause >nul