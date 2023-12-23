#!/bin/bash

# 设置JVM参数和程序参数
JVM_ARGS="-Xmx1024m -Xms512m"
PROGRAM_ARGS="-nogui"

# 检测当前目录下带有forge字样的第一个.jar文件
FORGE_JAR_FILE=$(find . -maxdepth 1 -name '*forge*.jar' | head -n 1)
FORGE_JAR_FILE=${FORGE_JAR_FILE:2}

# 如果没有找到带forge字样的.jar文件，则检测当前目录下的第一个.jar文件
if [ -z "$FORGE_JAR_FILE" ]; then
  JAR_FILE=$(find . -maxdepth 1 -name '*.jar' | head -n 1)
  JAR_FILE=${JAR_FILE:2}
else
  JAR_FILE="$FORGE_JAR_FILE"
fi

# 运行.jar文件
if [ -n "$JAR_FILE" ]; then
  echo "Found JAR file: $JAR_FILE"
  ./java/bin/java $JVM_ARGS -jar "$JAR_FILE" $PROGRAM_ARGS
else
  echo "No JAR files found."
fi
