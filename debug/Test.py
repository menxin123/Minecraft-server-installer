import os
import platform
import shutil
import requests
from tqdm import tqdm
import zipfile
import tarfile


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
        }
    },
    "linux": {
        "x86": {
            "v1": "https://download.bell-sw.com/java/17.0.9+11/bellsoft-jdk17.0.9+11-linux-i586-lite.tar.gz",
            "v2": "https://download.bell-sw.com/java/11.0.21+10/bellsoft-jdk11.0.21+10-linux-i586-lite.tar.gz",
            "v3": "https://download.bell-sw.com/java/8u392+9/bellsoft-jdk8u392+9-linux-i586-lite.tar.gz",
        },
        "x64": {
            "v1": "https://download.bell-sw.com/java/17.0.9+11/bellsoft-jdk17.0.9+11-linux-amd64-lite.tar.gz",
            "v2": "https://download.bell-sw.com/java/11.0.21+10/bellsoft-jdk11.0.21+10-linux-amd64-lite.tar.gz",
            "v3": "https://download.bell-sw.com/java/8u392+9/bellsoft-jdk8u392+9-linux-amd64-lite.tar.gz",
        },
        "arm": {
            "v1": "https://download.bell-sw.com/java/17.0.9+11/bellsoft-jdk17.0.9+11-linux-aarch64-lite.tar.gz",
            "v2": "https://download.bell-sw.com/java/11.0.21+10/bellsoft-jdk11.0.21+10-linux-aarch64-full.tar.gz",
            "v3": "https://download.bell-sw.com/java/8u392+9/bellsoft-jdk8u392+9-linux-aarch64-lite.tar.gz",
        },
        "arm32": {  # 假设这是 ARM 32位的键
            "v1": "https://download.bell-sw.com/java/17.0.9+11/bellsoft-jdk17.0.9+11-linux-arm32-vfp-hflt-lite.tar.gz",
            "v2": "https://download.bell-sw.com/java/11.0.21+10/bellsoft-jdk11.0.21+10-linux-arm32-vfp-hflt-lite.tar.gz",
            "v3": "https://cdn.azul.com/zulu-embedded/bin/zulu8.74.0.17-ca-jdk8.0.392-linux_aarch32sf.tar.gz",
        },
    },
    "darwin": {
        "x64": {
            "v1": "https://download.bell-sw.com/java/17.0.9+11/bellsoft-jdk17.0.9+11-macos-amd64-lite.tar.gz",
            "v2": "https://download.bell-sw.com/java/11.0.21+10/bellsoft-jdk11.0.21+10-macos-amd64-lite.tar.gz",
            "v3": "https://download.bell-sw.com/java/8u392+9/bellsoft-jdk8u392+9-macos-amd64-lite.tar.gz",
        },
        "arm": {
            "v1": "https://download.bell-sw.com/java/17.0.9+11/bellsoft-jdk17.0.9+11-macos-aarch64-lite.tar.gz",
            "v2": "https://download.bell-sw.com/java/11.0.21+10/bellsoft-jdk11.0.21+10-macos-aarch64-lite.tar.gz",
            "v3": "https://download.bell-sw.com/java/8u392+9/bellsoft-jdk8u392+9-macos-aarch64-lite.tar.gz",
        }
    }
}


def get_java_lite_url(os_name, arch_key, version_identifier):
    if os_name in java_versions and arch_key in java_versions[os_name]:
        if version_identifier in java_versions[os_name][arch_key]:
            return java_versions[os_name][arch_key][version_identifier]
    raise ValueError(f"No Java-Lite URL found for OS: {os_name}, Arch: {arch_key}, Version: {version_identifier}")


os_name, arch = get_os_arch()
if "arm" in arch.lower() or "aarch64" in arch.lower():
    arch_key = "arm"
elif "armv7l" in arch.lower() or "armhf" in arch.lower():
    arch_key = "arm32"  # 使用新添加的键
else:
    arch_key = "x64" if "64" in arch else "x86"

java_lite_v1_url = get_java_lite_url(os_name, arch_key, "v1")
java_lite_v2_url = get_java_lite_url(os_name, arch_key, "v2")
java_lite_v3_url = get_java_lite_url(os_name, arch_key, "v3")

download_urls = {
    "Minecraft_server_1.20.4": "https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar",
    "Minecraft_server_1.20.3": "xxx",
    "Minecraft_server_1.20.2": "xxx",
    "Minecraft_server_1.20.1": "xxx",
    "Minecraft_server_1.20": "xxx",
    "Minecraft_server_1.19.4": "xxx",
    "Minecraft_server_1.19.3": "xxx",
    "Minecraft_server_1.19.2": "xxx",
    "Minecraft_server_1.19.1": "xxx",
    "Minecraft_server_1.19": "xxx",
    "Minecraft_server_1.18.2": "xxx",
    "Minecraft_server_1.18.1": "xxx",
    "Minecraft_server_1.18": "xxx",
    "Minecraft_server_1.17.1": "xxx",
    "Minecraft_server_1.17": "xxx",
    "Minecraft_server_1.16.5": "xxx",
    "Minecraft_server_1.16.4": "xxx",
    "Minecraft_server_1.16.3": "xxx",
    "Minecraft_server_1.16.2": "xxx",
    "Minecraft_server_1.16.1": "xxx",
    "Minecraft_server_1.16": "xxx",
    "Minecraft_server_1.15.2": "xxx",
    "Minecraft_server_1.15.1": "xxx",
    "Minecraft_server_1.15": "xxx",
    "Minecraft_server_1.14.4": "xxx",
    "Minecraft_server_1.14.3": "xxx",
    "Minecraft_server_1.14.2": "xxx",
    "Minecraft_server_1.14.1": "xxx",
    "Minecraft_server_1.14": "xxx",
    "Minecraft_server_1.13.2": "xxx",
    "Minecraft_server_1.13.1": "xxx",
    "Minecraft_server_1.13": "xxx",
    "Minecraft_server_1.12.2": "xxx",
    "Minecraft_server_1.12.1": "xxx",
    "Minecraft_server_1.12": "xxx",
    "Minecraft_server_1.11.2": "xxx",
    "Minecraft_server_1.11.1": "xxx",
    "Minecraft_server_1.11": "xxx",
    "Minecraft_server_1.10.2": "xxx",
    "Minecraft_server_1.10.1": "xxx",
    "Minecraft_server_1.10": "xxx",
    "Minecraft_server_1.9.4": "xxx",
    "Minecraft_server_1.9.3": "xxx",
    "Minecraft_server_1.9.2": "xxx",
    "Minecraft_server_1.9.1": "xxx",
    "Minecraft_server_1.9": "xxx",
    "Minecraft_server_1.8.9": "xxx",
    "Minecraft_server_1.8.8": "xxx",
    "Minecraft_server_1.8.7": "xxx",
    "Minecraft_server_1.8.6": "xxx",
    "Minecraft_server_1.8.5": "xxx",
    "Minecraft_server_1.8.4": "xxx",
    "Minecraft_server_1.8.3": "xxx",
    "Minecraft_server_1.8.2": "xxx",
    "Minecraft_server_1.8.1": "xxx",
    "Minecraft_server_1.8": "xxx",
    "Minecraft_server_1.7.10": "xxx",
    "Minecraft_server_1.7.9": "xxx",
    "Minecraft_server_1.7.8": "xxx",
    "Minecraft_server_1.7.7": "xxx",
    "Minecraft_server_1.7.6": "xxx",
    "Minecraft_server_1.7.5": "xxx",
    "Minecraft_server_1.7.4": "xxx",
    "Minecraft_server_1.7.2": "xxx",
    "Minecraft_server_1.6.4": "xxx",
    "Minecraft_server_1.6.2": "xxx",
    "Minecraft_server_1.6.1": "xxx",
    "Minecraft_server_1.5.2": "xxx",
    "Minecraft_server_1.5.1": "xxx",
    "Minecraft_server_1.5": "xxx",
    "Minecraft_server_1.4.7": "xxx",
    "Minecraft_server_1.4.6": "xxx",
    "Minecraft_server_1.4.5": "xxx",
    "Minecraft_server_1.4.4": "xxx",
    "Minecraft_server_1.4.3": "xxx",
    "Minecraft_server_1.4.2": "xxx",
    "Minecraft_server_1.4.1": "xxx",
    "Minecraft_server_1.4.0": "xxx",
    "Minecraft_server_1.3.2": "xxx",
    "Minecraft_server_1.2.5": "xxx",
    "Minecraft_server_1.2.4": "xxx",
    "Minecraft_server_1.2.3": "xxx",
    "Minecraft_server_1.1": "xxx",
    "Minecraft_server_1.0.1": "xxx",
    "Minecraft_server_1.0.0": "xxx",
    "Forge_server_1.20.4": "xxx",
    "Forge_server_1.20.3": "xxx",
    "Forge_server_1.20.2": "xxx",
    "Forge_server_1.20.1": "xxx",
    "Forge_server_1.20": "xxx",
    "Forge_server_1.19.4": "xxx",
    "Forge_server_1.19.3": "xxx",
    "Forge_server_1.19.2": "xxx",
    "Forge_server_1.19.1": "xxx",
    "Forge_server_1.19": "xxx",
    "Forge_server_1.18.2": "xxx",
    "Forge_server_1.18.1": "xxx",
    "Forge_server_1.18": "xxx",
    "Forge_server_1.17.1": "xxx",
    "Forge_server_1.16.5": "xxx",
    "Forge_server_1.16.4": "xxx",
    "Forge_server_1.16.3": "xxx",
    "Forge_server_1.16.2": "xxx",
    "Forge_server_1.16.1": "xxx",
    "Forge_server_1.15.2": "xxx",
    "Forge_server_1.15.1": "xxx",
    "Forge_server_1.15": "xxx",
    "Forge_server_1.14.4": "xxx",
    "Forge_server_1.14.3": "xxx",
    "Forge_server_1.14.2": "xxx",
    "Forge_server_1.13.2": "xxx",
    "Forge_server_1.12.2": "xxx",
    "Forge_server_1.12.1": "xxx",
    "Forge_server_1.12": "xxx",
    "Forge_server_1.11.2": "xxx",
    "Forge_server_1.10.2": "xxx",
    "Forge_server_1.9.4": "xxx",
    "Forge_server_1.8.8": "xxx",
    "Fabric_server_1.20.4": "xxx",
    "Fabric_server_1.20.3": "xxx",
    "Fabric_server_1.20.2": "xxx",
    "Fabric_server_1.20.1": "xxx",
    "Fabric_server_1.20": "xxx",
    "Fabric_server_1.19.4": "xxx",
    "Fabric_server_1.19.3": "xxx",
    "Fabric_server_1.19.2": "xxx",
    "Fabric_server_1.19.1": "xxx",
    "Fabric_server_1.19": "xxx",
    "Fabric_server_1.18.2": "xxx",
    "Fabric_server_1.18.1": "xxx",
    "Fabric_server_1.18": "xxx",
    "Fabric_server_1.17.1": "xxx",
    "Fabric_server_1.17": "xxx",
    "Fabric_server_1.16.5": "xxx",
    "Fabric_server_1.16.4": "xxx",
    "Fabric_server_1.16.3": "xxx",
    "Fabric_server_1.16.2": "xxx",
    "Fabric_server_1.16.1": "xxx",
    "Fabric_server_1.15.2": "xxx",
    "Fabric_server_1.15.1": "xxx",
    "Fabric_server_1.15": "xxx",
    "Fabric_server_1.14.4": "xxx",
    "Fabric_server_1.14.3": "xxx",
    "Fabric_server_1.14.2": "xxx",
    "Fabric_server_1.13.2": "xxx",
    "Fabric_server_1.12.2": "xxx",
    "Fabric_server_1.12.1": "xxx",
    "Fabric_server_1.12": "xxx",
    "Fabric_server_1.11.2": "xxx",
    "Fabric_server_1.10.2": "xxx",
    "Fabric_server_1.9.4": "xxx",
    "Fabric_server_1.8.8": "xxx",
    "Cat_server_1.18.2": "xxx",
    "Cat_server_1.16.5": "xxx",
    "Cat_server_1.12.2": "xxx",
    "Mohist_server_1.20.2": "xxx",
    "Mohist_server_1.20.1": "xxx",
    "Mohist_server_1.20": "xxx",
    "Mohist_server_1.19.4": "xxx",
    "Mohist_server_1.19.2": "xxx",
    "Mohist_server_1.18.2": "xxx",
    "Mohist_server_1.16.5": "xxx",
    "Mohist_server_1.12.2": "xxx",
    "Mohist_server_1.7.10": "xxx",
    "Banner_server_1.20.1": "xxx",
    "Banner_server_1.20": "xxx",
    "Banner_server_1.19.4": "xxx",
    "Craftbukkit_server_1.20.4": "xxx",
    "Craftbukkit_server_1.20.2": "xxx",
    "Craftbukkit_server_1.20.1": "xxx",
    "Craftbukkit_server_1.19.4": "xxx",
    "Craftbukkit_server_1.19.3": "xxx",
    "Craftbukkit_server_1.19.2": "xxx",
    "Craftbukkit_server_1.19.1": "xxx",
    "Craftbukkit_server_1.19": "xxx",
    "Craftbukkit_server_1.18.2": "xxx",
    "Craftbukkit_server_1.18.1": "xxx",
    "Craftbukkit_server_1.18": "xxx",
    "Craftbukkit_server_1.17.1": "xxx",
    "Craftbukkit_server_1.17": "xxx",
    "Craftbukkit_server_1.16.5": "xxx",
    "Craftbukkit_server_1.16.4": "xxx",
    "Craftbukkit_server_1.16.3": "xxx",
    "Craftbukkit_server_1.16.2": "xxx",
    "Craftbukkit_server_1.16.1": "xxx",
    "Craftbukkit_server_1.15.2": "xxx",
    "Craftbukkit_server_1.15.1": "xxx",
    "Craftbukkit_server_1.15": "xxx",
    "Craftbukkit_server_1.14.4": "xxx",
    "Craftbukkit_server_1.14.3": "xxx",
    "Craftbukkit_server_1.14.2": "xxx",
    "Craftbukkit_server_1.13.2": "xxx",
    "Craftbukkit_server_1.12.2": "xxx",
    "Craftbukkit_server_1.12.1": "xxx",
    "Craftbukkit_server_1.12": "xxx",
    "Craftbukkit_server_1.11.2": "xxx",
    "Craftbukkit_server_1.11.1": "xxx",
    "Craftbukkit_server_1.11": "xxx",
    "Craftbukkit_server_1.10.2": "xxx",
    "Craftbukkit_server_1.10": "xxx",
    "Craftbukkit_server_1.9.4": "xxx",
    "Craftbukkit_server_1.9.2": "xxx",
    "Craftbukkit_server_1.9": "xxx",
    "Craftbukkit_server_1.8.8": "xxx",
    "Craftbukkit_server_1.8.7": "xxx",
    "Craftbukkit_server_1.8.6": "xxx",
    "Craftbukkit_server_1.8.5": "xxx",
    "Craftbukkit_server_1.8.4": "xxx",
    "Craftbukkit_server_1.8.3": "xxx",
    "Craftbukkit_server_1.8": "xxx",
    "Craftbukkit_server_1.7.10": "xxx",
    "Craftbukkit_server_1.7.9": "xxx",
    "Craftbukkit_server_1.7.8": "xxx",
    "Craftbukkit_server_1.7.5": "xxx",
    "Craftbukkit_server_1.7.2": "xxx",
    "Craftbukkit_server_1.6.4": "xxx",
    "Craftbukkit_server_1.6.2": "xxx",
    "Craftbukkit_server_1.5.2": "xxx",
    "Craftbukkit_server_1.5.1": "xxx",
    "Craftbukkit_server_1.4.7": "xxx",
    "Craftbukkit_server_1.4.6": "xxx",
    "Spigot_server_1.20.4": "xxx",
    "Spigot_server_1.20.2": "xxx",
    "Spigot_server_1.20.1": "xxx",
    "Spigot_server_1.19.4": "xxx",
    "Spigot_server_1.19.3": "xxx",
    "Spigot_server_1.19.2": "xxx",
    "Spigot_server_1.19.1": "xxx",
    "Spigot_server_1.19": "xxx",
    "Spigot_server_1.18.2": "xxx",
    "Spigot_server_1.18.1": "xxx",
    "Spigot_server_1.18": "xxx",
    "Spigot_server_1.17.1": "xxx",
    "Spigot_server_1.17": "xxx",
    "Spigot_server_1.16.5": "xxx",
    "Spigot_server_1.16.4": "xxx",
    "Spigot_server_1.16.3": "xxx",
    "Spigot_server_1.16.2": "xxx",
    "Spigot_server_1.16.1": "xxx",
    "Spigot_server_1.15.2": "xxx",
    "Spigot_server_1.15.1": "xxx",
    "Spigot_server_1.15": "xxx",
    "Spigot_server_1.14.4": "xxx",
    "Spigot_server_1.14.3": "xxx",
    "Spigot_server_1.14.2": "xxx",
    "Spigot_server_1.13.2": "xxx",
    "Spigot_server_1.12.2": "xxx",
    "Spigot_server_1.12.1": "xxx",
    "Spigot_server_1.12": "xxx",
    "Spigot_server_1.11.2": "xxx",
    "Spigot_server_1.10.2": "xxx",
    "Spigot_server_1.9.4": "xxx",
    "Spigot_server_1.8.8": "xxx",
    "Paper_server_1.20.4": "xxx",
    "Paper_server_1.20.2": "xxx",
    "Paper_server_1.20.1": "xxx",
    "Paper_server_1.20": "xxx",
    "Paper_server_1.19.4": "xxx",
    "Paper_server_1.19.3": "xxx",
    "Paper_server_1.19.2": "xxx",
    "Paper_server_1.19.1": "xxx",
    "Paper_server_1.19": "xxx",
    "Paper_server_1.18.2": "xxx",
    "Paper_server_1.18.1": "xxx",
    "Paper_server_1.18": "xxx",
    "Paper_server_1.17.1": "xxx",
    "Paper_server_1.17": "xxx",
    "Paper_server_1.16.5": "xxx",
    "Paper_server_1.16.4": "xxx",
    "Paper_server_1.16.3": "xxx",
    "Paper_server_1.16.2": "xxx",
    "Paper_server_1.16.1": "xxx",
    "Paper_server_1.15.2": "xxx",
    "Paper_server_1.15.1": "xxx",
    "Paper_server_1.15": "xxx",
    "Paper_server_1.14.4": "xxx",
    "Paper_server_1.14.3": "xxx",
    "Paper_server_1.14.2": "xxx",
    "Paper_server_1.13.2": "xxx",
    "Paper_server_1.12.2": "xxx",
    "Paper_server_1.12.1": "xxx",
    "Paper_server_1.12": "xxx",
    "Paper_server_1.11.2": "xxx",
    "Paper_server_1.10.2": "xxx",
    "Paper_server_1.9.4": "xxx",
    "Paper_server_1.8.8": "xxx",
    "Waterfall_server_1.20": "xxx",
    "Waterfall_server_1.19": "xxx",
    "Waterfall_server_1.18": "xxx",
    "Waterfall_server_1.17": "xxx",
    "Waterfall_server_1.16": "xxx",
    "Waterfall_server_1.15": "xxx",
    "Waterfall_server_1.14": "xxx",
    "Waterfall_server_1.13": "xxx",
    "Waterfall_server_1.12": "xxx",
    "Waterfall_server_1.11": "xxx",
    "java-lite-v1": java_lite_v1_url,
    "java-lite-v2": java_lite_v2_url,
    "java-lite-v3": java_lite_v3_url
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
            print(f"已下载: {destination}")

            # 如果文件是ZIP格式，解压它
            if destination.endswith('.zip'):
                with zipfile.ZipFile(destination, 'r') as zip_ref:
                    zip_ref.extractall(download_directory)
                print(f"已解压: {destination}")

            # 如果文件是TAR.GZ格式，解压它
            elif destination.endswith('.tar.gz'):
                with tarfile.open(destination, 'r:gz') as tar_ref:
                    tar_ref.extractall(download_directory)
                print(f"已解压: {destination}")

            # 删除原始压缩文件
            if destination.endswith('.zip') or destination.endswith('.tar.gz'):
                os.remove(destination)
                print(f"已删除压缩文件: {destination}")

            # 查找解压后的文件夹并重命名为 'java'
            extracted_folders = [f.name for f in os.scandir(download_directory) if f.is_dir()]
            for folder_name in extracted_folders:
                if folder_name.startswith("jdk"):
                    folder_path = os.path.join(download_directory, folder_name)
                    java_path = os.path.join(download_directory, 'java')
                    if os.path.exists(java_path):
                        shutil.rmtree(java_path)
                    shutil.move(folder_path, java_path)
                    print(f"已重命名 '{folder_name}' 为 'java'")
                    break

        else:
            print(f"下载失败: {url}")

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
    exit_program()


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
        "1.20.4": ["Minecraft_server_1.20.4", "java-lite-v1"],
        "1.20.3": ["Minecraft_server_1.20.3", "java-lite-v1"],
        "1.20.2": ["Minecraft_server_1.20.2", "java-lite-v1"],
        "1.20.1": ["Minecraft_server_1.20.1", "java-lite-v1"],
        "1.20": ["Minecraft_server_1.20", "java-lite-v1"],
        "1.19.4": ["Minecraft_server_1.19.4", "java-lite-v1"],
        "1.19.3": ["Minecraft_server_1.19.3", "java-lite-v1"],
        "1.19.2": ["Minecraft_server_1.19.2", "java-lite-v1"],
        "1.19.1": ["Minecraft_server_1.19.1", "java-lite-v1"],
        "1.19": ["Minecraft_server_1.19", "java-lite-v1"],
        "1.18.2": ["Minecraft_server_1.18.2", "java-lite-v1"],
        "1.18.1": ["Minecraft_server_1.18.1", "java-lite-v1"],
        "1.18": ["Minecraft_server_1.18", "java-lite-v1"],
        "1.17.1": ["Minecraft_server_1.17.1", "java-lite-v2"],
        "1.17": ["Minecraft_server_1.17", "java-lite-v2"],
        "1.16.5": ["Minecraft_server_1.16.5", "java-lite-v3"],
        "1.16.4": ["Minecraft_server_1.16.4", "java-lite-v3"],
        "1.16.3": ["Minecraft_server_1.16.3", "java-lite-v3"],
        "1.16.2": ["Minecraft_server_1.16.2", "java-lite-v3"],
        "1.16.1": ["Minecraft_server_1.16.1", "java-lite-v3"],
        "1.16": ["Minecraft_server_1.16", "java-lite-v3"],
        "1.15.2": ["Minecraft_server_1.15.2", "java-lite-v3"],
        "1.15.1": ["Minecraft_server_1.15.1", "java-lite-v3"],
        "1.15": ["Minecraft_server_1.15", "java-lite-v3"],
        "1.14.4": ["Minecraft_server_1.14.4", "java-lite-v3"],
        "1.14.3": ["Minecraft_server_1.14.3", "java-lite-v3"],
        "1.14.2": ["Minecraft_server_1.14.2", "java-lite-v3"],
        "1.13.2": ["Minecraft_server_1.13.2", "java-lite-v3"],
        "1.12.2": ["Minecraft_server_1.12.2", "java-lite-v3"],
        "1.12.1": ["Minecraft_server_1.12.1", "java-lite-v3"],
        "1.12": ["Minecraft_server_1.12", "java-lite-v3"],
        "1.11.2": ["Minecraft_server_1.11.2", "java-lite-v3"],
        "1.10.2": ["Minecraft_server_1.10.2", "java-lite-v3"],
        "1.9.4": ["Minecraft_server_1.9.4", "java-lite-v3"],
        "1.8.8": ["Minecraft_server_1.8.8", "java-lite-v3"]
    },
    "Forge_server": {
        "1.20.4": ["Forge_server_1.20.4", "java-lite-v1"],
        "1.20.3": ["Forge_server_1.20.3", "java-lite-1"],
        "1.20.2": ["Forge_server_1.20.2", "java-lite-1"],
        "1.20.1": ["Forge_server_1.20.1", "java-lite-1"],
        "1.20": ["Forge_server_1.20", "java-lite-v1"],
        "1.19.4": ["Forge_server_1.19.4", "java-lite-v1"],
        "1.19.3": ["Forge_server_1.19.3", "java-lite-v1"],
        "1.19.2": ["Forge_server_1.19.2", "java-lite-v1"],
        "1.19.1": ["Forge_server_1.19.1", "java-lite-v1"],
        "1.19": ["Forge_server_1.19", "java-lite-v1"],
        "1.18.2": ["Forge_server_1.18.2", "java-lite-v1"],
        "1.18.1": ["Forge_server_1.18.1", "java-lite-v1"],
        "1.18": ["Forge_server_1.18", "java-lite-v1"],
        "1.17.1": ["Forge_server_1.17.1", "java-lite-v2"],
        "1.16.5": ["Forge_server_1.16.5", "java-lite-v3"],
        "1.16.4": ["Forge_server_1.16.4", "java-lite-v3"],
        "1.16.3": ["Forge_server_1.16.3", "java-lite-v3"],
        "1.16.2": ["Forge_server_1.16.2", "java-lite-v3"],
        "1.16.1": ["Forge_server_1.16.1", "java-lite-v3"],
        "1.15.2": ["Forge_server_1.15.2", "java-lite-v3"],
        "1.15.1": ["Forge_server_1.15.1", "java-lite-v3"],
        "1.15": ["Forge_server_1.15", "java-lite-v3"],
        "1.14.4": ["Forge_server_1.14.4", "java-lite-v3"],
        "1.14.3": ["Forge_server_1.14.3", "java-lite-v3"],
        "1.14.2": ["Forge_server_1.14.2", "java-lite-v3"],
        "1.13.2": ["Forge_server_1.13.2", "java-lite-v3"],
        "1.12.2": ["Forge_server_1.12.2", "java-lite-v3"],
        "1.12.1": ["Forge_server_1.12.1", "java-lite-v3"],
        "1.12": ["Forge_server_1.12", "java-lite-v3"],
        "1.11.2": ["Forge_server_1.11.2", "java-lite-v3"],
        "1.10.2": ["Forge_server_1.10.2", "java-lite-v3"],
        "1.9.4": ["Forge_server_1.9.4", "java-lite-v3"],
        "1.8.8": ["Forge_server_1.8.8", "java-lite-v3"]
    },
    "Fabric_server": {
        "1.20.4": ["Fabric_server_1.20.4", "java-lite-v1"],
        "1.20.3": ["Fabric_server_1.20.3", "java-lite-v1"],
        "1.20.2": ["Fabric_server_1.20.2", "java-lite-v1"],
        "1.20.1": ["Fabric_server_1.20.1", "java-lite-v1"],
        "1.20": ["Fabric_server_1.20", "java-lite-v1"],
        "1.19.4": ["Fabric_server_1.19.4", "java-lite-v1"],
        "1.19.3": ["Fabric_server_1.19.3", "java-lite-v1"],
        "1.19.2": ["Fabric_server_1.19.2", "java-lite-v1"],
        "1.19.1": ["Fabric_server_1.19.1", "java-lite-v1"],
        "1.19": ["Fabric_server_1.19", "java-lite-v1"],
        "1.18.2": ["Fabric_server_1.18.2", "java-lite-v1"],
        "1.18.1": ["Fabric_server_1.18.1", "java-lite-v1"],
        "1.18": ["Fabric_server_1.18", "java-lite-v1"],
        "1.17.1": ["Fabric_server_1.17.1", "java-lite-v2"],
        "1.17": ["Fabric_server_1.17", "java-lite-v2"],
        "1.16.5": ["Fabric_server_1.16.5", "java-lite-v3"],
        "1.16.4": ["Fabric_server_1.16.4", "java-lite-v3"],
        "1.16.3": ["Fabric_server_1.16.3", "java-lite-v3"],
        "1.16.2": ["Fabric_server_1.16.2", "java-lite-v3"],
        "1.16.1": ["Fabric_server_1.16.1", "java-lite-v3"],
        "1.15.2": ["Fabric_server_1.15.2", "java-lite-v3"],
        "1.15.1": ["Fabric_server_1.15.1", "java-lite-v3"],
        "1.15": ["Fabric_server_1.15", "java-lite-v3"],
        "1.14.4": ["Fabric_server_1.14.4", "java-lite-v3"],
        "1.14.3": ["Fabric_server_1.14.3", "java-lite-v3"],
        "1.14.2": ["Fabric_server_1.14.2", "java-lite-v3"],
        "1.13.2": ["Fabric_server_1.13.2", "java-lite-v3"],
        "1.12.2": ["Fabric_server_1.12.2", "java-lite-v3"],
        "1.12.1": ["Fabric_server_1.12.1", "java-lite-v3"],
        "1.12": ["Fabric_server_1.12", "java-lite-v3"],
        "1.11.2": ["Fabric_server_1.11.2", "java-lite-v3"],
        "1.10.2": ["Fabric_server_1.10.2", "java-lite-v3"],
        "1.9.4": ["Fabric_server_1.9.4", "java-lite-v3"],
        "1.8.8": ["Fabric_server_1.8.8", "java-lite-v3"]
    },
    "Cat_server": {
        "1.18.2": ["Cat_server_1.18.2", "java-lite-v1"],
        "1.16.5": ["Cat_server_1.16.5", "java-lite-v3"],
        "1.12.2": ["Cat_server_1.12.2", "java-lite-v3"]
    },
    "Mohist_server": {
        "1.20.2": ["Mohist_server_1.20.2", "java-lite-v1"],
        "1.20.1": ["Mohist_server_1.20.1", "java-lite-v1"],
        "1.20": ["Mohist_server_1.20", "java-lite-v1"],
        "1.19.4": ["Mohist_server_1.19.4", "java-lite-v1"],
        "1.19.2": ["Mohist_server_1.19.2", "java-lite-v1"],
        "1.18.2": ["Mohist_server_1.18.2", "java-lite-v1"],
        "1.16.5": ["Mohist_server_1.16.5", "java-lite-v3"],
        "1.12.2": ["Mohist_server_1.12.2", "java-lite-v3"],
        "1.7.10": ["Mohist_server_1.7.10", "java-lite-v3"]
    },
    "Banner_server": {
        "1.20.1": ["Banner_server_1.20.1", "java-lite-v1"],
        "1.20": ["Banner_server_1.20", "java-lite-v1"],
        "1.19.4": ["Banner_server_1.19.4", "java-lite-v1"],
    },
    "Craftbukkit_server": {
        "1.20.4": ["Craftbukkit_server_1.20.4", "java-lite-v1"],
        "1.20.2": ["Craftbukkit_server_1.20.2", "java-lite-v1"],
        "1.20.1": ["Craftbukkit_server_1.20.1", "java-lite-v1"],
        "1.19.4": ["Craftbukkit_server_1.19.4", "java-lite-v1"],
        "1.19.3": ["Craftbukkit_server_1.19.3", "java-lite-v1"],
        "1.19.2": ["Craftbukkit_server_1.19.2", "java-lite-v1"],
        "1.19.1": ["Craftbukkit_server_1.19.1", "java-lite-v1"],
        "1.19": ["Craftbukkit_server_1.19", "java-lite-v1"],
        "1.18.2": ["Craftbukkit_server_1.18.2", "java-lite-v1"],
        "1.18.1": ["Craftbukkit_server_1.18.1", "java-lite-v1"],
        "1.18": ["Craftbukkit_server_1.18", "java-lite-v1"],
        "1.17.1": ["Craftbukkit_server_1.17.1", "java-lite-v2"],
        "1.17": ["Craftbukkit_server_1.17", "java-lite-v2"],
        "1.16.5": ["Craftbukkit_server_1.16.5", "java-lite-v3"],
        "1.16.4": ["Craftbukkit_server_1.16.4", "java-lite-v3"],
        "1.16.3": ["Craftbukkit_server_1.16.3", "java-lite-v3"],
        "1.16.2": ["Craftbukkit_server_1.16.2", "java-lite-v3"],
        "1.16.1": ["Craftbukkit_server_1.16.1", "java-lite-v3"],
        "1.15.2": ["Craftbukkit_server_1.15.2", "java-lite-v3"],
        "1.15.1": ["Craftbukkit_server_1.15.1", "java-lite-v3"],
        "1.15": ["Craftbukkit_server_1.15", "java-lite-v3"],
        "1.14.4": ["Craftbukkit_server_1.14.4", "java-lite-v3"],
        "1.14.3": ["Craftbukkit_server_1.14.3", "java-lite-v3"],
        "1.14.2": ["Craftbukkit_server_1.14.2", "java-lite-v3"],
        "1.13.2": ["Craftbukkit_server_1.13.2", "java-lite-v3"],
        "1.12.2": ["Craftbukkit_server_1.12.2", "java-lite-v3"],
        "1.12.1": ["Craftbukkit_server_1.12.1", "java-lite-v3"],
        "1.12": ["Craftbukkit_server_1.12", "java-lite-v3"],
        "1.11.2": ["Craftbukkit_server_1.11.2", "java-lite-v3"],
        "1.11.1": ["Craftbukkit_server_1.11.1", "java-lite-v3"],
        "1.11": ["Craftbukkit_server_1.11", "java-lite-v3"],
        "1.10.2": ["Craftbukkit_server_1.10.2", "java-lite-v3"],
        "1.10": ["Craftbukkit_server_1.10", "java-lite-v3"],
        "1.9.4": ["Craftbukkit_server_1.9.4", "java-lite-v3"],
        "1.9.2": ["Craftbukkit_server_1.9.2", "java-lite-v3"],
        "1.9": ["Craftbukkit_server_1.9", "java-lite-v3"],
        "1.8.8": ["Craftbukkit_server_1.8.8", "java-lite-v3"],
        "1.8.7": ["Craftbukkit_server_1.8.7", "java-lite-v3"],
        "1.8.6": ["Craftbukkit_server_1.8.6", "java-lite-v3"],
        "1.8.5": ["Craftbukkit_server_1.8.5", "java-lite-v3"],
        "1.8.4": ["Craftbukkit_server_1.8.4", "java-lite-v3"],
        "1.8.3": ["Craftbukkit_server_1.8.3", "java-lite-v3"],
        "1.8": ["Craftbukkit_server_1.8", "java-lite-v3"],
        "1.7.10": ["Craftbukkit_server_1.7.10", "java-lite-v3"],
        "1.7.9": ["Craftbukkit_server_1.7.9", "java-lite-v3"],
        "1.7.8": ["Craftbukkit_server_1.7.8", "java-lite-v3"],
        "1.7.5": ["Craftbukkit_server_1.7.5", "java-lite-v3"],
        "1.7.2": ["Craftbukkit_server_1.7.2", "java-lite-v3"],
        "1.6.4": ["Craftbukkit_server_1.6.4", "java-lite-v3"],
        "1.6.2": ["Craftbukkit_server_1.6.2", "java-lite-v3"],
        "1.5.2": ["Craftbukkit_server_1.5.2", "java-lite-v3"],
        "1.5.1": ["Craftbukkit_server_1.5.1", "java-lite-v3"],
        "1.4.7": ["Craftbukkit_server_1.4.7", "java-lite-v3"],
        "1.4.6": ["Craftbukkit_server_1.4.6", "java-lite-v3"]
    },
    "Spigot_server": {
        "1.20.4": ["Spigot_server_1.20.4", "java-lite-v1"],
        "1.20.2": ["Spigot_server_1.20.2", "java-lite-v1"],
        "1.20.1": ["Spigot_server_1.20.1", "java-lite-v1"],
        "1.19.4": ["Spigot_server_1.19.4", "java-lite-v1"],
        "1.19.3": ["Spigot_server_1.19.3", "java-lite-v1"],
        "1.19.2": ["Spigot_server_1.19.2", "java-lite-v1"],
        "1.19.1": ["Spigot_server_1.19.1", "java-lite-v1"],
        "1.19": ["Spigot_server_1.19", "java-lite-v1"],
        "1.18.2": ["Spigot_server_1.18.2", "java-lite-v1"],
        "1.18.1": ["Spigot_server_1.18.1", "java-lite-v1"],
        "1.18": ["Spigot_server_1.18", "java-lite-v1"],
        "1.17.1": ["Spigot_server_1.17.1", "java-lite-v2"],
        "1.17": ["Spigot_server_1.17", "java-lite-v2"],
        "1.16.5": ["Spigot_server_1.16.5", "java-lite-v3"],
        "1.16.4": ["Spigot_server_1.16.4", "java-lite-v3"],
        "1.16.3": ["Spigot_server_1.16.3", "java-lite-v3"],
        "1.16.2": ["Spigot_server_1.16.2", "java-lite-v3"],
        "1.16.1": ["Spigot_server_1.16.1", "java-lite-v3"],
        "1.15.2": ["Spigot_server_1.15.2", "java-lite-v3"],
        "1.15.1": ["Spigot_server_1.15.1", "java-lite-v3"],
        "1.15": ["Spigot_server_1.15", "java-lite-v3"],
        "1.14.4": ["Spigot_server_1.14.4", "java-lite-v3"],
        "1.14.3": ["Spigot_server_1.14.3", "java-lite-v3"],
        "1.14.2": ["Spigot_server_1.14.2", "java-lite-v3"],
        "1.13.2": ["Spigot_server_1.13.2", "java-lite-v3"],
        "1.12.2": ["Spigot_server_1.12.2", "java-lite-v3"],
        "1.12.1": ["Spigot_server_1.12.1", "java-lite-v3"],
        "1.12": ["Spigot_server_1.12", "java-lite-v3"],
        "1.11.2": ["Spigot_server_1.11.2", "java-lite-v3"],
        "1.10.2": ["Spigot_server_1.10.2", "java-lite-v3"],
        "1.9.4": ["Spigot_server_1.9.4", "java-lite-v3"],
        "1.8.8": ["Spigot_server_1.8.8", "java-lite-v3"]
    },
    "Paper_server": {
        "1.20.4": ["Paper_server_1.20.4", "java-lite-v1"],
        "1.20.2": ["Paper_server_1.20.2", "java-lite-v1"],
        "1.20.1": ["Paper_server_1.20.1", "java-lite-v1"],
        "1.20": ["Paper_server_1.20", "java-lite-v1"],
        "1.19.4": ["Paper_server_1.19.4", "java-lite-v1"],
        "1.19.3": ["Paper_server_1.19.3", "java-lite-v1"],
        "1.19.2": ["Paper_server_1.19.2", "java-lite-v1"],
        "1.19.1": ["Paper_server_1.19.1", "java-lite-v1"],
        "1.19": ["Paper_server_1.19", "java-lite-v1"],
        "1.18.2": ["Paper_server_1.18.2", "java-lite-v1"],
        "1.18.1": ["Paper_server_1.18.1", "java-lite-v1"],
        "1.18": ["Paper_server_1.18", "java-lite-v1"],
        "1.17.1": ["Paper_server_1.17.1", "java-lite-v2"],
        "1.17": ["Paper_server_1.17", "java-lite-v2"],
        "1.16.5": ["Paper_server_1.16.5", "java-lite-v3"],
        "1.16.4": ["Paper_server_1.16.4", "java-lite-v3"],
        "1.16.3": ["Paper_server_1.16.3", "java-lite-v3"],
        "1.16.2": ["Paper_server_1.16.2", "java-lite-v3"],
        "1.16.1": ["Paper_server_1.16.1", "java-lite-v3"],
        "1.15.2": ["Paper_server_1.15.2", "java-lite-v3"],
        "1.15.1": ["Paper_server_1.15.1", "java-lite-v3"],
        "1.15": ["Paper_server_1.15", "java-lite-v3"],
        "1.14.4": ["Paper_server_1.14.4", "java-lite-v3"],
        "1.14.3": ["Paper_server_1.14.3", "java-lite-v3"],
        "1.14.2": ["Paper_server_1.14.2", "java-lite-v3"],
        "1.13.2": ["Paper_server_1.13.2", "java-lite-v3"],
        "1.12.2": ["Paper_server_1.12.2", "java-lite-v3"],
        "1.12.1": ["Paper_server_1.12.1", "java-lite-v3"],
        "1.12": ["Paper_server_1.12", "java-lite-v3"],
        "1.11.2": ["Paper_server_1.11.2", "java-lite-v3"],
        "1.10.2": ["Paper_server_1.10.2", "java-lite-v3"],
        "1.9.4": ["Paper_server_1.9.4", "java-lite-v3"],
        "1.8.8": ["Paper_server_1.8.8", "java-lite-v3"]
    },
    "Waterfall_server": {
        "1.20": ["Paper_server_1.20", "java-lite-v1"],
        "1.19": ["Paper_server_1.19", "java-lite-v1"],
        "1.18": ["Paper_server_1.18", "java-lite-v1"],
        "1.17": ["Paper_server_1.17", "java-lite-v2"],
        "1.16": ["Paper_server_1.16", "java-lite-v3"],
        "1.15": ["Paper_server_1.15", "java-lite-v3"],
        "1.14": ["Paper_server_1.14", "java-lite-v3"],
        "1.13": ["Paper_server_1.13", "java-lite-v3"],
        "1.12": ["Paper_server_1.12", "java-lite-v3"],
        "1.11": ["Paper_server_1.11", "java-lite-v3"],
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

        user_input = input("\n输入a切换上一页，输入b切换下一页，输入q返回上一菜单，选择内容编号执行自定义函数：")
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
        "10": "Waterfall_server",
        # ... 其他服务器类型 ...
    }
    while True:
        user_input = input("---------主菜单---------\n1. Minecraft server\n2. Forge server\n3. Fabric_server\n4. "
                           "Cat_server\n5. Mohist_server\n6. Banner_server\n7. Craftbukkit_server\n8. "
                           "Spigot_server\n9. Paper_server\n10. Waterfall_server"
                           "\n-----------------------\n输入数字选择,输入q退出:")

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
