import platform
import os
import requests
from tqdm import tqdm
import zipfile
import tarfile
import shutil
from urllib.parse import unquote
import re

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


def statement():
    print("免责声明：")
    print("1. 本脚本一切均来自官方源转载，非商用")
    print("2. 本脚本只负责基础包装服务器，服务器除特殊版本均可正常使用。添加模组后无法运行不归本脚本负责")
    print("3. 本脚本为公益脚本，严禁倒卖商业")
    print("4. 无论服务器做和用途，本人概不负责")
    print("5. 本脚本仅由个人开发，请自行甄别作者")
    print("7. 使用本脚本后默认自动同意我的世界eula")
    print("8. eula详细内容请访问https://www.minecraft.net/zh-hans/eula")
    print("6. 反馈邮箱: dyx45d@163.com 作者QQ: 3636695284")
    input("按下任意键继续...")
    clear_screen()


def Basic_tutorials():
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
    print("14. server文件编辑教程下载https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download"
          "/Advanced_server_editing_tutorial/server.docx")
    input("按下任意键继续...")
    clear_screen()


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
    # 原版部分
    "Minecraft_server_1.20.4": "https://piston-data.mojang.com/v1/objects/8dd1a28015f51b1803213892b50b7b4fc76e594d/server.jar",
    "Minecraft_server_1.20.3": "https://piston-data.mojang.com/v1/objects/4fb536bfd4a83d61cdbaf684b8d311e66e7d4c49/server.jar",
    "Minecraft_server_1.20.2": "https://piston-data.mojang.com/v1/objects/5b868151bd02b41319f54c8d4061b8cae84e665c/server.jar",
    "Minecraft_server_1.20.1": "https://piston-data.mojang.com/v1/objects/0b4dba049482496c507b2387a73a913230ebbd76/server.txt",
    "Minecraft_server_1.20": "https://piston-data.mojang.com/v1/objects/15c777e2cfe0556eef19aab534b186c0c6f277e1/server.jar",
    "Minecraft_server_1.19.4": "https://piston-data.mojang.com/v1/objects/8f3112a1049751cc472ec13e397eade5336ca7ae/server.jar",
    "Minecraft_server_1.19.3": "https://piston-data.mojang.com/v1/objects/c9df48efed58511cdd0213c56b9013a7b5c9ac1f/server.jar",
    "Minecraft_server_1.19.2": "https://piston-data.mojang.com/v1/objects/f69c284232d7c7580bd89a5a4931c3581eae1378/server.jar",
    "Minecraft_server_1.19.1": "https://piston-data.mojang.com/v1/objects/8399e1211e95faa421c1507b322dbeae86d604df/server.jar",
    "Minecraft_server_1.19": "https://piston-data.mojang.com/v1/objects/e00c4052dac1d59a1188b2aa9d5a87113aaf1122/server.jar",
    "Minecraft_server_1.18.2": "https://piston-data.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar",
    "Minecraft_server_1.18.1": "https://piston-data.mojang.com/v1/objects/125e5adf40c659fd3bce3e66e67a16bb49ecc1b9/server.jar",
    "Minecraft_server_1.18": "https://piston-data.mojang.com/v1/objects/3cf24a8694aca6267883b17d934efacc5e44440d/server.jar",
    "Minecraft_server_1.17.1": "https://piston-data.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar",
    "Minecraft_server_1.17": "https://piston-data.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar",
    "Minecraft_server_1.16.5": "https://piston-data.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar",
    "Minecraft_server_1.16.4": "https://piston-data.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar",
    "Minecraft_server_1.16.3": "https://piston-data.mojang.com/v1/objects/f02f4473dbf152c23d7d484952121db0b36698cb/server.jar",
    "Minecraft_server_1.16.2": "https://piston-data.mojang.com/v1/objects/c5f6fb23c3876461d46ec380421e42b289789530/server.jar",
    "Minecraft_server_1.16.1": "https://piston-data.mojang.com/v1/objects/a412fd69db1f81db3f511c1463fd304675244077/server.jar",
    "Minecraft_server_1.16": "https://piston-data.mojang.com/v1/objects/a0d03225615ba897619220e256a266cb33a44b6b/server.jar",
    "Minecraft_server_1.15.2": "https://piston-data.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar",
    "Minecraft_server_1.15.1": "https://piston-data.mojang.com/v1/objects/4d1826eebac84847c71a77f9349cc22afd0cf0a1/server.jar",
    "Minecraft_server_1.15": "https://piston-data.mojang.com/v1/objects/e9f105b3c5c7e85c7b445249a93362a22f62442d/server.jar",
    "Minecraft_server_1.14.4": "https://piston-data.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar",
    "Minecraft_server_1.14.3": "https://piston-data.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar",
    "Minecraft_server_1.14.2": "https://piston-data.mojang.com/v1/objects/808be3869e2ca6b62378f9f4b33c946621620019/server.jar",
    "Minecraft_server_1.14.1": "https://piston-data.mojang.com/v1/objects/ed76d597a44c5266be2a7fcd77a8270f1f0bc118/server.jar",
    "Minecraft_server_1.14": "https://piston-data.mojang.com/v1/objects/f1a0073671057f01aa843443fef34330281333ce/server.jar",
    "Minecraft_server_1.13.2": "https://piston-data.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar",
    "Minecraft_server_1.13.1": "https://piston-data.mojang.com/v1/objects/fe123682e9cb30031eae351764f653500b7396c9/server.jar",
    "Minecraft_server_1.13": "https://piston-data.mojang.com/v1/objects/d0caafb8438ebd206f99930cfaecfa6c9a13dca0/server.jar",
    "Minecraft_server_1.12.2": "https://piston-data.mojang.com/v1/objects/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar",
    "Minecraft_server_1.12.1": "https://piston-data.mojang.com/v1/objects/561c7b2d54bae80cc06b05d950633a9ac95da816/server.jar",
    "Minecraft_server_1.12": "https://piston-data.mojang.com/v1/objects/8494e844e911ea0d63878f64da9dcc21f53a3463/server.jar",
    "Minecraft_server_1.11.2": "https://piston-data.mojang.com/v1/objects/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar",
    "Minecraft_server_1.11.1": "https://piston-data.mojang.com/v1/objects/1f97bd101e508d7b52b3d6a7879223b000b5eba0/server.jar",
    "Minecraft_server_1.11": "https://piston-data.mojang.com/v1/objects/48820c84cb1ed502cb5b2fe23b8153d5e4fa61c0/server.jar",
    "Minecraft_server_1.10.2": "https://piston-data.mojang.com/v1/objects/3d501b23df53c548254f5e3f66492d178a48db63/server.jar",
    "Minecraft_server_1.10.1": "https://piston-data.mojang.com/v1/objects/cb4c6f9f51a845b09a8861cdbe0eea3ff6996dee/server.jar",
    "Minecraft_server_1.10": "https://piston-data.mojang.com/v1/objects/a96617ffdf5dabbb718ab11a9a68e50545fc5bee/server.jar",
    "Minecraft_server_1.9.4": "https://piston-data.mojang.com/v1/objects/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar",
    "Minecraft_server_1.9.3": "https://piston-data.mojang.com/v1/objects/8e897b6b6d784f745332644f4d104f7a6e737ccf/server.jar",
    "Minecraft_server_1.9.2": "https://piston-data.mojang.com/v1/objects/2b95cc7b136017e064c46d04a5825fe4cfa1be30/server.jar",
    "Minecraft_server_1.9.1": "https://piston-data.mojang.com/v1/objects/bf95d9118d9b4b827f524c878efd275125b56181/server.jar",
    "Minecraft_server_1.9": "https://piston-data.mojang.com/v1/objects/b4d449cf2918e0f3bd8aa18954b916a4d1880f0d/server.jar",
    "Minecraft_server_1.8.9": "https://piston-data.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar",
    "Minecraft_server_1.8.8": "https://piston-data.mojang.com/v1/objects/5fafba3f58c40dc51b5c3ca72a98f62dfdae1db7/server.jar",
    "Minecraft_server_1.8.7": "https://piston-data.mojang.com/v1/objects/35c59e16d1f3b751cd20b76b9b8a19045de363a9/server.jar",
    "Minecraft_server_1.8.6": "https://piston-data.mojang.com/v1/objects/2bd44b53198f143fb278f8bec3a505dad0beacd2/server.jar",
    "Minecraft_server_1.8.5": "https://piston-data.mojang.com/v1/objects/ea6dd23658b167dbc0877015d1072cac21ab6eee/server.jar",
    "Minecraft_server_1.8.4": "https://piston-data.mojang.com/v1/objects/dd4b5eba1c79500390e0b0f45162fa70d38f8a3d/server.jar",
    "Minecraft_server_1.8.3": "https://piston-data.mojang.com/v1/objects/dd4b5eba1c79500390e0b0f45162fa70d38f8a3d/server.jar",
    "Minecraft_server_1.8.2": "https://piston-data.mojang.com/v1/objects/a37bdd5210137354ed1bfe3dac0a5b77fe08fe2e/server.jar",
    "Minecraft_server_1.8.1": "https://piston-data.mojang.com/v1/objects/68bfb524888f7c0ab939025e07e5de08843dac0f/server.jar",
    "Minecraft_server_1.8": "https://piston-data.mojang.com/v1/objects/a028f00e678ee5c6aef0e29656dca091b5df11c7/server.jar",
    "Minecraft_server_1.7.10": "https://piston-data.mojang.com/v1/objects/952438ac4e01b4d115c5fc38f891710c4941df29/server.jar",
    "Minecraft_server_1.7.9": "https://piston-data.mojang.com/v1/objects/4cec86a928ec171fdc0c6b40de2de102f21601b5/server.jar",
    "Minecraft_server_1.7.8": "https://piston-data.mojang.com/v1/objects/c69ebfb84c2577661770371c4accdd5f87b8b21d/server.jar",
    "Minecraft_server_1.7.7": "https://piston-data.mojang.com/v1/objects/a6ffc1624da980986c6cc12a1ddc79ab1b025c62/server.jar",
    "Minecraft_server_1.7.6": "https://piston-data.mojang.com/v1/objects/41ea7757d4d7f74b95fc1ac20f919a8e521e910c/server.jar",
    "Minecraft_server_1.7.5": "https://piston-data.mojang.com/v1/objects/e1d557b2e31ea881404e41b05ec15c810415e060/server.jar",
    "Minecraft_server_1.7.4": "https://piston-data.mojang.com/v1/objects/61220311cef80aecc4cd8afecd5f18ca6b9461ff/server.jar",
    "Minecraft_server_1.7.2": "https://piston-data.mojang.com/v1/objects/3716cac82982e7c2eb09f83028b555e9ea606002/server.jar",
    "Minecraft_server_1.6.4": "https://piston-data.mojang.com/v1/objects/050f93c1f3fe9e2052398f7bd6aca10c63d64a87/server.jar",
    "Minecraft_server_1.6.2": "https://piston-data.mojang.com/v1/objects/01b6ea555c6978e6713e2a2dfd7fe19b1449ca54/server.jar",
    "Minecraft_server_1.6.1": "https://piston-data.mojang.com/v1/objects/0252918a5f9d47e3c6eb1dfec02134d1374a89b4/server.jar",
    "Minecraft_server_1.5.2": "https://piston-data.mojang.com/v1/objects/f9ae3f651319151ce99a0bfad6b34fa16eb6775f/server.jar",
    "Minecraft_server_1.5.1": "https://piston-data.mojang.com/v1/objects/d07c71ee2767dabb79fb32dad8162e1b854d5324/server.jar",
    "Minecraft_server_1.5": "https://piston-data.mojang.com/v1/objects/aedad5159ef56d69c5bcf77ed141f53430af43c3/server.jar",
    "Minecraft_server_1.4.7": "https://piston-data.mojang.com/v1/objects/2f0ec8efddd2f2c674c77be9ddb370b727dec676/server.jar",
    "Minecraft_server_1.4.6": "https://piston-data.mojang.com/v1/objects/a0aeb5709af5f2c3058c1cf0dc6b110a7a61278c/server.jar",
    "Minecraft_server_1.4.5": "https://piston-data.mojang.com/v1/objects/c12fd88a8233d2c517dbc8196ba2ae855f4d36ea/server.jar",
    "Minecraft_server_1.4.4": "https://piston-data.mojang.com/v1/objects/4215dcadb706508bf9d6d64209a0080b9cee9e71/server.jar",
    "Minecraft_server_1.4.2": "https://piston-data.mojang.com/v1/objects/5be700523a729bb78ef99206fb480a63dcd09825/server.jar",
    "Minecraft_server_1.3.2": "https://piston-data.mojang.com/v1/objects/3de2ae6c488135596e073a9589842800c9f53bfe/server.jar",
    "Minecraft_server_1.3.1": "https://piston-data.mojang.com/v1/objects/82563ce498bfc1fc8a2cb5bf236f7da86a390646/server.jar",
    "Minecraft_server_1.2.5": "https://piston-data.mojang.com/v1/objects/d8321edc9470e56b8ad5c67bbd16beba25843336/server.jar",
    "Minecraft_server_1.2.4": "https://files.betacraft.uk/server-archive/release/1.2/1.2.4.jar",
    "Minecraft_server_1.2.3": "https://files.betacraft.uk/server-archive/release/1.2/1.2.3.jar",
    "Minecraft_server_1.2.2": "https://files.betacraft.uk/server-archive/release/1.2/1.2.2.jar",
    "Minecraft_server_1.2.1": "https://files.betacraft.uk/server-archive/release/1.2/1.2.1.jar",
    "Minecraft_server_1.1": "https://web.archive.org/web/20120208062853/https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar",
    "Minecraft_server_1.0.1": "https://files.betacraft.uk/server-archive/release/1.0/1.0.1.jar",
    "Minecraft_server_1.0.0": "https://files.betacraft.uk/server-archive/release/1.0/1.0.0.jar",
    # forge部分
    "Forge_server_1.20.4": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.20.4.zip",
    "Forge_server_1.20.3": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.20.3.zip",
    "Forge_server_1.20.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.20.2.zip",
    "Forge_server_1.20.1": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.20.1.zip",
    "Forge_server_1.20": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.20.zip",
    "Forge_server_1.19.4": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.19.4.zip",
    "Forge_server_1.19.3": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.19.3.zip",
    "Forge_server_1.19.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.19.2.zip",
    "Forge_server_1.19.1": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.19.1.zip",
    "Forge_server_1.19": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.19.zip",
    "Forge_server_1.18.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.18.2.zip",
    "Forge_server_1.18.1": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.18.1.zip",
    "Forge_server_1.18": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.18.zip",
    "Forge_server_1.17.1": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.17.1.zip",
    "Forge_server_1.16.5": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.16.5.zip",
    "Forge_server_1.16.4": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.16.4.zip",
    "Forge_server_1.16.3": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.16.3.zip",
    "Forge_server_1.16.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.16.2.zip",
    "Forge_server_1.16.1": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.16.1.zip",
    "Forge_server_1.15.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.15.2.zip",
    "Forge_server_1.15.1": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.15.1.zip",
    "Forge_server_1.15": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.15.zip",
    "Forge_server_1.14.4": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.14.4.zip",
    "Forge_server_1.14.3": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.14.3.zip",
    "Forge_server_1.14.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.14.2.zip",
    "Forge_server_1.13.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.13.2.zip",
    "Forge_server_1.12.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.12.2.zip",
    "Forge_server_1.12.1": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.12.1.zip",
    "Forge_server_1.12": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.12.zip",
    "Forge_server_1.11.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.11.2.zip",
    "Forge_server_1.10.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.10.2.zip",
    "Forge_server_1.9.4": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.9.4.zip",
    "Forge_server_1.8.9": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.8.9.zip",
    "Forge_server_1.8.8": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.8.8.zip",
    "Forge_server_1.8": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.8.zip",
    "Forge_server_1.7.10": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.7.10.zip",
    "Forge_server_1.7.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.7.2.zip",
    "Forge_server_1.6.4": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.6.4.zip",
    "Forge_server_1.6.3": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.6.3.zip",
    "Forge_server_1.6.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.6.2.zip",
    "Forge_server_1.6.1": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.6.1.zip",
    "Forge_server_1.5.2": "https://gh.con.sh/?q=https://github.com/menxin123/Minecraft-server-installer/releases/download/forge/1.5.2.zip",
    # fabric部分
    "Fabric_server_1.20.4": "https://meta.fabricmc.net/v2/versions/loader/1.20.4/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.20.3": "https://meta.fabricmc.net/v2/versions/loader/1.20.3/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.20.2": "https://meta.fabricmc.net/v2/versions/loader/1.20.2/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.20.1": "https://meta.fabricmc.net/v2/versions/loader/1.20.1/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.20": "https://meta.fabricmc.net/v2/versions/loader/1.20/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.19.4": "https://meta.fabricmc.net/v2/versions/loader/1.19.4/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.19.3": "https://meta.fabricmc.net/v2/versions/loader/1.19.3/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.19.2": "https://meta.fabricmc.net/v2/versions/loader/1.19.2/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.19.1": "https://meta.fabricmc.net/v2/versions/loader/1.19.1/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.19": "https://meta.fabricmc.net/v2/versions/loader/1.19/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.18.2": "https://meta.fabricmc.net/v2/versions/loader/1.18.2/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.18.1": "https://meta.fabricmc.net/v2/versions/loader/1.18.1/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.18": "https://meta.fabricmc.net/v2/versions/loader/1.18/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.17.1": "https://meta.fabricmc.net/v2/versions/loader/1.17.1/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.17": "https://meta.fabricmc.net/v2/versions/loader/1.17/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.16.5": "https://meta.fabricmc.net/v2/versions/loader/1.16.5/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.16.4": "https://meta.fabricmc.net/v2/versions/loader/1.16.4/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.16.3": "https://meta.fabricmc.net/v2/versions/loader/1.16.3/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.16.2": "https://meta.fabricmc.net/v2/versions/loader/1.16.2/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.16.1": "https://meta.fabricmc.net/v2/versions/loader/1.16.1/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.16": "https://meta.fabricmc.net/v2/versions/loader/1.16/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.15.2": "https://meta.fabricmc.net/v2/versions/loader/1.15.2/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.15.1": "https://meta.fabricmc.net/v2/versions/loader/1.15.1/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.15": "https://meta.fabricmc.net/v2/versions/loader/1.15/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.14.4": "https://meta.fabricmc.net/v2/versions/loader/1.14.4/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.14.3": "https://meta.fabricmc.net/v2/versions/loader/1.14.3/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.14.2": "https://meta.fabricmc.net/v2/versions/loader/1.14.2/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.14.1": "https://meta.fabricmc.net/v2/versions/loader/1.14.1/0.15.3/0.11.2/server/jar",
    "Fabric_server_1.14": "https://meta.fabricmc.net/v2/versions/loader/1.14/0.15.3/0.11.2/server/jar",
    # Cat部分
    "Cat_server_1.18.2": "https://jenkins.rbqcloud.cn:30011/job/CatServer-1.18.2/lastSuccessfulBuild/artifact/projects/forge/build/libs/CatServer-1.18.2-bc64e1fc-server.jar",
    "Cat_server_1.16.5": "https://jenkins.rbqcloud.cn:30011/job/CatServer-1.16.5/lastSuccessfulBuild/artifact/projects/forge/build/libs/CatServer-1.16.5-fad62406-server.jar",
    "Cat_server_1.12.2": "https://catserver.moe/download/universal",
    # Mohist部分
    "Mohist_server_1.20.2": "https://mohistmc.com/api/v2/projects/mohist/1.20.2/builds/122/download",
    "Mohist_server_1.20.1": "https://mohistmc.com/api/v2/projects/mohist/1.20.1/builds/511/download",
    "Mohist_server_1.20": "https://mohistmc.com/api/v2/projects/mohist/1.20/builds/18/download",
    "Mohist_server_1.19.4": "https://mohistmc.com/api/v2/projects/mohist/1.19.4/builds/192/download",
    "Mohist_server_1.19.2": "https://mohistmc.com/api/v2/projects/mohist/1.19.2/builds/82/download",
    "Mohist_server_1.18.2": "https://mohistmc.com/api/v2/projects/mohist/1.18.2/builds/134/download",
    "Mohist_server_1.16.5": "https://mohistmc.com/api/v2/projects/mohist/1.16.5/builds/131/download",
    "Mohist_server_1.12.2": "https://mohistmc.com/api/v2/projects/mohist/1.12.2/builds/313/download",
    "Mohist_server_1.7.10": "https://mohistmc.com/api/v2/projects/mohist/1.7.10/builds/36/download",
    # Banner部分
    "Banner_server_1.20.1": "https://mohistmc.com/api/v2/projects/banner/1.20.1/builds/458/download",
    "Banner_server_1.20": "https://mohistmc.com/api/v2/projects/banner/1.20/builds/39/download",
    "Banner_server_1.19.4": "https://mohistmc.com/api/v2/projects/banner/1.19.4/builds/392/download",
    # Craftbukkit部分
    "Craftbukkit_server_1.20.4": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.20.4.jar",
    "Craftbukkit_server_1.20.2": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.20.2.jar",
    "Craftbukkit_server_1.20.1": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.20.1.jar",
    "Craftbukkit_server_1.19.4": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.19.4.jar",
    "Craftbukkit_server_1.19.3": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.19.3.jar",
    "Craftbukkit_server_1.19.2": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.19.2.jar",
    "Craftbukkit_server_1.19.1": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.19.1.jar",
    "Craftbukkit_server_1.19": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.19.jar",
    "Craftbukkit_server_1.18.2": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.18.2.jar",
    "Craftbukkit_server_1.18.1": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.18.1.jar",
    "Craftbukkit_server_1.18": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.18.jar",
    "Craftbukkit_server_1.17.1": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.17.1.jar",
    "Craftbukkit_server_1.17": "https://download.getbukkit.org/craftbukkit/craftbukkit-1.17.jar",
    "Craftbukkit_server_1.16.5": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.5.jar",
    "Craftbukkit_server_1.16.4": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.4.jar",
    "Craftbukkit_server_1.16.3": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.3.jar",
    "Craftbukkit_server_1.16.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.2.jar",
    "Craftbukkit_server_1.16.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.1.jar",
    "Craftbukkit_server_1.15.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.15.2.jar",
    "Craftbukkit_server_1.15.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.15.1-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.15": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.15-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.14.4": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.4-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.14.3": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.3-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.14.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.2-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.14.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.1-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.14": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.13.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.13.2.jar",
    "Craftbukkit_server_1.13.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.13.1.jar",
    "Craftbukkit_server_1.13": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.13.jar",
    "Craftbukkit_server_1.12.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.12.2.jar",
    "Craftbukkit_server_1.12.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.12.1.jar",
    "Craftbukkit_server_1.12": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.12.jar",
    "Craftbukkit_server_1.11.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.11.2.jar",
    "Craftbukkit_server_1.11.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.11.1.jar",
    "Craftbukkit_server_1.11": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.11.jar",
    "Craftbukkit_server_1.10.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.10.2-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.10": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.10-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.9.4": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.9.4-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.9.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.9.2-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.9": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.9-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.8.8": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.8-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.8.7": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.7-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.8.6": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.6-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.8.5": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.5-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.8.4": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.4-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.8.3": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.3-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.8": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8-R0.1-SNAPSHOT-latest.jar",
    "Craftbukkit_server_1.7.10": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.10-R0.1-20140808.005431-8.jar",
    "Craftbukkit_server_1.7.9": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.9-R0.2-SNAPSHOT.jar",
    "Craftbukkit_server_1.7.8": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.8-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.7.5": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.5-R0.1-20140402.020013-12.jar",
    "Craftbukkit_server_1.7.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.2-R0.4-20140216.012104-3.jar",
    "Craftbukkit_server_1.6.4": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.6.4-R2.0.jar",
    "Craftbukkit_server_1.6.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.6.2-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.6.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.6.1-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.5.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.5.2-R1.0.jar",
    "Craftbukkit_server_1.5.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.5.1-R0.2-SNAPSHOT.jar",
    "Craftbukkit_server_1.4.7": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.4.7-R1.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.4.6": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.4.6-R0.4-SNAPSHOT.jar",
    "Craftbukkit_server_1.4.5": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.4.5-R1.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.4.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.4.2-R0.3-SNAPSHOT.jar",
    "Craftbukkit_server_1.3.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.3.2-R2.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.3.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.3.1-R2.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.2.5": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.2.5-R5.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.2.4": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.2.4-R1.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.2.3": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.2.3-R0.3-SNAPSHOT.jar",
    "Craftbukkit_server_1.2.2": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.2.2-R0.1-SNAPSHOT.jar",
    "Craftbukkit_server_1.1": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.1-R5-SNAPSHOT.jar",
    "Craftubkkit_server_1.0.0": "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.0.0-SNAPSHOT.jar",
    # Spigot部分
    "Spigot_server_1.20.4": "https://download.getbukkit.org/spigot/spigot-1.20.4.jar",
    "Spigot_server_1.20.2": "https://download.getbukkit.org/spigot/spigot-1.20.2.jar",
    "Spigot_server_1.20.1": "https://download.getbukkit.org/spigot/spigot-1.20.1.jar",
    "Spigot_server_1.19.4": "https://download.getbukkit.org/spigot/spigot-1.19.4.jar",
    "Spigot_server_1.19.3": "https://download.getbukkit.org/spigot/spigot-1.19.3.jar",
    "Spigot_server_1.19.2": "https://download.getbukkit.org/spigot/spigot-1.19.2.jar",
    "Spigot_server_1.19.1": "https://download.getbukkit.org/spigot/spigot-1.19.1.jar",
    "Spigot_server_1.19": "https://download.getbukkit.org/spigot/spigot-1.19.jar",
    "Spigot_server_1.18.2": "https://download.getbukkit.org/spigot/spigot-1.18.2.jar",
    "Spigot_server_1.18.1": "https://download.getbukkit.org/spigot/spigot-1.18.1.jar",
    "Spigot_server_1.18": "https://download.getbukkit.org/spigot/spigot-1.18.jar",
    "Spigot_server_1.17.1": "https://download.getbukkit.org/spigot/spigot-1.17.1.jar",
    "Spigot_server_1.17": "https://download.getbukkit.org/spigot/spigot-1.17.1.jar",
    "Spigot_server_1.16.5": "https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar",
    "Spigot_server_1.16.4": "https://cdn.getbukkit.org/spigot/spigot-1.16.4.jar",
    "Spigot_server_1.16.3": "https://cdn.getbukkit.org/spigot/spigot-1.16.3.jar",
    "Spigot_server_1.16.2": "https://cdn.getbukkit.org/spigot/spigot-1.16.2.jar",
    "Spigot_server_1.16.1": "https://cdn.getbukkit.org/spigot/spigot-1.16.1.jar",
    "Spigot_server_1.15.2": "https://cdn.getbukkit.org/spigot/spigot-1.15.2.jar",
    "Spigot_server_1.15.1": "https://cdn.getbukkit.org/spigot/spigot-1.15.1.jar",
    "Spigot_server_1.15": "https://cdn.getbukkit.org/spigot/spigot-1.15.jar",
    "Spigot_server_1.14.4": "https://cdn.getbukkit.org/spigot/spigot-1.14.4.jar",
    "Spigot_server_1.14.3": "https://cdn.getbukkit.org/spigot/spigot-1.14.3.jar",
    "Spigot_server_1.14.2": "https://cdn.getbukkit.org/spigot/spigot-1.14.2.jar",
    "Spigot_server_1.14.1": "https://cdn.getbukkit.org/spigot/spigot-1.14.1.jar",
    "Spigot_server_1.14": "https://cdn.getbukkit.org/spigot/spigot-1.14.jar",
    "Spigot_server_1.13.2": "https://cdn.getbukkit.org/spigot/spigot-1.13.2.jar",
    "Spigot_server_1.13.1": "https://cdn.getbukkit.org/spigot/spigot-1.13.1.jar",
    "Spigot_server_1.13": "https://cdn.getbukkit.org/spigot/spigot-1.13.jar",
    "Spigot_server_1.12.2": "https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar",
    "Spigot_server_1.12.1": "https://cdn.getbukkit.org/spigot/spigot-1.12.1.jar",
    "Spigot_server_1.12": "https://cdn.getbukkit.org/spigot/spigot-1.12.jar",
    "Spigot_server_1.11.2": "https://cdn.getbukkit.org/spigot/spigot-1.11.2.jar",
    "Spigot_server_1.10.2": "https://cdn.getbukkit.org/spigot/spigot-1.10.2-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.10": "https://cdn.getbukkit.org/spigot/spigot-1.10-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.9.4": "https://cdn.getbukkit.org/spigot/spigot-1.9.4-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.8.8": "https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.8.7": "https://cdn.getbukkit.org/spigot/spigot-1.8.7-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.8.6": "https://cdn.getbukkit.org/spigot/spigot-1.8.6-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.8.5": "https://cdn.getbukkit.org/spigot/spigot-1.8.5-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.8.4": "https://cdn.getbukkit.org/spigot/spigot-1.8.4-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.8.3": "https://cdn.getbukkit.org/spigot/spigot-1.8.3-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.8": "https://cdn.getbukkit.org/spigot/spigot-1.8-R0.1-SNAPSHOT-latest.jar",
    "Spigot_server_1.7.10": "https://cdn.getbukkit.org/spigot/spigot-1.7.10-SNAPSHOT-b1657.jar",
    "Spigot_server_1.7.9": "https://cdn.getbukkit.org/spigot/spigot-1.7.9-R0.2-SNAPSHOT.jar",
    "Spigot_server_1.7.8": "https://cdn.getbukkit.org/spigot/spigot-1.7.8-R0.1-SNAPSHOT.jar",
    "Spigot_server_1.7.5": "https://cdn.getbukkit.org/spigot/spigot-1.7.5-R0.1-SNAPSHOT-1387.jar",
    "Spigot_server_1.7.2": "https://cdn.getbukkit.org/spigot/spigot-1.7.2-R0.4-SNAPSHOT-1339.jar",
    "Spigot_server_1.6.4": "https://cdn.getbukkit.org/spigot/spigot",
    "Spigot_server_1.6.2": "https://cdn.getbukkit.org/spigot/spigot-1.6.2-R1.1-SNAPSHOT.jar",
    "Spigot_server_1.5.2": "https://cdn.getbukkit.org/spigot/spigot-1.5.2-R1.1-SNAPSHOT.jar",
    "Spigot_server_1.5.1": "https://cdn.getbukkit.org/spigot/spigot-1.5.1-R0.1-SNAPSHOT.jar",
    "Spigot_server_1.4.7": "https://cdn.getbukkit.org/spigot/spigot-1.4.7-R1.1-SNAPSHOT.jar",
    "Spigot_server_1.4.6": "https://cdn.getbukkit.org/spigot/spigot-1.4.6-R0.4-SNAPSHOT.jar",
    # Paper部分
    "Paper_server_1.20.4": "https://api.papermc.io/v2/projects/paper/versions/1.20.4/builds/336/downloads/paper-1.20.4-336.jar",
    "Paper_server_1.20.2": "https://api.papermc.io/v2/projects/paper/versions/1.20.2/builds/318/downloads/paper-1.20.2-318.jar",
    "Paper_server_1.20.1": "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/196/downloads/paper-1.20.1-196.jar",
    "Paper_server_1.20": "https://api.papermc.io/v2/projects/paper/versions/1.20/builds/17/downloads/paper-1.20-17.jar",
    "Paper_server_1.19.4": "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar",
    "Paper_server_1.19.3": "https://api.papermc.io/v2/projects/paper/versions/1.19.3/builds/448/downloads/paper-1.19.3-448.jar",
    "Paper_server_1.19.2": "https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/307/downloads/paper-1.19.2-307.jar",
    "Paper_server_1.19.1": "https://api.papermc.io/v2/projects/paper/versions/1.19.1/builds/111/downloads/paper-1.19.1-111.jar",
    "Paper_server_1.19": "https://api.papermc.io/v2/projects/paper/versions/1.19/builds/81/downloads/paper-1.19-81.jar",
    "Paper_server_1.18.2": "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar",
    "Paper_server_1.18.1": "https://api.papermc.io/v2/projects/paper/versions/1.18.1/builds/216/downloads/paper-1.18.1-216.jar",
    "Paper_server_1.18": "https://api.papermc.io/v2/projects/paper/versions/1.18/builds/66/downloads/paper-1.18-66.jar",
    "Paper_server_1.17.1": "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar",
    "Paper_server_1.17": "https://api.papermc.io/v2/projects/paper/versions/1.17/builds/79/downloads/paper-1.17-79.jar",
    "Paper_server_1.16.5": "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar",
    "Paper_server_1.16.4": "https://api.papermc.io/v2/projects/paper/versions/1.16.4/builds/416/downloads/paper-1.16.4-416.jar",
    "Paper_server_1.16.3": "https://api.papermc.io/v2/projects/paper/versions/1.16.3/builds/253/downloads/paper-1.16.3-253.jar",
    "Paper_server_1.16.2": "https://api.papermc.io/v2/projects/paper/versions/1.16.2/builds/189/downloads/paper-1.16.2-189.jar",
    "Paper_server_1.16.1": "https://api.papermc.io/v2/projects/paper/versions/1.16.1/builds/138/downloads/paper-1.16.1-138.jar",
    "Paper_server_1.15.2": "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar",
    "Paper_server_1.15.1": "https://api.papermc.io/v2/projects/paper/versions/1.15.1/builds/62/downloads/paper-1.15.1-62.jar",
    "Paper_server_1.15": "https://api.papermc.io/v2/projects/paper/versions/1.15/builds/21/downloads/paper-1.15-21.jar",
    "Paper_server_1.14.4": "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar",
    "Paper_server_1.14.3": "https://api.papermc.io/v2/projects/paper/versions/1.14.3/builds/134/downloads/paper-1.14.3-134.jar",
    "Paper_server_1.14.2": "https://api.papermc.io/v2/projects/paper/versions/1.14.2/builds/107/downloads/paper-1.14.2-107.jar",
    "Paper_server_1.14.1": "https://api.papermc.io/v2/projects/paper/versions/1.14.1/builds/50/downloads/paper-1.14.1-50.jar",
    "Paper_server_1.14": "https://api.papermc.io/v2/projects/paper/versions/1.14/builds/17/downloads/paper-1.14-17.jar",
    "Paper_server_1.13.2": "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar",
    "Paper_server_1.13.1": "https://api.papermc.io/v2/projects/paper/versions/1.13.1/builds/386/downloads/paper-1.13.1-386.jar",
    "Paper_server_1.13": "https://api.papermc.io/v2/projects/paper/versions/1.13/builds/173/downloads/paper-1.13-173.jar",
    "Paper_server_1.12.2": "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar",
    "Paper_server_1.12.1": "https://api.papermc.io/v2/projects/paper/versions/1.12.1/builds/1204/downloads/paper-1.12.1-1204.jar",
    "Paper_server_1.12": "https://api.papermc.io/v2/projects/paper/versions/1.12/builds/1169/downloads/paper-1.12-1169.jar",
    "Paper_server_1.11.2": "https://api.papermc.io/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar",
    "Paper_server_1.10.2": "https://api.papermc.io/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar",
    "Paper_server_1.9.4": "https://api.papermc.io/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar",
    "Paper_server_1.8.8": "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar",
    # Waterfall部分
    "Waterfall_server_1.20": "https://api.papermc.io/v2/projects/waterfall/versions/1.20/builds/559/downloads/waterfall-1.20-559.jar",
    "Waterfall_server_1.19": "https://api.papermc.io/v2/projects/waterfall/versions/1.19/builds/535/downloads/waterfall-1.19-535.jar",
    "Waterfall_server_1.18": "https://api.papermc.io/v2/projects/waterfall/versions/1.18/builds/488/downloads/waterfall-1.18-488.jar",
    "Waterfall_server_1.17": "https://api.papermc.io/v2/projects/waterfall/versions/1.17/builds/454/downloads/waterfall-1.17-454.jar",
    "Waterfall_server_1.16": "https://api.papermc.io/v2/projects/waterfall/versions/1.16/builds/431/downloads/waterfall-1.16-431.jar",
    "Waterfall_server_1.15": "https://api.papermc.io/v2/projects/waterfall/versions/1.15/builds/350/downloads/waterfall-1.15-350.jar",
    "Waterfall_server_1.14": "https://api.papermc.io/v2/projects/waterfall/versions/1.14/builds/301/downloads/waterfall-1.14-301.jar",
    "Waterfall_server_1.13": "https://api.papermc.io/v2/projects/waterfall/versions/1.13/builds/276/downloads/waterfall-1.13-276.jar",
    "Waterfall_server_1.12": "https://api.papermc.io/v2/projects/waterfall/versions/1.12/builds/185/downloads/waterfall-1.12-185.jar",
    "Waterfall_server_1.11": "https://api.papermc.io/v2/projects/waterfall/versions/1.11/builds/108/downloads/waterfall-1.11-108.jar",
    # java部分
    "java-lite-v1": java_lite_v1_url,
    "java-lite-v2": java_lite_v2_url,
    "java-lite-v3": java_lite_v3_url
}

# 必备文件的下载链接
essential_files_urls = {
    "eula": "https://gitee.com/a-clear-water/cs/releases/download/run/eula.txt",
    "run.bat": "https://gitee.com/a-clear-water/cs/releases/download/run/run.bat",
    "run.sh": "https://gitee.com/a-clear-water/cs/releases/download/run/run.sh"
}


def get_script_directory():
    return os.path.dirname(os.path.realpath(__file__))

# 检查并创建服务器目录
def get_server_directory():
    base_name = "server"
    base_dir = os.path.join(get_script_directory(), base_name)
    counter = 1
    while os.path.exists(base_dir):
        base_dir = os.path.join(get_script_directory(), f"{base_name}{counter}")
        counter += 1
    os.makedirs(base_dir)
    return base_dir


# 提示用户输入下载目录
def prompt_for_download_directory():
    user_input_directory = input("请输入下载目录（留空则使用默认目录）: ").strip()
    if user_input_directory and not os.path.exists(user_input_directory):
        print("您输入的目录不存在，请重新输入。")
        return prompt_for_download_directory()
    return user_input_directory if user_input_directory else get_server_directory()



# 创建下载函数
# 根据URL获取文件名
def get_filename_from_cd_or_url(response, url):
    cd = response.headers.get('content-disposition')
    if cd:
        fname = re.findall('filename="(.+)"', cd)
        if len(fname) == 1:
            return unquote(fname[0])
    return url.split('/')[-1]


# 创建下载并解压函数
def make_download_and_extract_function(url):
    def download_and_extract(download_directory):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                filename = get_filename_from_cd_or_url(response, url)
                destination = os.path.join(download_directory, filename)

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

                if destination.endswith('.zip'):
                    with zipfile.ZipFile(destination, 'r') as zip_ref:
                        zip_ref.extractall(download_directory)
                    print(f"已解压: {destination}")
                elif destination.endswith('.tar.gz'):
                    with tarfile.open(destination, 'r:gz') as tar_ref:
                        tar_ref.extractall(download_directory)
                    print(f"已解压: {destination}")

                if destination.endswith('.zip') or destination.endswith('.tar.gz'):
                    os.remove(destination)
                    print(f"已删除压缩文件: {destination}")

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
                shutil.rmtree(download_directory)
                print(f"已删除下载目录: {download_directory}")
        except requests.exceptions.RequestException as e:
            clear_screen()
            shutil.rmtree(download_directory)
            print(f"已删除下载目录: {download_directory}")
            print("下载失败，可能是网络问题，请重试。")
            input("按下任意键继续...")
            clear_screen()
            return main_menu()

    return download_and_extract


# 创建下载函数的字典
download_functions = {version: make_download_and_extract_function(url) for version, url in download_urls.items()}


def download_files(download_directory, versions, download_essentials=True):
    # 下载版本文件
    for version in versions:
        if version in download_functions:
            download_functions[version](download_directory)
        else:
            print(f"Version {version} not found in download functions.")

    # 如果需要，下载必备文件
    if download_essentials:
        for essential_file in essential_files_urls.keys():
            if essential_file in download_functions:
                download_functions[essential_file](download_directory)
            else:
                print(f"Essential file {essential_file} not found in download functions.")

    # 所有下载完成后退出程序
    exit_program()


essential_download_functions = {name: make_download_and_extract_function(url) for name, url in
                                essential_files_urls.items()}
download_functions.update(essential_download_functions)


# 函数生成器，用于创建 item_functions1 中的选项函数
def create_option_function(versions):
    def option_function():
        download_directory = prompt_for_download_directory()

        # 检查版本数据是否为列表（默认下载必备文件）或字典（可能包含 download_essentials 键）
        if isinstance(versions, list):
            files_list = versions
            download_essentials = True
        elif isinstance(versions, dict):
            files_list = versions.get("files", [])
            download_essentials = versions.get("download_essentials", True)
        else:
            print("Invalid version data format.")
            return

        download_files(download_directory, files_list, download_essentials)
        exit_program()

    return option_function



def download_version_files(version, version_data):
    download_directory = prompt_for_download_directory()

    # 初始化变量以避免引用前未赋值的警告
    files_list = []
    download_essentials = True

    # 检查版本数据是否为列表（默认下载必备文件）或字典（可能包含 download_essentials 键）
    if isinstance(version_data, list):
        files_list = version_data
    elif isinstance(version_data, dict):
        files_list = version_data.get("files", [])
        download_essentials = version_data.get("download_essentials", True)

    # 调用 download_files 函数进行下载
    download_files(download_directory, files_list, download_essentials)


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
        "1.14.1": ["Minecraft_server_1.14.1", "java-lite-v3"],
        "1.14": ["Minecraft_server_1.14", "java-lite-v3"],
        "1.13.2": ["Minecraft_server_1.13.2", "java-lite-v3"],
        "1.13.1": ["Minecraft_server_1.13.1", "java-lite-v3"],
        "1.13": ["Minecraft_server_1.13", "java-lite-v3"],
        "1.12.2": ["Minecraft_server_1.12.2", "java-lite-v3"],
        "1.12.1": ["Minecraft_server_1.12.1", "java-lite-v3"],
        "1.12": ["Minecraft_server_1.12", "java-lite-v3"],
        "1.11.2": ["Minecraft_server_1.11.2", "java-lite-v3"],
        "1.11.1": ["Minecraft_server_1.11.1", "java-lite-v3"],
        "1.11": ["Minecraft_server_1.11", "java-lite-v3"],
        "1.10.2": ["Minecraft_server_1.10.2", "java-lite-v3"],
        "1.10.1": ["Minecraft_server_1.10.1", "java-lite-v3"],
        "1.10": ["Minecraft_server_1.10", "java-lite-v3"],
        "1.9.4": ["Minecraft_server_1.9.4", "java-lite-v3"],
        "1.9.3": ["Minecraft_server_1.9.3", "java-lite-v3"],
        "1.9.2": ["Minecraft_server_1.9.2", "java-lite-v3"],
        "1.9.1": ["Minecraft_server_1.9.1", "java-lite-v3"],
        "1.9": ["Minecraft_server_1.9", "java-lite-v3"],
        "1.8.9": ["Minecraft_server_1.8.9", "java-lite-v3"],
        "1.8.8": ["Minecraft_server_1.8.8", "java-lite-v3"],
        "1.8.7": ["Minecraft_server_1.8.7", "java-lite-v3"],
        "1.8.6": ["Minecraft_server_1.8.6", "java-lite-v3"],
        "1.8.5": ["Minecraft_server_1.8.5", "java-lite-v3"],
        "1.8.4": ["Minecraft_server_1.8.4", "java-lite-v3"],
        "1.8.3": ["Minecraft_server_1.8.3", "java-lite-v3"],
        "1.8.2": ["Minecraft_server_1.8.2", "java-lite-v3"],
        "1.8.1": ["Minecraft_server_1.8.1", "java-lite-v3"],
        "1.8": ["Minecraft_server_1.8", "java-lite-v3"],
        "1.7.10": ["Minecraft_server_1.7.10", "java-lite-v3"],
        "1.7.9": ["Minecraft_server_1.7.9", "java-lite-v3"],
        "1.7.8": ["Minecraft_server_1.7.8", "java-lite-v3"],
        "1.7.7": ["Minecraft_server_1.7.7", "java-lite-v3"],
        "1.7.6": ["Minecraft_server_1.7.6", "java-lite-v3"],
        "1.7.5": ["Minecraft_server_1.7.5", "java-lite-v3"],
        "1.7.4": ["Minecraft_server_1.7.4", "java-lite-v3"],
        "1.7.2": ["Minecraft_server_1.7.2", "java-lite-v3"],
        "1.6.4": ["Minecraft_server_1.6.4", "java-lite-v3"],
        "1.6.2": ["Minecraft_server_1.6.2", "java-lite-v3"],
        "1.6.1": ["Minecraft_server_1.6.1", "java-lite-v3"],
        "1.5.2": ["Minecraft_server_1.5.2", "java-lite-v3"],
        "1.5.1": ["Minecraft_server_1.5.1", "java-lite-v3"],
        "1.5": ["Minecraft_server_1.5", "java-lite-v3"],
        "1.4.7": ["Minecraft_server_1.4.7", "java-lite-v3"],
        "1.4.6": ["Minecraft_server_1.4.6", "java-lite-v3"],
        "1.4.5": ["Minecraft_server_1.4.5", "java-lite-v3"],
        "1.4.4": ["Minecraft_server_1.4.4", "java-lite-v3"],
        "1.4.2": ["Minecraft_server_1.4.2", "java-lite-v3"],
        "1.3.2": ["Minecraft_server_1.3.2", "java-lite-v3"],
        "1.3.1": ["Minecraft_server_1.3.1", "java-lite-v3"],
        "1.2.5": ["Minecraft_server_1.2.5", "java-lite-v3"],
        "1.2.4": ["Minecraft_server_1.2.4", "java-lite-v3"],
        "1.2.3": ["Minecraft_server_1.2.3", "java-lite-v3"],
        "1.2.2": ["Minecraft_server_1.2.2", "java-lite-v3"],
        "1.2.1": ["Minecraft_server_1.2.1", "java-lite-v3"],
        "1.1": ["Minecraft_server_1.1", "java-lite-v3"],
        "1.0.1": ["Minecraft_server_1.0.1", "java-lite-v3"],
        "1.0.0": ["Minecraft_server_1.0.0", "java-lite-v3"],
    },
    "Forge_server": {
        "1.20.4": ["Forge_server_1.20.4", "java-lite-v1"],
        "1.20.3": ["Forge_server_1.20.3", "java-lite-v1"],
        "1.20.2": {
            "files": ["Forge_server_1.20.2", "java-lite-v1"],
            "download_essentials": False
        },
        "1.20.1": {
            "files": ["Forge_server_1.20.1", "java-lite-v1"],
            "download_essentials": False
        },
        "1.20": {
            "files": ["Forge_server_1.20", "java-lite-v1"],
            "download_essentials": False
        },
        "1.19.4": {
            "files": ["Forge_server_1.19.4", "java-lite-v1"],
            "download_essentials": False
        },
        "1.19.3": {
            "files": ["Forge_server_1.19.3", "java-lite-v1"],
            "download_essentials": False
        },
        "1.19.2": {
            "files": ["Forge_server_1.19.2", "java-lite-v1"],
            "download_essentials": False
        },
        "1.19.1": {
            "files": ["Forge_server_1.19.1", "java-lite-v1"],
            "download_essentials": False
        },
        "1.19": {
            "files": ["Forge_server_1.19", "java-lite-v1"],
            "download_essentials": False
        },
        "1.18.2": {
            "files": ["Forge_server_1.18.2", "java-lite-v1"],
            "download_essentials": False
        },
        "1.18.1": {
            "files": ["Forge_server_1.18.1", "java-lite-v1"],
            "download_essentials": False
        },
        "1.18": {
            "files": ["Forge_server_1.18", "java-lite-v1"],
            "download_essentials": False
        },
        "1.17.1": {
            "files": ["Forge_server_1.17.1", "java-lite-v2"],
            "download_essentials": False
        },
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
        "1.8.9": ["Forge_server_1.8.9", "java-lite-v3"],
        "1.8.8": ["Forge_server_1.8.8", "java-lite-v3"],
        "1.8": ["Forge_server_1.8", "java-lite-v3"],
        "1.7.10": ["Forge_server_1.7.10", "java-lite-v3"],
        "1.7.2": ["Forge_server_1.7.2", "java-lite-v3"],
        "1.6.4": ["Forge_server_1.6.4", "java-lite-v3"],
        "1.6.3": ["Forge_server_1.6.3", "java-lite-v3"],
        "1.6.2": ["Forge_server_1.6.2", "java-lite-v3"],
        "1.6.1": ["Forge_server_1.6.1", "java-lite-v3"],
        "1.5.2": ["Forge_server_1.5.2", "java-lite-v3"],
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
        "1.16": ["Fabric_server_1.16", "java-lite-v3"],
        "1.15.2": ["Fabric_server_1.15.2", "java-lite-v3"],
        "1.15.1": ["Fabric_server_1.15.1", "java-lite-v3"],
        "1.15": ["Fabric_server_1.15", "java-lite-v3"],
        "1.14.4": ["Fabric_server_1.14.4", "java-lite-v3"],
        "1.14.3": ["Fabric_server_1.14.3", "java-lite-v3"],
        "1.14.2": ["Fabric_server_1.14.2", "java-lite-v3"],
        "1.14.1": ["Fabric_server_1.14.1", "java-lite-v3"],
        "1.14": ["Fabric_server_1.14", "java-lite-v3"]
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
        "1.11": ["Paper_server_1.11", "java-lite-v3"]
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
                    version_info = version_files_mapping[title].get(selected_version)
                    # 如果版本信息不是字典，则创建一个包含文件列表的字典
                    if not isinstance(version_info, dict):
                        version_info = {"files": version_info}
                    # 调用下载函数，传入版本和版本信息
                    download_version_files(selected_version, version_info)
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
            clear_screen()
            print("无效的选择，请重新输入。")


statement()
Basic_tutorials()
clear_screen()
# 调用主菜单函数
if __name__ == "__main__":
    main_menu()
