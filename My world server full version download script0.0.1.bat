:menu
@echo off
@title Server-One-Click-Install-Script-0.0.1
@cls
@color cf
@echo.
@echo =================��ѡ������=================
@echo 1.forge
@echo 2.fabric
@echo 3.catserver
@echo 4.mo
@echo =============================================
@set/p a=ѡ��������汾,��r����ѡ������,v�˳��˽ű�
if "%a%" == 1 goto :1
if "%a%" == r goto :menu
if "%a%" == v goto :exit 

:1
@cls
@echo forge������б�:
@echo 1:   "1.19ϵ��---1.13ϵ��"
@echo 2:   "1.12ϵ��---1.16ϵ��"
@set/p a=��ѡ��������汾��Χ
if "%a%" == 1 goto :1.19ϵ��---1.13ϵ��
if "%a%" == 1 goto :1.12ϵ��---1.16ϵ��

:1.19ϵ��---1.13ϵ��
@cls
@echo 1:   "1.19"
@echo 2:   "1.18"
@echo 3:   "1.17"
@echo 4:   "1.16"
@echo 5:   "1.15"
@echo 6:   "1.14"
@echo 7:   "1.13"
@set/p a=��ѡ��������汾��Χ
if "%a%" == 1 goto :1.19
if "%a%" == 2 goto :1.18
if "%a%" == 3 goto :1.17
if "%a%" == 4 goto :1.16
if "%a%" == 5 goto :1.15
if "%a%" == 6 goto :1.14
if "%a%" == 7 goto :1.13



:1.19
@cls
@echo 1:   "1.19.4"
@echo 2:   "1.19.3"
@echo 3:   "1.19.2"
@echo 4:   "1.19.1"
@echo 5:   "1.19"
@set/p a=��ѡ��������汾
if "%a%" ==1 goto 1.19.4
if "%a%" ==2 goto 1.19.3
if "%a%" ==3 goto 1.19.2
if "%a%" ==4 goto 1.19.1
if "%a%" ==5 goto 1.19
@set/p a=ѡ�����

:1.19.4
@cls
@echo ��ʼ�����ļ�....
@certutil -urlcache -split -f https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cs/1.19.4-forge-server.zip
@echo �������,��ѹ������ѹ����,˫��run.bat����
@set/p a=�������Դ�java,������������׼��



:1.19.3
@cls
@echo ��ʼ�����ļ�....
@certutil -urlcache -split -f https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cs/1.19.3-forge-server.zip
@echo �������,��ѹ������ѹ����,˫��run.bat����
@set/p a=�������Դ�java,������������׼��



:1.19.2
@cls
@echo ��ʼ�����ļ�....
@certutil -urlcache -split -f https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cs/1.19.2-forge-server.zip
@echo �������,��ѹ������ѹ����,˫��run.bat����
@set/p a=�������Դ�java,������������׼��



:1.19.1
@cls
@echo ��ʼ�����ļ�....
@certutil -urlcache -split -f https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cs/1.19.1-forge-server.zip
@echo �������,��ѹ������ѹ����,˫��run.bat����
@set/p a=�������Դ�java,������������׼��



:1.19
@cls
@echo ��ʼ�����ļ�....
@certutil -urlcache -split -f https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cs/1.19-forge-server.zip
@echo �������,��ѹ������ѹ����,˫��run.bat����
@set/p a=�������Դ�java,������������׼��



:1.18
@cls
@echo 1:   "1.18.2"
@echo 2:   "1.18.1"
@echo 3:   "1.18"
@set/p a=��ѡ��������汾










:1.12ϵ��---1.16ϵ��
@echo 1:   "1.12"
@echo 2:   "1.11"
@echo 3:   "1.10"
@echo 4:   "1.9"
@echo 5:   "1.8"
@echo 6:   "1.7"
@echo 7:   "1.6"
@set/p a=��ѡ��������汾��Χ












@echo ��ʼ�����ļ�....
@certutil -urlcache -split -f https://github.com/menxin123/Minecraft-server-one-click-install-script/releases/download/cs/1.12.2-forge-server.zip
@echo �������,��ѹ������ѹ����,˫��run.bat����
@echo �������Դ�java,������������׼��
@pause


:menu



:exit