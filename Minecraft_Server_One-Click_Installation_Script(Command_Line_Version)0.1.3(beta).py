import os
from tqdm import tqdm
import zipfile
import urllib.request
import fnmatch
import requests

def statement():
    print("免责声明：")
    print("1. 本脚本一切均来自官方源转载，非商用")
    print("2. 本脚本只负责基础包装服务器，服务器除特殊版本均可正常使用。添加模组后无法运行不归本脚本负责")
    print("3. 本脚本为公益脚本，严禁倒卖商业")
    print("4. 无论服务器做和用途，本人概不负责")
    print("5. 本脚本仅由个人开发，请自行甄别作者")
    print("6. 反馈邮箱: dyx45d@163.com 作者QQ: 3636695284")
    input("按下任意键继续...")
    os.system('cls')

def 基础教程():
    print("服务器基础教程")
    print("1. 本教程提供打包服务器,自带Java环境,启动器请自行配置选择。")
    print("2. 本服务器默认关闭正版验证，无需担心账号认证问题。")
    print("3. 双击run.bat即可快速启动服务器,方便简洁。")
    print("4. 如果服务器在本地运行,默认IP为127.0.0.1,端口为25565。")
    print("5. 将模组放置在服务器根目录的mods文件夹中,确保正确加载所需的模组。")
    print("6. 将插件放置在服务器根目录的plugins文件夹中,保证插件正常运行。")
    print("7. 内网穿透的配置示例（以本地部署，未进行修改为例）：")
    print("8. 内网穿透IP输入127.0.0.1,表示将本地IP映射为公网IP。")
    print("9. 内部端口输入25565,表示映射的是Minecraft服务器的端口。")
    print("10. 外部IP和端口可任意选择,根据需要进行设置。")
    print("11. 连接服务器时，可以使用 外部IP:外部端口 进行连接。（例如 xxx.xxx.xxx.xxx:外部端口，冒号一定要加）")
    print("12. 如果在使用过程中遇到任何问题，请联系反馈给作者,QQ:3636695284,邮箱,dyx45d@163.com。")
    print("13. 如果下载文件时遇到闪退情况，请考虑检查网络连接是否正常，可能是网络问题而非脚本本身的问题。")
    print("14. server文件编辑教程下载https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/Advanced_server_editing_tutorial/server.docx")
    input("按下任意键继续...")
    os.system('cls')

def 核心作用():
    print("核心作用")
    print("1. forge:  仅仅支持forge引擎api衍生类模组(推荐低版本使用,如1.18以下)")
    print("2. fabric:  仅仅支持fabric引擎api衍生类模组(推荐高版本使用,如1.18及以上)")
    print("3. cat-server:  支持添加加forge引擎api衍生类模组和Spigot和Bukkit的API衍生类插件")
    print("4. MohistMC:  支持添加加forge引擎api衍生类模组和Spigot和Bukkit的API衍生类插件")
    print("5. Bukkit:  支持添加Bukkit的API衍生类插件")
    print("6. Spigot:  支持添加Spigot的API衍生类插件")
    print("7. Paper:  基于Spigot的Minecraft游戏服务器,可以在大大提高性能并提供更高级的功能和API。")
    input("按下任意键继续...")
    os.system('cls')

def exit():
    exit


###############################################
#文件下载
###############################################
class FileDownloader:
    def __init__(self):
        self.total_progress_bar = None
        self.file_progress_bar = None

    def download_file(self, url, output_path):
        r = requests.get(url, stream=True)
        file_size = int(r.headers.get('content-length', 0))

        self.total_progress_bar = tqdm(total=file_size, unit='B', unit_scale=True)
        self.file_progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, bar_format='{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt}')

        with open(output_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    self.total_progress_bar.update(len(chunk))
                    self.file_progress_bar.update(len(chunk))
                    f.write(chunk)

        self.file_progress_bar.close()
        self.total_progress_bar.close()

    def download_files(self, file_urls, output_dir):
        os.makedirs(output_dir, exist_ok=True)
        for url in file_urls:
            file_name = url.split('/')[-1]
            file_path = os.path.join(output_dir, file_name)
            self.download_file(url, file_path)

# Example usage
if __name__ == "__main__":
    downloader = FileDownloader()


def 压缩文件解压(zip_files, destination_folders):
    # 确保zip_files和destination_folders列表长度相等
    if len(zip_files) != len(destination_folders):
        print("错误:ZIP 文件和目标文件夹的数量应相同。")
        return

    # 循环处理每个ZIP文件
    for i in range(len(zip_files)):
        zip_file_path = zip_files[i]
        extract_folder = destination_folders[i]

        # 创建目标文件夹路径
        os.makedirs(extract_folder, exist_ok=True)

        # 解压缩ZIP文件到目标文件夹
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

        print("正在解压缩 {} to {}".format(zip_file_path, extract_folder))
    

def 压缩文件删除(directory_path):
    for file in os.listdir(directory_path):
        if fnmatch.fnmatch(file, '*.zip'):
            file_path = os.path.join(directory_path, file)
            os.remove(file_path)
            print("Deleted: {}".format(file_path))




###############################################
#forge版本文件下载
###############################################

def forge版本1_20_1():
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.20.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.20.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_20():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.20.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.20.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_19_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.19.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.19.4.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_19_3():
    print ("开始下载")
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.19.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.19.3.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_19_2():
    print ("开始下载")
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.19.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.19.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_19_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.19.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.19.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_19():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.19.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.19.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_18_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.18.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.18.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_18_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.18.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.18.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_18():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.18.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.18.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_17_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.17.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.17.1.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_16_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.16.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.16.5.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_16_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.16.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.16.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_16_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.16.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.16.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_16_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.16.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.16.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_16_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.16.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.16.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_15_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.15.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.15.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_15_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.15.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.15.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_15():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.15.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.15.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_14_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.14.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.14.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_14_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.14.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.14.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_14_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.14.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.14.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_13_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.13.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.13.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_12_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.12.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.12.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_12_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.12.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.12.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_12():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.12.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.12.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_11_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.11.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.12.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_11():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.11zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.11.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_10():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.10.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.10.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_10_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.10.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.10.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_9_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.9.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.9.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_9():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.9.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.9.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()


def forge版本1_8_9():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.8.9.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.8.9.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_8_8():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.8.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.8.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def forge版本1_8():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/forge/forge-1.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/forge-1.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

###############################################
#forge系列核心版本选择
###############################################

def forge版本系列选择1_20():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_20_1()
    elif user_input == "2":
        forge版本1_20()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_19():            
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_19_4()
    elif user_input == "2":
        forge版本1_19_3()
    elif user_input == "3":
        forge版本1_19_2()
    elif user_input == "4":
        forge版本1_19_1()
    elif user_input == "5":
        forge版本1_19()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_18():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_18_2()
    elif user_input == "2":
        forge版本1_18_1()
    elif user_input == "3":
        forge版本1_18()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_17():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_17_1()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_16():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_16_5()
    elif user_input == "2":
        forge版本1_16_4()
    elif user_input == "3":
        forge版本1_16_3()
    elif user_input == "4":
        forge版本1_16_2()
    elif user_input == "5":
        forge版本1_16_1()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_15():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_15_2()
    elif user_input == "2":
        forge版本1_15_1()
    elif user_input == "2":
        forge版本1_15()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_14():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_14_4()
    elif user_input == "2":
        forge版本1_14_3()
    elif user_input == "3":
        forge版本1_14_2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_13():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_13_2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_12():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_12_2()
    elif user_input == "2":
        forge版本1_12_1()
    elif user_input == "3":
        forge版本1_12()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_11():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_11_2()
    elif user_input == "2":
        forge版本1_11()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_10():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_10_2()
    elif user_input == "2":
        forge版本1_10()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_9():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_9_4()
    elif user_input == "2":
        forge版本1_9()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列选择1_8():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本1_8_9()
    elif user_input == "2":
        forge版本1_8_8()
    elif user_input == "3":
        forge版本1_8()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()


###############################################
#forge版本选择部分
###############################################
def forge版本系列1_20():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.20.1")
    print ("2: 1.20")
    print ("=" * 20)
    print ("按下对应数字按键以继续")
    forge版本系列选择1_20()

def forge版本系列1_19():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.19.4")
    print ("2: 1.19.3")
    print ("3: 1.19.2")
    print ("4: 1.19.1")
    print ("5: 1.19")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_19()

def forge版本系列1_18():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.18.2")
    print ("2: 1.18.1")
    print ("3: 1.18")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_18()

def forge版本系列1_17():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.17.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_17()

def forge版本系列1_16():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.16.5")
    print ("2: 1.16.4")
    print ("3: 1.16.3")
    print ("4: 1.16.2")
    print ("5: 1.16.1")
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_16()

def forge版本系列1_15():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.15.2")
    print ("2: 1.15.1")
    print ("3: 1.15")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_15()

def forge版本系列1_14():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.14.4")
    print ("2: 1.14.3")
    print ("3: 1.14.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_14()

def forge版本系列1_13():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.13.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_13()

def forge版本系列1_12():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.12.2")
    print ("2: 1.12.1")
    print ("3: 1.12")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_12()

def forge版本系列1_11():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.11.2")
    print ("2: 1.11")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_11()

def forge版本系列1_10():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.10.2")
    print ("2: 1.10")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_10()

def forge版本系列1_9():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.9.4")
    print ("2: 1.9")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_9()

def forge版本系列1_8():
    os.system('cls')
    print ("按下对应数字按键以继续,输入t退出")
    print ("=" * 20)
    print ("1: 1.8.9")
    print ("2: 1.8.8")
    print ("3: 1.8")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列选择1_8()

 
def forge版本范围选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本系列1()
    elif user_input == "2":
        forge版本系列2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def forge版本系列1选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本系列1_20()
    elif user_input == "2":
        forge版本系列1_19()
    elif user_input == "3":
        forge版本系列1_18()
    elif user_input == "4":
        forge版本系列1_17()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()



def forge版本系列2选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge版本系列1_16()
    elif user_input == "2":
        forge版本系列1_15()
    elif user_input == "3":
        forge版本系列1_14()
    elif user_input == "4":
        forge版本系列1_13()
    elif user_input == "5":
        forge版本系列1_12()
    elif user_input == "6":
        forge版本系列1_11()
    elif user_input == "7":
        forge版本系列1_10()
    elif user_input == "8":
        forge版本系列1_9()
    elif user_input == "9":
        forge版本系列1_8()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()


def forge版本系列1():
    os.system('cls') 
    print ("1.17系列---1.20系列")
    print ("=" * 20)
    print ("1: 1.20系列")
    print ("2: 1.19系列")
    print ("3: 1.18系列")
    print ("4: 1.17系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    forge版本系列1选择()

def forge版本系列2():
    os.system('cls') 
    print ("1.8系列---1.16系列")
    print ("=" * 20)
    print ("1: 1.16系列")
    print ("2: 1.15系列")
    print ("3: 1.14系列")
    print ("4: 1.13系列")
    print ("5: 1.12系列")
    print ("6: 1.11系列")
    print ("7: 1.10系列")
    print ("8: 1.9系列")
    print ("9: 1.8系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    forge版本系列2选择()

def forge():
    os.system('cls')                       #forge版本范围选择菜单
    print ("   请选择版本范围   ")
    print ("=" * 20)
    print ("1: 1.17系列-1.20系列")
    print ("2: 1.8系列-1.16系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    forge版本范围选择()   

###############################################
#fabric版本文件下载
###############################################

def fabric版本1_20_1():   
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.20.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.20.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_20():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.20.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.20.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_19_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.19.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.19.4.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_19_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.19.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.19.3.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_19_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.19.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.19.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_19_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.19.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.19.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_19():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.19.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.19.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_18_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.18.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.18.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_18_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.18.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.18.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_18():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.18.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.18.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_17_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.17.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.17.1.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_17():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.17.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.17.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_16_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.16.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.16.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_16_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.16.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.16.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_16_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.16.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.16.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_16_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.16.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.16.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_16_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.16.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.16.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_16():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.16.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.16.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_15_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.15.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.15.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_15_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.15.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.15.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_15():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.15.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.15.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_14_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.14.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.14.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_14_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.14.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.14.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_14_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.14.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.14.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_14_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.14.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.14.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def fabric版本1_14():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/fabric-server/fabric-server-1.14.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/fabric-server-1.14.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()



###############################################
#fabric系列核心版本选择
###############################################
def fabric版本系列选择1_20():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本1_20_1()
    elif user_input == "2":
        fabric版本1_20()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def fabric版本系列选择1_19():            
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本1_19_4()
    elif user_input == "2":
        fabric版本1_19_3()
    elif user_input == "3":
        fabric版本1_19_2()
    elif user_input == "4":
        fabric版本1_19_1()
    elif user_input == "5":
        fabric版本1_19()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def fabric版本系列选择1_18():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本1_18_2()
    elif user_input == "2":
        fabric版本1_18_1()
    elif user_input == "3":
        fabric版本1_18()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def fabric版本系列选择1_17():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本1_17_1()
    elif user_input == "2":
        fabric版本1_17()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def fabric版本系列选择1_16():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本1_16_5()
    elif user_input == "2":
        fabric版本1_16_4()
    elif user_input == "3":
        fabric版本1_16_3()
    elif user_input == "4":
        fabric版本1_16_2()
    elif user_input == "5":
        fabric版本1_16_1()
    elif user_input == "6":
        fabric版本1_16()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def fabric版本系列选择1_15():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本1_15_2()
    elif user_input == "2":
        fabric版本1_15_1()
    elif user_input == "2":
        fabric版本1_15()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def fabric版本系列选择1_14():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本1_14_4()
    elif user_input == "2":
        fabric版本1_14_3()
    elif user_input == "3":
        fabric版本1_14_2()
    elif user_input == "4":
        fabric版本1_14_1()
    elif user_input == "5":
        fabric版本1_14()
    elif user_input == "6":
        fabric版本1_16()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()


###############################################
#fabric部分
###############################################

def fabric版本系列1_20():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.20.1")
    print ("2: 1.20")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    fabric版本系列选择1_20()

def fabric版本系列1_19():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.19.4")
    print ("2: 1.19.3")
    print ("3: 1.19.2")
    print ("4: 1.19.1")
    print ("5: 1.19")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    fabric版本系列选择1_19()

def fabric版本系列1_18():
    os.system('cls')
    print ("按下对应数字按键以继续,输入t退出")
    print ("=" * 20)
    print ("1: 1.18.2")
    print ("2: 1.18.1")
    print ("3: 1.18")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    fabric版本系列选择1_18()

def fabric版本系列1_17():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.17.1")
    print ("2: 1.17")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    fabric版本系列选择1_17()

def fabric版本系列1_16():
    os.system('cls')
    print ("按下对应数字按键以继续,输入t退出")
    print ("=" * 20)
    print ("1: 1.16.5")
    print ("2: 1.16.4")
    print ("3: 1.16.3")
    print ("4: 1.16.2")
    print ("5: 1.16.1")
    print ("6: 1.16")
    print ("=" * 20)
    print ("按下对应数字按键以继续")
    fabric版本系列选择1_16()

def fabric版本系列1_15():
    os.system('cls')
    print ("按下对应数字按键以继续,输入t退出")
    print ("=" * 20)
    print ("1: 1.15.2")
    print ("2: 1.15.1")
    print ("3: 1.15")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    fabric版本系列选择1_15()

def fabirc版本系列1_14():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.14.4")
    print ("2: 1.14.3")
    print ("3: 1.14.2")
    print ("4: 1.14.1")
    print ("5: 1.14")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    fabric版本系列选择1_14()

def fabric版本范围选择():            #fabric核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本系列()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

###############################################
#fabric核心版本范围选择
###############################################
def fabric版本系列选择():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        fabric版本系列1_20()
    elif user_input == "2":
        fabric版本系列1_19()
    elif user_input == "3":
        fabric版本系列1_18()
    elif user_input == "4":
        fabric版本系列1_17()
    elif user_input == "5":
        fabric版本系列1_16()
    elif user_input == "6":
        fabric版本系列1_15()
    elif user_input == "7":
        fabirc版本系列1_14()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

###############################################
#fabric版本范围选择
###############################################

def fabric版本系列():
    os.system('cls')
    print ("1.14系列---1.20系列")
    print ("=" * 20)
    print ("1: 1.20系列")
    print ("2: 1.19系列")
    print ("3: 1.18系列")
    print ("4: 1.17系列")
    print ("5: 1.16系列")
    print ("6: 1.15系列")
    print ("7: 1.14系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    fabric版本系列选择()

def fabric():
    os.system('cls') 
    print ("   请选择版本范围   ")
    print ("=" * 20)
    print ("1: 1.14系列-1.20系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    fabric版本范围选择()


###############################################
#插件 + forge核心选择及下载
###############################################

def cat_server1_18_2():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cat_server/CatServer-1.18.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/CatServer-1.18.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def cat_server1_16_5():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cat_server/CatServer-1.16.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/CatServer-1.16.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def cat_server1_12_2():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cat_server/CatServer-1.12.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/CatServer-1.12.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def cat_server版本选择():            #cat_server核心版本选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        cat_server1_18_2()
    elif user_input == "2":
        cat_server1_16_5()
    elif user_input == "3":
        cat_server1_12_2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def cat_server():
    os.system('cls') 
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.18.2")
    print ("2: 1.16.5")
    print ("3: 1.12.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    cat_server版本选择()

def mo_server1_20_1():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/mo_server/mohist-1.20.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/mohist-1.20.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def mo_server1_19_4():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/mo_server/mohist-1.19.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/mohist-1.19.4.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def mo_server1_19_2():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/mo_server/mohist-1.19.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/mohist-1.19.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def mo_server_1_18_2():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/mo_server/mohist-1.18.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/mohist-1.18.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit

def mo_server1_16_5():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/mo_server/mohist-1.16.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/mohist-1.16.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def mo_server_1_12_2():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/mo_server/mohist-1.12.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/mohist-1.12.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def mo_server_1_7_10():
    print ("开始下载文件")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/mo_server/mohist-1.7.10.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/mohist-1.7.10.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()


def mo_server版本选择():            #mo_server核心版本选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        mo_server1_20_1()
    elif user_input == "2":
        mo_server1_19_4()
    elif user_input == "3":
        mo_server1_19_2()
    elif user_input == "4":
        mo_server_1_18_2()
    elif user_input == "5":
        mo_server1_16_5()
    elif user_input == "6":
        mo_server_1_12_2()
    elif user_input == "7":
        mo_server_1_7_10()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def mo_server():
    os.system('cls') 
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.20.1")
    print ("2: 1.19.4")
    print ("3: 1.19.2")
    print ("4: 1.18.2")
    print ("5: 1.16.5")
    print ("6: 1.12.2")
    print ("7: 1.7.10")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    mo_server版本选择()



###############################################
#bukkit文件下载
###############################################

def bukkit版本1_20_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.20.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.20.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_19_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.19.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.19.4.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_19_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.19.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.19.3.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_19_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.19.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.19.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_19_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.19.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.19.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_19():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.19.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.19.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_18_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.18.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.18.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_18_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.18.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.18.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_18():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.18.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.18.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()
    
def bukkit版本1_17_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.17.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.17.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_17():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.17.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.17.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_16_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.16.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.16.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_16_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.16.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.16.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_16_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.16.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.16.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_16_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.16.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.16.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_16_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.16.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.16.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_15_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.15.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.15.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_15_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.15.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.15.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_15():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.15.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.15.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_14_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.14.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.14.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_14_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.14.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.14.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_14_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.14.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.14.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_14_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.14.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.14.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_14():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.14.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.14.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_13_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.13.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.13.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_13_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.13.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.13.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_13():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.13.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.13.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_12_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.12.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.12.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_12_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.12.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.12.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_12():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.12.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.12.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_11_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.11.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.11.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_11_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.11.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.11.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_11():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.11.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.11.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_10_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.10.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.10.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_10():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.10.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.10.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_9_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.9.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.9.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_9_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.9.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.9.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_9():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.9.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.9.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_8_8():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.8.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.8.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_8_7():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.8.7.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.8.7.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_8_6():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.8.6.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.8.6.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_8_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.8.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.8.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_8_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.8.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.8.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_8_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.8.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.8.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_8():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_7_10():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.7.10.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.7.10.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_7_9():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.7.9.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.7.9.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_7_8():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.7.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.7.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_7_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.7.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.7.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_7_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.7.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.7.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_6_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.6.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.6.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_6_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.6.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.6.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_6_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.6.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.6.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_5_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.5.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.5.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_5_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.5.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.5.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_4_7():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.4.7.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.4.7.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_4_6():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.4.6.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.4.6.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_4_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.4.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.4.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_4_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.4.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.4.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_3_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.3.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.3.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_3_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.3.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.3.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_2_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.2.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.2.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_2_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.2.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.2.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_2_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.2.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.2.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_2_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.2.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.2.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def bukkit版本1_0_0():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/craftbukkit/craftbukkit-1.0.0.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/craftbukkit-1.0.0.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()
    
###############################################
#bukkit版本范围选择部分
###############################################

def bukkit版本系列选择1_20():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_20_1()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_19():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_19_4()
    elif user_input == "2":
        bukkit版本1_19_3()
    elif user_input == "3":
        bukkit版本1_19_2
    elif user_input == "4":
        bukkit版本1_19_1
    elif user_input == "5":
        bukkit版本1_19
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_18():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_18_2()
    elif user_input == "2":
        bukkit版本1_18_1()
    elif user_input == "3":
        bukkit版本1_18
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_17():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_17_1()
    elif user_input == "2":
        bukkit版本1_17()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_16():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_16_5()
    elif user_input == "2":
        bukkit版本1_16_4()
    elif user_input == "3":
        bukkit版本1_16_3()
    elif user_input == "4":
        bukkit版本1_16_2()
    elif user_input == "5":
        bukkit版本1_16_1
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_15():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_15_2()
    elif user_input == "2":
        bukkit版本1_15_1()
    elif user_input == "3":
        bukkit版本1_15()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_14():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_14_4()
    elif user_input == "2":
        bukkit版本1_14_3()
    elif user_input == "3":
        bukkit版本1_14_2
    elif user_input == "4":
        bukkit版本1_14_1
    elif user_input == "5":
        bukkit版本1_14
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_13():            
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_13_2()
    elif user_input == "2":
        bukkit版本1_13_1()
    elif user_input == "3":
        bukkit版本1_13()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_12():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_12_2()
    elif user_input == "2":
        bukkit版本1_12_1()
    elif user_input == "3":
        bukkit版本1_12()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_11():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_11_2()
    elif user_input == "2":
        bukkit版本1_11_1()
    elif user_input == "3":
        bukkit版本1_11()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_10():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_10_2()
    elif user_input == "2":
        bukkit版本1_10()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_9():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_9_4()
    elif user_input == "2":
        bukkit版本1_9_2()
    elif user_input == "3":
        bukkit版本1_9()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_8():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_8_8()
    elif user_input == "2":
        bukkit版本1_8_7()
    elif user_input == "3":
        bukkit版本1_8_6()
    elif user_input == "4":
        bukkit版本1_8_5()
    elif user_input == "5":
        bukkit版本1_8_4()
    elif user_input == "6":
        bukkit版本1_8_3()
    elif user_input == "7":
        bukkit版本1_8
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_7():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_7_10()
    if user_input == "2":
        bukkit版本1_7_9()
    if user_input == "3":
        bukkit版本1_7_8()
    if user_input == "4":
        bukkit版本1_7_5()
    if user_input == "5":
        bukkit版本1_7_2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_6():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_6_4()
    elif user_input == "2":
        bukkit版本1_6_2()
    elif user_input == "3":
        bukkit版本1_6_1()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_5():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_5_2()
    elif user_input == "3":
        bukkit版本1_5_1
    elif user_input == "2":
        bukkit版本1_5()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_4():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_4_7()
    elif user_input == "2":
        bukkit版本1_4_6()
    elif user_input == "3":
        bukkit版本1_4_5()
    elif user_input == "2":
        bukkit版本1_4_2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_3():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_3_2()
    elif user_input == "2":
        bukkit版本1_3_1()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_2():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_2_5()
    elif user_input == "2":
        bukkit版本1_2_4()
    elif user_input == "3":
        bukkit版本1_2_3()
    elif user_input == "4":
        bukkit版本1_2_2
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_1():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_1()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列选择1_0():                     
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本1_0_0()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()


def bukkit版本系列1_20():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.20.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_20()

def bukkit版本系列1_19():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.19.4")
    print ("2: 1.19.3")
    print ("3: 1.19.2")
    print ("4: 1.19.1")
    print ("5: 1.19")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_19()

def bukkit版本系列1_18():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.18.2")
    print ("2: 1.18.1")
    print ("3: 1.18")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_18()

def bukkit版本系列1_17():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.17.1")
    print ("2: 1.17")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_17()

def bukkit版本系列1_16():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.16.5")
    print ("2: 1.16.4")
    print ("4: 1.16.3")
    print ("5: 1.16.2")
    print ("6: 1.16.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_16()

def bukkit版本系列1_15():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.15.2")
    print ("2: 1.15.1")
    print ("3: 1.15")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_15()

def bukkit版本系列1_14():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.14.4")
    print ("2: 1.14.3")
    print ("3: 1.14.2")
    print ("4: 1.14.1")
    print ("5: 1.14")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_14()
 
def bukkit版本系列1_13():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.13.2")
    print ("2: 1.13.1")
    print ("3: 1.13")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_13()

def bukkit版本系列1_12():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.12.2")
    print ("2: 1.12.1")
    print ("3: 1.12")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_12()

def bukkit版本系列1_11():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.11.2")
    print ("2: 1.11.1")
    print ("3: 1.11")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_11()

def bukkit版本系列1_10():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.10.2")
    print ("2: 1.10")
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_10()

def bukkit版本系列1_9():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.9.4")
    print ("2: 1.9.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_9()

def bukkit版本系列1_8():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.8.8")
    print ("2: 1.8.7")
    print ("3: 1.8.6")
    print ("4: 1.8.5")
    print ("5: 1.8.4")
    print ("6: 1.8.3")
    print ("7: 1.8")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_8()

def bukkit版本系列1_7():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.7.10")
    print ("2: 1.7.9")
    print ("3: 1.7.8")
    print ("4: 1.7.5")
    print ("5: 1.7.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_7()

def bukkit版本系列1_6():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.6.4")
    print ("2: 1.6.2")
    print ("3: 1.6.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_6()

def bukkit版本系列1_5():
    os.system('cls') 
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.5.2")
    print ("2: 1.5.1")
    print ("3: 1.5")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_5()

def bukkit版本系列1_4():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.4.7")
    print ("2: 1.4.6")
    print ("3: 1.4.5")
    print ("4: 1.4.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_4()

def bukkit版本系列1_3():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.3.2")
    print ("2: 1.3.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_3()

def bukkit版本系列1_2():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.2.5")
    print ("2: 1.2.4")
    print ("3: 1.2.3")
    print ("4: 1.2.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_2()

def bukkit版本系列1_1():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_1()

def bukkit版本系列1_0():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.0.0")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列选择1_0()

def bukkit版本系列1选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本系列1_20()
    elif user_input == "2":
        bukkit版本系列1_19()
    elif user_input == "3":
        bukkit版本系列1_18()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列2选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本系列1_17()
    elif user_input == "2":
        bukkit版本系列1_16()
    elif user_input == "3":
        bukkit版本系列1_15()
    elif user_input == "4":
        bukkit版本系列1_14()
    elif user_input == "5":
        bukkit版本系列1_13()
    elif user_input == "6":
        bukkit版本系列1_12()
    elif user_input == "7":
        bukkit版本系列1_11()
    elif user_input == "8":
        bukkit版本系列1_10()
    elif user_input == "9":
        bukkit版本系列1_9()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列3选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本系列1_8()
    elif user_input == "2":
        bukkit版本系列1_7()
    elif user_input == "3":
        bukkit版本系列1_6()
    elif user_input == "4":
        bukkit版本系列1_5()
    elif user_input == "5":
        bukkit版本系列1_4()
    elif user_input == "6":
        bukkit版本系列1_3()
    elif user_input == "7":
        bukkit版本系列1_2()
    elif user_input == "8":
        bukkit版本系列1_1()
    elif user_input == "9":
        bukkit版本系列1_0()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit版本系列1():
    os.system('cls') 
    print ("1.18系列---1.20系列")
    print ("=" * 20)
    print ("1: 1.20系列")
    print ("2: 1.19系列")
    print ("3: 1.18系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    bukkit版本系列1选择()

def bukkit版本系列2():
    os.system('cls') 
    print ("1.9系列---1.17系列")
    print ("=" * 20)
    print ("1: 1.17系列")
    print ("2: 1.16系列")
    print ("3: 1.15系列")
    print ("4: 1.14系列")
    print ("5: 1.13系列")
    print ("6: 1.12系列")
    print ("7: 1.11系列")
    print ("8: 1.10系列")
    print ("9: 1.9系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    bukkit版本系列2选择()

def bukkit版本系列3():
    os.system('cls') 
    print ("1.0系列-1.8系列")
    print ("=" * 20)
    print ("1: 1.8系列")
    print ("2: 1.7系列")
    print ("3: 1.6系列")
    print ("4: 1.5系列")
    print ("5: 1.4系列")
    print ("6: 1.3系列")
    print ("7: 1.2系列")
    print ("8: 1.1系列")
    print ("9: 1.0系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    bukkit版本系列3选择()

def bukkit版本范围选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        bukkit版本系列1()
    elif user_input == "2":
        bukkit版本系列2()
    elif user_input == "3":
        bukkit版本系列3()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def bukkit():
    os.system('cls')                       
    print ("   请选择版本范围   ")
    print ("=" * 20)
    print ("1: 1.18系列-1.20系列")
    print ("2: 1.9系列-1.17系列")
    print ("3: 1.0系列-1.8系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    bukkit版本范围选择() 


###############################################
#spigot文件下载
###############################################

def spigot版本1_20_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.20.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.20.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_19_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.19.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.19.4.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_19_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.19.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.19.3.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_19_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.19.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.19.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_19_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.19.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.19.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_19():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.19.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.19.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_18_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.18.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.18.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_18_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.18.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.18.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_18():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.18.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.18.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_17_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.17.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.17.1.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_17():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.17.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.17.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_16_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.16.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.16.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_16_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.16.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.16.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_16_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.16.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.16.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_16_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.16.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.16.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_16_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.16.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.16.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_15_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.15.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.15.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_15_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.15.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.15.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_15():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.15.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.15.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_14_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.14.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.14.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_14_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.14.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.14.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_14_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.14.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.14.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_14_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.14.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.14.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_14():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.14.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.14.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_13_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.13.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.13.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_13_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.13.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.13.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_13():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.13.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.13.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_12_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.12.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.12.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_12_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.12.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.12.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_12():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.12.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.12.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_11_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.11.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.11.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_11_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.11.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.11.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_11():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.11.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.11.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_10_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.10.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.10.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_10():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.10.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.10.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_9_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.9.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.9.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_9_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.9..zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.9.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_9():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.9.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.9.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_8_8():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.8.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.8.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_8_7():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.8.7.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.8.7.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_8_6():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.8.6.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.8.6.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_8_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.8.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.8.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_8_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.8.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.8.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_8_3():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.8.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.8.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_8():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_7_10():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.7.10.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.7.10.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_7_9():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.7.9.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.7.9.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_7_8():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.7.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.7.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_7_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.7.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.7.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_7_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.7.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.7.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_6_4():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.6.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.6.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_6_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.6.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.6.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_6_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.6.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.6.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_5_2():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.5.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.5.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_5_1():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.5.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.5.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_5():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_4_7():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.4.7.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.4.7.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def spigot版本1_4_6():
    print ("开始下载")
    os.system('cls')
    print ("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/spigot/spigot-1.4.6.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/spigot-1.4.6.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'
    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

###############################################
#spigot版本范围选择部分
###############################################

def spigot版本系列选择1_20():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_20_1()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_19():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_19_4()
    elif user_input == "2":
        spigot版本1_19_3()
    elif user_input == "3":
        spigot版本1_19_2
    elif user_input == "4":
        spigot版本1_19_1
    elif user_input == "5":
        spigot版本1_19
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_18():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_18_2()
    elif user_input == "2":
        spigot版本1_18_1()
    elif user_input == "3":
        spigot版本1_18
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_17():   #需要java16
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_17_1()
    elif user_input == "2":
        spigot版本1_17()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_16():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_16_5()
    elif user_input == "2":
        spigot版本1_16_4()
    elif user_input == "3":
        spigot版本1_16_3()
    elif user_input == "4":
        spigot版本1_16_2()
    elif user_input == "5":
        spigot版本1_16_1
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_15():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_15_2()
    elif user_input == "2":
        spigot版本1_15_1()
    elif user_input == "3":
        spigot版本1_15()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_14():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_14_4()
    elif user_input == "2":
        spigot版本1_14_3()
    elif user_input == "3":
        spigot版本1_14_2
    elif user_input == "4":
        spigot版本1_14_1
    elif user_input == "5":
        spigot版本1_14
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_13():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_13_2()
    elif user_input == "2":
        spigot版本1_13_1()
    elif user_input == "3":
        spigot版本1_13()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_12():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_12_2()
    elif user_input == "2":
        spigot版本1_12_1()
    elif user_input == "3":
        spigot版本1_12()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_11():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_11_2()
    elif user_input == "2":
        spigot版本1_11_1()
    elif user_input == "3":
        spigot版本1_11()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_10():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_10_2()
    elif user_input == "2":
        spigot版本1_10()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_9():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_9_4()
    elif user_input == "2":
        spigot版本1_9_2()
    elif user_input == "2":
        spigot版本1_9()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_8():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_8_8()
    elif user_input == "2":
        spigot版本1_8_7()
    elif user_input == "3":
        spigot版本1_8_6()
    elif user_input == "4":
        spigot版本1_8_5()
    elif user_input == "5":
        spigot版本1_8_4()
    elif user_input == "6":
        spigot版本1_8_3()
    elif user_input == "7":
        spigot版本1_8
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_7():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_7_10()
    if user_input == "1":
        spigot版本1_7_9()
    if user_input == "1":
        spigot版本1_7_8()
    if user_input == "1":
        spigot版本1_7_5()
    if user_input == "1":
        spigot版本1_7_2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_6():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_6_4()
    if user_input == "2":
        spigot版本1_6_2
    elif user_input == "t":
        exit()

def spigot版本系列选择1_5():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_5_2()
    if user_input == "2":
        spigot版本1_5_1()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列选择1_4():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本1_4_7()
    if user_input == "2":
        spigot版本1_4_6()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()


def spigot版本系列1_20():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.20.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_20()

def spigot版本系列1_19():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.19.4")
    print ("2: 1.19.3")
    print ("3: 1.19.2")
    print ("4: 1.19.1")
    print ("5: 1.19")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_19()

def spigot版本系列1_18():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.18.2")
    print ("2: 1.18.1")
    print ("3: 1.18")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_18()

def spigot版本系列1_17():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.17.1")
    print ("2: 1.17")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_17()

def spigot版本系列1_16():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.16.5")
    print ("1: 1.16.4")
    print ("1: 1.16.3")
    print ("1: 1.16.2")
    print ("2: 1.16.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_16()

def spigot版本系列1_15():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.15.2")
    print ("1: 1.15.1")
    print ("2: 1.15")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_15()

def spigot版本系列1_14():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.14.4")
    print ("1: 1.14.3")
    print ("1: 1.14.2")
    print ("1: 1.14.1")
    print ("2: 1.14")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_14()
 
def spigot版本系列1_13():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.13.2")
    print ("2: 1.13.1")
    print ("3: 1.13")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_13()

def spigot版本系列1_12():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.12.2")
    print ("2: 1.12.1")
    print ("3: 1.12")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_12()

def spigot版本系列1_11():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.11.2")
    print ("2: 1.11.1")
    print ("3: 1.11")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_11()

def spigot版本系列1_10():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.10.2")
    print ("2: 1.10")
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_10()

def spigot版本系列1_9():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.9.4")
    print ("2: 1.9.2")
    print ("3: 1.9")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_9()

def spigot版本系列1_8():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.8.8")
    print ("2: 1.8.7")
    print ("3: 1.8.6")
    print ("4: 1.8.5")
    print ("5: 1.8.4")
    print ("6: 1.8.3")
    print ("7: 1.8")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_8()

def spigot版本系列1_7():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.7.10")
    print ("1: 1.7.9")
    print ("1: 1.7.8")
    print ("1: 1.7.5")
    print ("1: 1.7.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_7()

def spigot版本系列1_6():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.6.4")
    print ("2: 1.6.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_6()

def spigot版本系列1_5():
    os.system('cls') 
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.5.2")
    print ("2: 1.5.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_5()

def spigot版本系列1_4():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.4.7")
    print ("2: 1.4.6")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    spigot版本系列选择1_4()

def spigot版本系列1选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本系列1_20()
    elif user_input == "2":
        spigot版本系列1_19()
    elif user_input == "3":
        spigot版本系列1_18()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot版本系列2选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本系列1_17()
    elif user_input == "2":
        spigot版本系列1_16()
    elif user_input == "3":
        spigot版本系列1_15()
    elif user_input == "4":
        spigot版本系列1_14()
    elif user_input == "5":
        spigot版本系列1_13()
    elif user_input == "6":
        spigot版本系列1_12()
    elif user_input == "7":
        spigot版本系列1_11()
    elif user_input == "8":
        spigot版本系列1_10()
    elif user_input == "9":
        spigot版本系列1_9()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()


def spigot版本系列1():
    os.system('cls') 
    print ("1.13系列---1.20系列")
    print ("=" * 20)
    print ("1: 1.20系列")
    print ("2: 1.19系列")
    print ("3: 1.18系列")
    print ("4: 1.17系列")
    print ("5: 1.16系列")
    print ("6: 1.15系列")
    print ("7: 1.14系列")
    print ("8: 1.13系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    spigot版本系列1选择()

def spigot版本系列2():
    os.system('cls') 
    print ("1.4系列-1.12系列")
    print ("=" * 20)
    print ("1: 1.12系列")
    print ("2: 1.11系列")
    print ("3: 1.10系列")
    print ("4: 1.9系列")
    print ("5: 1.8系列")
    print ("6: 1.7系列")
    print ("7: 1.6系列")
    print ("8: 1.5系列")
    print ("9: 1.4系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    spigot版本系列2选择()

def spigot版本范围选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        spigot版本系列1()
    elif user_input == "2":
        spigot版本系列2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def spigot():
    os.system('cls')                       
    print ("   请选择版本范围   ")
    print ("=" * 20)
    print ("1: 1.13系列-1.20系列")
    print ("2: 1.4系列-1.12系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    spigot版本范围选择()


###############################################
#Paper文件下载
###############################################

def Paper版本1_20_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.20.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.20.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_20():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.20.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.20.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_19_4():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.19.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.19.4.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_19_3():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.19.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.19.3.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_19_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.19.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.19.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_19_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.19.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.19.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_19():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.19.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.19.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_18_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.18.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.18.2.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_18_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.18.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.18.1.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_18():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.18.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java17.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.18.zip",
    "server/java17.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_17_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.17.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.17.1.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_17():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.17.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java16.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.17.zip",
    "server/java16.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_16_5():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.16.5.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.16.5.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_16_4():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.16.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.16.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_16_3():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.16.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.16.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_16_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.16.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.16.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_16_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.16.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.16.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_15_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.15.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.15.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_15_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.16.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.15.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_15():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.15.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.15.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_14_4():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.14.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.14.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_14_3():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.14.3.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.14.3.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_14_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.14.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.14.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_14_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.14.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.14.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_14():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.14.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.14.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_13_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.13.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.13.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_13_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.13.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.13.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_13():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.13.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.13.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_12_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.12.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.12.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_12_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.12.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.12.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_12():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.12.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.12.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_11_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.11.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.11.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_11_1():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.11.1.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.11.1.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_11():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.11.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.11.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_10_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.10.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.10.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_10():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.10.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.10.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_9_4():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.9.4.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.9.4.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_9_2():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.9.2.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.9.2.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_9():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.9.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.9.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

def Paper版本1_8_8():
    os.system('cls')
    print("开始下载")
    file_urls = ["https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/paper/paper-1.8.8.zip","https://ghps.cc/https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/java-lite/java8.zip"]  # 要下载的文件URL列表
    download_folder = "server"
    downloader.download_files(file_urls, download_folder)
    zip_files = [
    "server/paper-1.8.8.zip",
    "server/java8.zip"
    ]
    destination_folders = [
    "server",
    "server"
    ]
    压缩文件解压(zip_files, destination_folders)
    directory_path = 'server/'

    压缩文件删除(directory_path)
    os.system('cls')
    print("下载完成")
    input("按下任意键继续...")
    exit()

###############################################
#Paper版本范围选择部分
###############################################

def Paper版本系列选择1_20():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_20_1()
    elif user_input == "2":
        Paper版本1_20()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_19():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_19_4()
    elif user_input == "2":
        Paper版本1_19_3()
    elif user_input == "3":
        Paper版本1_19_2
    elif user_input == "4":
        Paper版本1_19_1
    elif user_input == "5":
        Paper版本1_19
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_18():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_18_2()
    elif user_input == "2":
        Paper版本1_18_1()
    elif user_input == "3":
        Paper版本1_18
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_17():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_17_1()
    elif user_input == "2":
        Paper版本1_17()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_16():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_16_5()
    elif user_input == "2":
        Paper版本1_16_4()
    elif user_input == "3":
        Paper版本1_16_3()
    elif user_input == "4":
        Paper版本1_16_2()
    elif user_input == "5":
        Paper版本1_16_1
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_15():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_15_2()
    elif user_input == "2":
        Paper版本1_15_1()
    elif user_input == "3":
        Paper版本1_15()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_14():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_14_4()
    elif user_input == "2":
        Paper版本1_14_3()
    elif user_input == "3":
        Paper版本1_14_2
    elif user_input == "4":
        Paper版本1_14_1
    elif user_input == "5":
        Paper版本1_14
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_13():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_13_2()
    elif user_input == "2":
        Paper版本1_13_1()
    elif user_input == "3":
        Paper版本1_13()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_12():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_12_2()
    elif user_input == "2":
        Paper版本1_12_1()
    elif user_input == "3":
        Paper版本1_12()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_11():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_11_2()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_10():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_10_2()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_9():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_9_4()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列选择1_8():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本1_8_8()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列1_20():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.20.1")
    print ("2: 1.20")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_20()

def Paper版本系列1_19():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.19.4")
    print ("2: 1.19.3")
    print ("3: 1.19.2")
    print ("4: 1.19.1")
    print ("5: 1.19")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_19()

def Paper版本系列1_18():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.18.2")
    print ("2: 1.18.1")
    print ("3: 1.18")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_18()

def Paper版本系列1_17():  #要用java16
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.17.1")
    print ("2: 1.17")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_17()

def Paper版本系列1_16():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.16.5")
    print ("1: 1.16.4")
    print ("1: 1.16.3")
    print ("1: 1.16.2")
    print ("2: 1.16.1")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_16()

def Paper版本系列1_15():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.15.2")
    print ("1: 1.15.1")
    print ("2: 1.15")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_15()

def Paper版本系列1_14():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.14.4")
    print ("1: 1.14.3")
    print ("1: 1.14.2")
    print ("1: 1.14.1")
    print ("2: 1.14")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_14()

def Paper版本系列1_13():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.13.2")
    print ("2: 1.13.1")
    print ("3: 1.13")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_13()

def Paper版本系列1_12():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.12.2")
    print ("2: 1.12.1(出现问题官方端无法正常部署，请勿使用)")
    print ("3: 1.12(出现问题官方端无法正常部署，请勿使用)")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_12()

def Paper版本系列1_11():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.11.2")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_11()

def Paper版本系列1_10():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.10.2")
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_10()

def Paper版本系列1_9():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.9.4")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_9()

def Paper版本系列1_8():
    os.system('cls')
    print ("请选择服务器核心版本")
    print ("=" * 20)
    print ("1: 1.8.8")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    Paper版本系列选择1_8()


def Paper版本系列1选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本系列1_20()
    elif user_input == "2":
        Paper版本系列1_19()
    elif user_input == "3":
        Paper版本系列1_18()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列2选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本系列1_16()
    elif user_input == "2":
        Paper版本系列1_15()
    elif user_input == "3":
        Paper版本系列1_14()
    elif user_input == "4":
        Paper版本系列1_13()
    elif user_input == "5":
        Paper版本系列1_12()
    elif user_input == "6":
        Paper版本系列1_11()
    elif user_input == "7":
        Paper版本系列1_10()
    elif user_input == "8":
        Paper版本系列1_9()
    elif user_input == "9":
        Paper版本系列1_8()
    elif user_input == "t":
        exit()
    else:
        print("无效的输入")
        input("按下任意键继续...")
        player()

def Paper版本系列1():
    os.system('cls') 
    print ("1.17系列---1.20系列")
    print ("=" * 20)
    print ("1: 1.20系列")
    print ("2: 1.19系列")
    print ("3: 1.18系列")
    print ("4: 1.17系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    Paper版本系列1选择()

def Paper版本系列2():
    os.system('cls') 
    print ("1.8系列-1.16系列")
    print ("=" * 20)
    print ("1: 1.16系列")
    print ("2: 1.15系列")
    print ("3: 1.14系列")
    print ("4: 1.13系列")
    print ("5: 1.12系列")
    print ("6: 1.11系列")
    print ("7: 1.10系列")
    print ("8: 1.9系列")
    print ("9: 1.8系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    Paper版本系列2选择()

def Paper版本范围选择():            #核心版本范围选择
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        Paper版本系列1()
    elif user_input == "2":
        Paper版本系列2()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()

def Paper():
    os.system('cls')                      
    print ("   请选择版本范围   ")
    print ("=" * 20)
    print ("1: 1.17系列-1.20系列")
    print ("2: 1.8系列-1.16系列")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出") 
    Paper版本范围选择()

###############################################
#核心选择
###############################################

def 核心选择():
    user_input = input("请输入选择的数字: ")
    if user_input == "1":
        forge()
    elif user_input == "2":
        fabric()
    elif user_input == "3":
        cat_server()
    elif user_input == "4":
        mo_server()
    elif user_input == "5":
        bukkit()
    elif user_input == "6":
        spigot()
    elif user_input == "7":
        Paper()
    elif user_input == "t":
        exit()
    else:
     print("无效的输入")
     input("按下任意键继续...")
     player()


###############################################
#初始菜单
###############################################

def player():
    os.system('cls')
    print ("请选择服务器核心")
    print ("=" * 20)
    print ("1: froge")
    print ("2: fabric")
    print ("3: cat_server")
    print ("4: mo_server")
    print ("5: bukkit")
    print ("6: spigot")
    print ("7: Paper")
    print ("=" * 20)
    print ("按下对应数字按键以继续,输入t退出")
    核心选择()

声明()
基础教程()
核心作用()
player()

