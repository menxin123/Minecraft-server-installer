@echo off
setlocal enabledelayedexpansion

:: 设置JVM参数和程序参数
set JVM_ARGS=-Xmx1024m -Xms512m
set PROGRAM_ARGS=-nogui

:: 检测当前目录下带有forge字样的第一个.jar文件
set "FORGE_JAR_FILE="
for %%f in (*forge*.jar) do (
    set "FORGE_JAR_FILE=%%f"
    goto :runjar
)

:: 如果没有找到带forge字样的.jar文件，则检测当前目录下的第一个.jar文件
if not defined FORGE_JAR_FILE (
    for %%f in (*.jar) do (
        set "JAR_FILE=%%f"
        goto :runjar
    )
)

:runjar
if defined FORGE_JAR_FILE (
    echo Found Forge JAR file: !FORGE_JAR_FILE!
    java\bin\java.exe %JVM_ARGS% -jar !FORGE_JAR_FILE! %PROGRAM_ARGS%
) else if defined JAR_FILE (
    echo Found JAR file: !JAR_FILE!
    java\bin\java.exe %JVM_ARGS% -jar !JAR_FILE! %PROGRAM_ARGS%
) else (
    echo No JAR files found.
)

endlocal
pause
