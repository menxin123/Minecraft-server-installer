import os
import platform
import requests
from tqdm import tqdm
import zipfile
import shutil


def get_os_arch():
    os_name = platform.system().lower()
    arch, _ = platform.architecture()
    return os_name, arch


java_versions = {
    "windows": {
        "x86": {
            "v1": "https://download.bell-sw.com/java/17.0.9+11/bellsoft-jdk17.0.9+11-windows-i586-lite.zip",
            "v2": "https://download.bell-sw.com/java/11.0.21+10/bellsoft-jdk11.0.21+10-windows-i586-lite.zip",
            "v3": "https://download.bell-sw.com/java/8u392+9/bellsoft-jdk8u392+9-windows-i586-lite.zip",
        },
        "x64": {
            "v1": "https://download.bell-sw.com/java/17.0.9+11/bellsoft-jdk17.0.9+11-windows-amd64-lite.zip",
            "v2": "https://download.bell-sw.com/java/11.0.21+10/bellsoft-jdk11.0.21+10-windows-amd64-lite.zip",
            "v3": "https://download.bell-sw.com/java/8u392+9/bellsoft-jdk8u392+9-windows-amd64-lite.zip",
        },
        "arm": {
            "v1": "",
            "v2": "",
            "v3": ""
        }
    },
    "linux": {
        "x86": {
            "v1": "linux-x86-java-lite-v1-url",
            "v2": "linux-x86-java-lite-v2-url",
            "v3": "linux-x86-java-lite-v3-url",
        },
        "x64": {
            "v1": "linux-x64-java-lite-v1-url",
            "v2": "linux-x64-java-lite-v2-url",
            "v3": "linux-x64-java-lite-v3-url",
        },
        "arm": {
            "v1": "linux-arm-java-lite-v1-url",
            "v2": "linux-arm-java-lite-v2-url",
            "v3": "linux-arm-java-lite-v3-url",
        }
    },
    "darwin": {
        "x64": {
            "v1": "macos-x64-java-lite-v1-url",
            "v2": "macos-x64-java-lite-v2-url",
            "v3": "macos-x64-java-lite-v3-url",
        },
        "arm": {
            "v1": "macos-arm-java-lite-v1-url",
            "v2": "macos-arm-java-lite-v2-url",
            "v3": "macos-arm-java-lite-v3-url",
        }
    }
}


def get_java_lite_url(os_name, arch_key, version_identifier):
    if os_name in java_versions and arch_key in java_versions[os_name]:
        if version_identifier in java_versions[os_name][arch_key]:
            return java_versions[os_name][arch_key][version_identifier]
    raise ValueError(f"No Java-Lite URL found for OS: {os_name}, Arch: {arch_key}, Version: {version_identifier}")


os_name, arch = get_os_arch()
arch_key = "x64" if "64" in arch else "x86"
if "arm" in arch.lower() or "aarch64" in arch.lower():
    arch_key = "arm"

java_lite_v1_url = get_java_lite_url(os_name, arch_key, "v1")
java_lite_v2_url = get_java_lite_url(os_name, arch_key, "v2")
java_lite_v3_url = get_java_lite_url(os_name, arch_key, "v3")

download_urls = {
    "1.20.4": "https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar",
    "java-lite-v1": java_lite_v1_url,
    "java-lite-v2": java_lite_v2_url,
    "java-lite-v3": java_lite_v3_url
    # ... 其他版本的 URL ...
}


# 检查并创建服务器目录
def get_server_directory():
    base_name = "server"
    base_dir = base_name
    counter = 1
    while os.path.exists(base_dir):
        base_dir = f"{base_name}{counter}"
        counter += 1
    os.makedirs(base_dir)
    return base_dir


# 提示用户输入下载目录
def prompt_for_download_directory():
    user_input_directory = input("请输入下载目录（留空则使用默认目录）: ").strip()
    return user_input_directory if user_input_directory else get_server_directory()


# 创建下载函数
# 根据URL获取文件名
def get_filename_from_url(url):
    return url.split('/')[-1]


# 创建下载并解压函数
def make_download_and_extract_function(url):
    def download_and_extract(download_directory):
        filename = get_filename_from_url(url)
        destination = os.path.join(download_directory, filename)

        # 下载文件
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(destination, 'wb') as file, tqdm(
                    desc=filename,
                    total=int(response.headers.get('content-length', 0)),
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
            ) as bar:
                for chunk in response.iter_content(chunk_size=1024):
                    bar.update(len(chunk))
                    file.write(chunk)
            print(f"Downloaded: {destination}")

            # 如果文件是ZIP格式，解压它
            if destination.endswith('.zip'):
                with zipfile.ZipFile(destination, 'r') as zip_ref:
                    zip_ref.extractall(download_directory)
                print(f"Extracted: {destination}")

                # 删除原始的ZIP文件
                os.remove(destination)
                print(f"Deleted ZIP file: {destination}")

                # 查找和重命名特定文件夹
                for folder_name in ["jdk-17.0.9-lite", "jdk-11.0.21-lite", "jdk8u392-lite"]:
                    folder_path = os.path.join(download_directory, folder_name)
                    if os.path.exists(folder_path):
                        java_path = os.path.join(download_directory, 'java')
                        if os.path.exists(java_path):
                            shutil.rmtree(java_path)
                        shutil.move(folder_path, java_path)
                        print(f"Renamed '{folder_name}' to 'java'")
                        break  # 只重命名找到的第一个匹配的文件夹
        else:
            print(f"Failed to download: {url}")

    return download_and_extract


# 创建下载函数的字典
download_functions = {version: make_download_and_extract_function(url) for version, url in download_urls.items()}


def download_files(download_directory, versions):
    for version in versions:
        if version in download_functions:
            download_functions[version](download_directory)
        else:
            print(f"Version {version} not found in download functions.")


# 函数生成器，用于创建 item_functions1 中的选项函数
def create_option_function(versions):
    def option_function():
        download_directory = prompt_for_download_directory()
        download_files(download_directory, versions)
        exit_program()

    return option_function


def download_version_files(version, files_list):
    download_directory = prompt_for_download_directory()
    download_files(download_directory, files_list)


def clear_screen():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
    else:
        print("无法清屏：不支持的操作系统")


def exit_program():
    clear_screen()
    print("已完成")
    input("按下任意键继续...")
    exit()


version_files_mapping = {
    "Minecraft_server": {
        "1.20.4": ["1.20.4", "java-lite-v"],
        "1.20.3": ["1.20.3", "java-lite-v"],
        "1.20.2": ["1.20.2", "java-lite-v"],
        "1.20.1": ["1.20.1", "java-lite-v"],
        "1.20": ["1.20", "java-lite-v"],
        "1.19.4": ["1.19.4", "java-lite-v"],
        "1.19.3": ["1.19.3", "java-lite-v"],
        "1.19.2": ["1.19.2", "java-lite-v"],
        "1.19.1": ["1.19.1", "java-lite-v"],
        "1.19": ["1.19", "java-lite-v"],
        "1.18.2": ["1.18.2", "java-lite-v"],
        "1.18.1": ["1.18.1", "java-lite-v"],
        "1.18": ["1.18", "java-lite-v"],
        "1.17.1": ["1.17.1", "java-lite-v"],
        "1.17": ["1.17", "java-lite-v"],
        "1.16.5": ["1.16.5", "java-lite-v"],
        "1.16.4": ["1.16.4", "java-lite-v"],
        "1.16.3": ["1.16.3", "java-lite-v"],
        "1.16.2": ["1.16.2", "java-lite-v"],
        "1.16.1": ["1.16.1", "java-lite-v"],
        "1.16": ["1.16", "java-lite-v"],
        "1.15.2": ["1.15.2", "java-lite-v"],
        "1.15.1": ["1.15.1", "java-lite-v"],
        "1.15": ["1.15", "java-lite-v"],
        "1.14.4": ["1.14.4", "java-lite-v"],
        "1.14.3": ["1.14.3", "java-lite-v"],
        "1.14.2": ["1.14.2", "java-lite-v"],
        "1.14.1": ["1.14.1", "java-lite-v"],
        "1.14": ["1.14", "java-lite-v"],
        "1.13.2": ["1.13.2", "java-lite-v"],
        "1.13.1": ["1.13.1", "java-lite-v"],
        "1.13": ["1.13", "java-lite-v"],
        "1.12.2": ["1.12.2", "java-lite-v"],
        "1.12.1": ["1.12.1", "java-lite-v"],
        "1.12": ["1.12", "java-lite-v"],
        "1.11.2": ["1.11.2", "java-lite-v"],
        "1.11.1": ["1.11.1", "java-lite-v"],
        "1.11": ["1.11", "java-lite-v"],
        "1.10.2": ["1.10.2", "java-lite-v"],
        "1.10.1": ["1.10.1", "java-lite-v"],
        "1.10": ["1.10", "java-lite-v"],
        "1.9.4": ["1.9.4", "java-lite-v"],
        "1.9.3": ["1.9.3", "java-lite-v"],
        "1.9.2": ["1.9.2", "java-lite-v"],
        "1.9.1": ["1.9.1", "java-lite-v"],
        "1.9": ["1.9", "java-lite-v"],
        "1.8.9": ["1.8.9", "java-lite-v"],
        "1.8.8": ["1.8.8", "java-lite-v"],
        "1.8.7": ["1.8.7", "java-lite-v"],
        "1.8.6": ["1.8.6", "java-lite-v"],
        "1.8.5": ["1.8.5", "java-lite-v"],
        "1.8.4": ["1.8.4", "java-lite-v"],
        "1.8.3": ["1.8.3", "java-lite-v"],
        "1.8.2": ["1.8.2", "java-lite-v"],
        "1.8.1": ["1.8.1", "java-lite-v"],
        "1.8": ["1.8", "java-lite-v"],
        "1.7.10": ["1.7.10", "java-lite-v"],
        "1.7.9": ["1.7.9", "java-lite-v"],
        "1.7.8": ["1.7.8", "java-lite-v"],
        "1.7.7": ["1.7.7", "java-lite-v"],
        "1.7.6": ["1.7.6", "java-lite-v"],
        "1.7.5": ["1.7.5", "java-lite-v"],
        "1.7.4": ["1.7.4", "java-lite-v"],
        "1.7.2": ["1.7.2", "java-lite-v"],
        "1.6.4": ["1.6.4", "java-lite-v"],
        "1.6.2": ["1.6.2", "java-lite-v"],
        "1.6.1": ["1.6.1", "java-lite-v"],
        "1.5.2": ["1.5.2", "java-lite-v"],
        "1.5.1": ["1.5.1", "java-lite-v"],
        "1.5": ["1.5", "java-lite-v"],
        "1.4.7": ["1.4.7", "java-lite-v"],
        "1.4.6": ["1.4.6", "java-lite-v"],
        "1.4.5": ["1.4.5", "java-lite-v"],
        "1.4.4": ["1.4.4", "java-lite-v"],
        "1.4.3": ["1.4.3", "java-lite-v"],
        "1.4.2": ["1.4.2", "java-lite-v"],
        "1.4.1": ["1.4.1", "java-lite-v"],
        "1.4.0": ["1.4.0", "java-lite-v"],
        "1.3.2": ["1.3.2", "java-lite-v"],
        "1.2.5": ["1.2.5", "java-lite-v"],
        "1.2.4": ["1.2.4", "java-lite-v"],
        "1.2.3": ["1.2.3", "java-lite-v"],
        "1.1": ["1.1", "java-lite-v"],
        "1.0.1": ["1.0.1", "java-lite-v"],
        "1.0.0": ["1.0.0", "java-lite-v"]
    },
    "Forge_server": {
        "1.20.4": ["1.20.4", "java-lite-v"],
        "1.20.3": ["1.20.3", "java-lite-v"],
        "1.20.2": ["1.20.2", "java-lite-v"],
        "1.20.1": ["1.20.1", "java-lite-v"],
        "1.20": ["1.20", "java-lite-v"],
        "1.19.4": ["1.19.4", "java-lite-v"],
        "1.19.3": ["1.19.3", "java-lite-v"],
        "1.19.2": ["1.19.2", "java-lite-v"],
        "1.19.1": ["1.19.1", "java-lite-v"],
        "1.19": ["1.19", "java-lite-v"],
        "1.18.2": ["1.18.2", "java-lite-v"],
        "1.18.1": ["1.18.1", "java-lite-v"],
        "1.18": ["1.18", "java-lite-v"],
        "1.17.1": ["1.17.1", "java-lite-v"],
        "1.16.5": ["1.16.5", "java-lite-v"],
        "1.16.4": ["1.16.4", "java-lite-v"],
        "1.16.3": ["1.16.3", "java-lite-v"],
        "1.16.2": ["1.16.2", "java-lite-v"],
        "1.16.1": ["1.16.1", "java-lite-v"],
        "1.15.2": ["1.15.2", "java-lite-v"],
        "1.15.1": ["1.15.1", "java-lite-v"],
        "1.15": ["1.15", "java-lite-v"],
        "1.14.4": ["1.14.4", "java-lite-v"],
        "1.14.3": ["1.14.3", "java-lite-v"],
        "1.14.2": ["1.14.2", "java-lite-v"],
        "1.13.2": ["1.13.2", "java-lite-v"],
        "1.12.2": ["1.12.2", "java-lite-v"],
        "1.12.1": ["1.12.1", "java-lite-v"],
        "1.12": ["1.12", "java-lite-v"],
        "1.11.2": ["1.11.2", "java-lite-v"],
        "1.11": ["1.11", "java-lite-v"],
        "1.10.2": ["1.10.2", "java-lite-v"],
        "1.10": ["1.10", "java-lite-v"],
        "1.9.4": ["1.9.4", "java-lite-v"],
        "1.9": ["1.9", "java-lite-v"],
        "1.8.9": ["1.8.9", "java-lite-v"],
        "1.8.8": ["1.8.8", "java-lite-v"],
        "1.8": ["1.8", "java-lite-v"],
        "1.7.10": ["1.7.10", "java-lite-v"],
        "1.7.10_pre4": ["1.7.10_pre4", "java-lite-v"],
        "1.7.2": ["1.7.2", "java-lite-v"],
        "1.6.4": ["1.6.4", "java-lite-v"],
        "1.6.3": ["1.6.3", "java-lite-v"],
        "1.6.2": ["1.6.2", "java-lite-v"],
        "1.6.1": ["1.6.1", "java-lite-v"],
        "1.5.2": ["1.5.2", "java-lite-v"],
        "1.5.1": ["1.5.1", "java-lite-v"],
        "1.5": ["1.5", "java-lite-v"],
        "1.4.7": ["1.4.7", "java-lite-v"],
        "1.4.6": ["1.4.6", "java-lite-v"],
        "1.4.5": ["1.4.5", "java-lite-v"],
        "1.4.4": ["1.4.4", "java-lite-v"],
        "1.4.3": ["1.4.3", "java-lite-v"],
        "1.4.2": ["1.4.2", "java-lite-v"],
        "1.4.1": ["1.4.1", "java-lite-v"],
        "1.4.0": ["1.4.0", "java-lite-v"],
        "1.3.2": ["1.3.2", "java-lite-v"],
        "1.2.5": ["1.2.5", "java-lite-v"],
        "1.2.4": ["1.2.4", "java-lite-v"],
        "1.2.3": ["1.2.3", "java-lite-v"],
        "1.1": ["1.1", "java-lite-v"],
        "1.0.1": ["1.0.1", "java-lite-v"],
        "1.0.0": ["1.0.0", "java-lite-v"]
    },
    "Fabric_server": {
        "1.20.4": ["1.20.4", "java-lite-v"],
        "1.20.3": ["1.20.3", "java-lite-v"],
        "1.20.2": ["1.20.2", "java-lite-v"],
        "1.20.1": ["1.20.1", "java-lite-v"],
        "1.20": ["1.20", "java-lite-v"],
        "1.19.4": ["1.19.4", "java-lite-v"],
        "1.19.3": ["1.19.3", "java-lite-v"],
        "1.19.2": ["1.19.2", "java-lite-v"],
        "1.19.1": ["1.19.1", "java-lite-v"],
        "1.19": ["1.19", "java-lite-v"],
        "1.18.2": ["1.18.2", "java-lite-v"],
        "1.18.1": ["1.18.1", "java-lite-v"],
        "1.18": ["1.18", "java-lite-v"],
        "1.17.1": ["1.17.1", "java-lite-v"],
        "1.17": ["1.17", "java-lite-v"],
        "1.16.5": ["1.16.5", "java-lite-v"],
        "1.16.4": ["1.16.4", "java-lite-v"],
        "1.16.3": ["1.16.3", "java-lite-v"],
        "1.16.2": ["1.16.2", "java-lite-v"],
        "1.16.1": ["1.16.1", "java-lite-v"],
        "1.16": ["1.16", "java-lite-v"],
        "1.15.2": ["1.15.2", "java-lite-v"],
        "1.15.1": ["1.15.1", "java-lite-v"],
        "1.15": ["1.15", "java-lite-v"],
        "1.14.4": ["1.14.4", "java-lite-v"],
        "1.14.3": ["1.14.3", "java-lite-v"],
        "1.14.2": ["1.14.2", "java-lite-v"],
        "1.13.2": ["1.13.2", "java-lite-v"],
        "1.12.2": ["1.12.2", "java-lite-v"],
        "1.12.1": ["1.12.1", "java-lite-v"],
        "1.12": ["1.12", "java-lite-v"],
        "1.11.2": ["1.11.2", "java-lite-v"],
        "1.10.2": ["1.10.2", "java-lite-v"],
        "1.9.4": ["1.9.4", "java-lite-v"],
        "1.8.8": ["1.8.8", "java-lite-v"]
    },
    "Cat_server": {
        "1.18.2": ["1.18.2", "java-lite-v"],
        "1.16.5": ["1.16.5", "java-lite-v"],
        "1.12.2": ["1.12.2", "java-lite-v"]
    },
    "Mohist_server": {
        "1.7.10": ["1.7.10", "java-lite-v"],
        "1.12.2": ["1.12.2", "java-lite-v"],
        "1.16.5": ["1.16.5", "java-lite-v"],
        "1.18.2": ["1.18.2", "java-lite-v"],
        "1.19.2": ["1.19.2", "java-lite-v"],
        "1.19.4": ["1.19.4", "java-lite-v"],
        "1.20": ["1.20", "java-lite-v"],
        "1.20.1": ["1.20.1", "java-lite-v"],
        "1.20.2": ["1.20.2", "java-lite-v"]
    },
    "Banner_server": {
        "1.19.4": ["1.19.4", "java-lite-v"],
        "1.20": ["1.20", "java-lite-v"],
        "1.20.1": ["1.20.1", "java-lite-v"]
    },
    "Craftbukkit_server": {
        "1.20.4": ["1.20.4", "java-lite-v"],
        "1.20.2": ["1.20.2", "java-lite-v"],
        "1.20.1": ["1.20.1", "java-lite-v"],
        "1.19.4": ["1.19.4", "java-lite-v"],
        "1.19.3": ["1.19.3", "java-lite-v"],
        "1.19.2": ["1.19.2", "java-lite-v"],
        "1.19.1": ["1.19.1", "java-lite-v"],
        "1.19": ["1.19", "java-lite-v"],
        "1.18.2": ["1.18.2", "java-lite-v"],
        "1.18.1": ["1.18.1", "java-lite-v"],
        "1.18": ["1.18", "java-lite-v"],
        "1.17.1": ["1.17.1", "java-lite-v"],
        "1.17": ["1.17", "java-lite-v"],
        "1.16.5": ["1.16.5", "java-lite-v"],
        "1.16.4": ["1.16.4", "java-lite-v"],
        "1.16.3": ["1.16.3", "java-lite-v"],
        "1.16.2": ["1.16.2", "java-lite-v"],
        "1.16.1": ["1.16.1", "java-lite-v"],
        "1.15.2": ["1.15.2", "java-lite-v"],
        "1.15.1": ["1.15.1", "java-lite-v"],
        "1.15": ["1.15", "java-lite-v"],
        "1.14.4": ["1.14.4", "java-lite-v"],
        "1.14.3": ["1.14.3", "java-lite-v"],
        "1.14.2": ["1.14.2", "java-lite-v"],
        "1.14.1": ["1.14.1", "java-lite-v"],
        "1.14": ["1.14", "java-lite-v"],
        "1.13.2": ["1.13.2", "java-lite-v"],
        "1.13.1": ["1.13.1", "java-lite-v"],
        "1.13": ["1.13", "java-lite-v"],
        "1.12.2": ["1.12.2", "java-lite-v"],
        "1.12.1": ["1.12.1", "java-lite-v"],
        "1.12": ["1.12", "java-lite-v"],
        "1.11.2": ["1.11.2", "java-lite-v"],
        "1.11.1": ["1.11.1", "java-lite-v"],
        "1.11": ["1.11", "java-lite-v"],
        "1.10.2": ["1.10.2", "java-lite-v"],
        "1.10": ["1.10", "java-lite-v"],
        "1.9.4": ["1.9.4", "java-lite-v"],
        "1.9.2": ["1.9.2", "java-lite-v"],
        "1.9": ["1.9", "java-lite-v"],
        "1.8.8": ["1.8.8", "java-lite-v"],
        "1.8.7": ["1.8.7", "java-lite-v"],
        "1.8.6": ["1.8.6", "java-lite-v"],
        "1.8.5": ["1.8.5", "java-lite-v"],
        "1.8.4": ["1.8.4", "java-lite-v"],
        "1.8.3": ["1.8.3", "java-lite-v"],
        "1.8": ["1.8", "java-lite-v"],
        "1.7.10": ["1.7.10", "java-lite-v"],
        "1.7.9": ["1.7.9", "java-lite-v"],
        "1.7.8": ["1.7.8", "java-lite-v"],
        "1.7.5": ["1.7.5", "java-lite-v"],
        "1.7.2": ["1.7.2", "java-lite-v"],
        "1.6.4": ["1.6.4", "java-lite-v"],
        "1.6.2": ["1.6.2", "java-lite-v"],
        "1.5.2": ["1.5.2", "java-lite-v"],
        "1.5.1": ["1.5.1", "java-lite-v"],
        "1.4.7": ["1.4.7", "java-lite-v"],
        "1.4.6": ["1.4.6", "java-lite-v"]
    },
    "Spigot_server": {
        "1.20.4": ["1.20.4", "java-lite-v"],
        "1.20.2": ["1.20.2", "java-lite-v"],
        "1.20.1": ["1.20.1", "java-lite-v"],
        "1.19.4": ["1.19.4", "java-lite-v"],
        "1.19.3": ["1.19.3", "java-lite-v"],
        "1.19.2": ["1.19.2", "java-lite-v"],
        "1.19.1": ["1.19.1", "java-lite-v"],
        "1.19": ["1.19", "java-lite-v"],
        "1.18.2": ["1.18.2", "java-lite-v"],
        "1.18.1": ["1.18.1", "java-lite-v"],
        "1.18": ["1.18", "java-lite-v"],
        "1.17.1": ["1.17.1", "java-lite-v"],
        "1.17": ["1.17", "java-lite-v"],
        "1.16.5": ["1.16.5", "java-lite-v"],
        "1.16.4": ["1.16.4", "java-lite-v"],
        "1.16.3": ["1.16.3", "java-lite-v"],
        "1.16.2": ["1.16.2", "java-lite-v"],
        "1.16.1": ["1.16.1", "java-lite-v"],
        "1.15.2": ["1.15.2", "java-lite-v"],
        "1.15.1": ["1.15.1", "java-lite-v"],
        "1.15": ["1.15", "java-lite-v"],
        "1.14.4": ["1.14.4", "java-lite-v"],
        "1.14.3": ["1.14.3", "java-lite-v"],
        "1.14.2": ["1.14.2", "java-lite-v"],
        "1.14.1": ["1.14.1", "java-lite-v"],
        "1.14": ["1.14", "java-lite-v"],
        "1.13.2": ["1.13.2", "java-lite-v"],
        "1.13.1": ["1.13.1", "java-lite-v"],
        "1.13": ["1.13", "java-lite-v"],
        "1.12.2": ["1.12.2", "java-lite-v"],
        "1.12.1": ["1.12.1", "java-lite-v"],
        "1.12": ["1.12", "java-lite-v"],
        "1.11.2": ["1.11.2", "java-lite-v"],
        "1.10.2": ["1.10.2", "java-lite-v"],
        "1.9.4": ["1.9.4", "java-lite-v"],
        "1.8.8": ["1.8.8", "java-lite-v"]
    },
    "Paper_server": {
        "1.20.4": ["1.20.4", "java-lite-v"],
        "1.20.2": ["1.20.2", "java-lite-v"],
        "1.20.1": ["1.20.1", "java-lite-v"],
        "1.20": ["1.20", "java-lite-v"],
        "1.19.4": ["1.19.4", "java-lite-v"],
        "1.19.3": ["1.19.3", "java-lite-v"],
        "1.19.2": ["1.19.2", "java-lite-v"],
        "1.19.1": ["1.19.1", "java-lite-v"],
        "1.19": ["1.19", "java-lite-v"],
        "1.18.2": ["1.18.2", "java-lite-v"],
        "1.18.1": ["1.18.1", "java-lite-v"],
        "1.18": ["1.18", "java-lite-v"],
        "1.17.1": ["1.17.1", "java-lite-v"],
        "1.17": ["1.17", "java-lite-v"],
        "1.16.5": ["1.16.5", "java-lite-v"],
        "1.16.4": ["1.16.4", "java-lite-v"],
        "1.16.3": ["1.16.3", "java-lite-v"],
        "1.16.2": ["1.16.2", "java-lite-v"],
        "1.16.1": ["1.16.1", "java-lite-v"],
        "1.15.2": ["1.15.2", "java-lite-v"],
        "1.15.1": ["1.15.1", "java-lite-v"],
        "1.15": ["1.15", "java-lite-v"],
        "1.14.4": ["1.14.4", "java-lite-v"],
        "1.14.3": ["1.14.3", "java-lite-v"],
        "1.14.2": ["1.14.2", "java-lite-v"],
        "1.14.1": ["1.14.1", "java-lite-v"],
        "1.14": ["1.14", "java-lite-v"],
        "1.13.2": ["1.13.2", "java-lite-v"],
        "1.13.1": ["1.13.1", "java-lite-v"],
        "1.13": ["1.13", "java-lite-v"],
        "1.13-pre7": ["1.13-pre7", "java-lite-v"],
        "1.12.2": ["1.12.2", "java-lite-v"],
        "1.12.1": ["1.12.1", "java-lite-v"],
        "1.12": ["1.12", "java-lite-v"],
        "1.11.2": ["1.11.2", "java-lite-v"],
        "1.10.2": ["1.10.2", "java-lite-v"],
        "1.9.4": ["1.9.4", "java-lite-v"],
        "1.8.8": ["1.8.8", "java-lite-v"]
    },
    "Velocity_server": {
        "3.3.0-SNAPSHOT": ["3.3.0-SNAPSHOT", "java-lite-v"],
        "3.2.0-SNAPSHOT": ["3.2.0-SNAPSHOT", "java-lite-v"],
        "3.1.2-SNAPSHOT": ["3.1.2-SNAPSHOT", "java-lite-v"],
        "3.1.1-SNAPSHOT": ["3.1.1-SNAPSHOT", "java-lite-v"],
        "3.1.1": ["3.1.1", "java-lite-v"],
        "3.1.0": ["3.1.0", "java-lite-v"],
        "1.1.9": ["1.1.9", "java-lite-v"],
        "1.0.10": ["1.0.10", "java-lite-v"]
    },
    "Waterfall_server": {
        "1.20": ["1.20", "java-lite-v"],
        "1.19": ["1.19", "java-lite-v"],
        "1.18": ["1.18", "java-lite-v"],
        "1.17": ["1.17", "java-lite-v"],
        "1.16": ["1.16", "java-lite-v"],
        "1.15": ["1.15", "java-lite-v"],
        "1.14": ["1.14", "java-lite-v"],
        "1.13": ["1.13", "java-lite-v"],
        "1.12": ["1.12", "java-lite-v"],
        "1.11": ["1.11", "java-lite-v"]
    }
}


def execute_option_logic(content_tuple):
    title, content_list = content_tuple
    items_per_page = 10  # 设置每页所需的项目数
    current_page = 0
    max_page_num = (len(content_list) - 1) // items_per_page + 1

    while True:
        clear_screen()
        print(f"当前页内容 - {title}:")
        start_index = current_page * items_per_page
        end_index = min((current_page + 1) * items_per_page, len(content_list))
        for i, version in enumerate(content_list[start_index:end_index], start=start_index):
            print(f"{i + 1}. {version}")

        user_input = input("\n输入a切换上一页，输入b切换下一页，输入q退出，选择内容编号执行自定义函数：")
        if user_input == 'a':
            if current_page > 0:
                current_page -= 1
            else:
                print("\n已经是第一页，无法向前翻页。")
        elif user_input == 'b':
            if current_page < max_page_num - 1:
                current_page += 1
            else:
                print("\n已经是最后一页，无法向后翻页。")
        elif user_input == 'q':
            break
        else:
            try:
                selected_item_index = int(user_input) - 1
                # 确保用户选择的是当前页面上的选项
                if start_index <= selected_item_index < end_index:
                    selected_version = content_list[selected_item_index]
                    if selected_version in version_files_mapping[title]:
                        files_list = version_files_mapping[title][selected_version]
                        download_version_files(selected_version, files_list)
                    else:
                        print("\n该选项没有对应的下载信息。")
                else:
                    print("\n选择的编号不在当前页面，请重新输入。")
            except (ValueError, IndexError):
                print("\n无效的选择，请重新输入。")


text = '-' * 23 + "\n请输入你的选择（输入t退出）："


def main_menu():
    server_options = {
        "1": "Minecraft_server",
        "2": "Forge_server",
        "3": "Fabric_server",
        "4": "Cat_server",
        "5": "Mohist_server",
        "6": "Banner_server",
        "7": "Craftbukkit_server",
        "8": "Spigot_server",
        "9": "Paper_server",
        "10": "Velocity_server",
        "11": "Waterfall_server",
        # ... 其他服务器类型 ...
    }
    while True:
        user_input = input("---------主菜单---------\n1. Minecraft server\n2. Forge server\n3. Fabric_server\n4. "
                           "Cat_server\n5. Mohist_server\n6. Banner_server\n7. Craftbukkit_server\n8. "
                           "Spigot_server\n9. Paper_server\n10. Velocity_server\n11. "
                           "Waterfall_server\n-----------------------\n输入数字选择,输入q退出:")

        if user_input in server_options:
            server_type = server_options[user_input]
            content_tuple = (server_type, list(version_files_mapping[server_type].keys()))
            execute_option_logic(content_tuple)
        elif user_input == 'q':
            exit()
        else:
            print("无效的选择，请重新输入。")


# 调用主菜单函数
if __name__ == "__main__":
    main_menu()
