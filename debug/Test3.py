import requests

def make_download_function(url, destination):
    def download_function():
        # 发起请求
        response = requests.get(url, stream=True)
        # 确保请求成功
        if response.status_code == 200:
            # 打开文件进行写入
            with open(destination, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"下载完成：{destination}")
        else:
            print(f"下载失败，HTTP 状态码：{response.status_code}")
    return download_function

# 示例用法
download_urls = {
    "1.20.4": "http://example.com/minecraft_server.1.20.4.jar",
    "1.20.2": "http://example.com/minecraft_server.1.20.2.jar",
    # ... 其他版本
}

# 创建一个字典来保存生成的下载函数
download_functions = {}
for version, url in download_urls.items():
    destination_path = f"server.{version}.jar"
    download_functions[version] = make_download_function(url, destination_path)

# 现在可以调用特定版本的下载函数
version_to_download = "1.20.4"  # 假设用户选择了这个版本
download_functions[version_to_download]()
