#!/bin/bash

# 设置JVM参数和程序参数
JVM_ARGS="-Xmx1024m -Xms512m"
PROGRAM_ARGS="-nogui"

# 检测当前目录下的第一个.jar文件
JAR_FILE=""
for f in *.jar; do
  JAR_FILE="$f"
  break
done

# 运行.jar文件
if [ -n "$JAR_FILE" ]; then
  echo "Found JAR file: $JAR_FILE"
  ./java/bin/java $JVM_ARGS -jar "$JAR_FILE" $PROGRAM_ARGS
else
  echo "No JAR files found."
fi
