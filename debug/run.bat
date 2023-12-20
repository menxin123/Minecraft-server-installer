@echo off
setlocal enabledelayedexpansion

:: 设置JVM参数和程序参数
set JVM_ARGS=-Xmx1024m -Xms512m
set PROGRAM_ARGS=-nogui

:: 检测当前目录下的第一个.jar文件
for %%f in (*.jar) do (
    set "JAR_FILE=%%f"
    goto :runjar
)

:runjar
if defined JAR_FILE (
    echo Found JAR file: !JAR_FILE!
    java\bin\java.exe %JVM_ARGS% -jar !JAR_FILE! %PROGRAM_ARGS%
) else (
    echo No JAR files found.
)

endlocal
pause
