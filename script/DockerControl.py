import subprocess

# やられ環境コンテナの個別制御補助スクリプト
'''
以下ポートを使用
実行環境にポートフォワーディングの設定が必要
docker container間での通信の場合は問題ない
IP : 172.17.0.0 /24

badstore  : 8030
bwapp     : 8040
dvwa      : 8050
juiceshop : 8060

'''

'''
https://qiita.com/prograti/items/00cba4ea0ab7d45cf61e

# Dockerfileからimageを作成(指定pathにkali用Dockerfileが必要)
docker build -t my_kali . /bin/zsh

# imageからcontainerを作成
docker run --name my_kali -itd my_kali

'''

class DockerCctl:
    # kali control
    build_kali_image = "docker build -t my_kali ./kali/" #指定のpathにDockerfileが存在すること確認
    build_kali_container = "docker run --name my_kali -itd my_kali"
    start_kali = "docker start my_kali"
    access_kali = "docker exec -it my_kali bash"
    stop_kali = "docker stop my_kali"
    # build cmd
    build_badstore = "docker run --name single_badstore -d -p 8030:80 jvhoof/badstore-docker"
    build_bwapp = "docker run --name single_bwapp -d -p 8040:80 raesene/bwapp"
    build_dvwa = "docker run --name single_dvwa -d -p 8050:80 vulnerables/web-dvwa"
    build_juiceshop = "docker run --name single_juiceshop -d -p 8060:3000 bkimminich/juice-shop"
    build_msf2 = "docker run --name single_msf2 -itd tleemcjr/metasploitable2"
    # start cmd
    start_badstore = "docker start single_badstore"
    start_bwapp = "docker start single_bwapp"
    start_dvwa = "docker start single_dvwa"
    start_juiceshop = "docker start single_juiceshop"
    start_msf2 = "docker start single_msf2"
    # stop cmd
    stop_badstore = "docker stop single_badstore"
    stop_bwapp = "docker stop single_bwapp"
    stop_dvwa = "docker stop single_dvwa"
    stop_juiceshop = "docker stop single_juiceshop"
    stop_msf2 = "docker stop single_msf2"
    # other cmd
    stop_all = "docker stop $(docker ps -q)" #これやるとmy_kaliも一緒にstopさせてしまう
    show_run = "docker ps"

    menu_msg = """
=== Docker Control Select menu ===
[Kali container control]
[k1]  : Image Building kali
[k2]  : Container Building kai
[k3]  : Container Starting kali
[k4]  : Container access kali
[k5]  : Container Stoping kali

[All build container]
[1]   : Container building
# everything is built 
# (badstore, bwapp, dvwa, juiceshop, metasploitable2)

[Start a container]
[2]   : Container Starting badstore
[3]   : Container Starting bwapp
[4]   : Container Starting dvwa
[5]   : Container Starting juiceshop
[6]   : Container Starting metasploitable2

[Stop a container]
[7]   : Container Stoping badstore
[8]   : Container Stoping bwapp
[9]   : Container Stoping dvwa
[10]  : Container Stoping juiceshop
[11]  : Container Stoping metasploitable2

[Others]
[show]: show running container
[all] : all container stop
[q]   : quit

==============================
"""

    def run(self):
        print(self.menu_msg)
        while True:
            print("[m] : Redisplay menu")
            select_num = input('Please enter the menu number : ')
            if select_num == 'k1':
                subprocess.run(self.build_kali_image,shell=True)
                continue
            if select_num == 'k2':
                subprocess.run(self.build_kali_container,shell=True)
                continue
            if select_num == 'k3':
                subprocess.run(self.start_kali,shell=True)
                print('Run "KaliIn" or "docker container exec -it my_kali zsh" command to access the container.')
                continue
            if select_num == 'k4':
                subprocess.run(self.access_kali,shell=True)
                continue
            if select_num == 'k5':
                subprocess.run(self.stop_kali,shell=True)
                continue
            if select_num == '1':
                # build all containers
                subprocess.run(self.build_badstore,shell=True)
                subprocess.run(self.build_bwapp,shell=True)
                subprocess.run(self.build_dvwa,shell=True)
                subprocess.run(self.build_juiceshop,shell=True)
                subprocess.run(self.build_msf2,shell=True)
                continue
            if select_num == '2':
                subprocess.run(self.start_badstore,shell=True)
                continue
            if select_num == '3':
                subprocess.run(self.start_bwapp,shell=True)
                continue
            if select_num == '4':
                subprocess.run(self.start_dvwa,shell=True)
                continue
            if select_num == '5':
                subprocess.run(self.start_juiceshop,shell=True)
                continue
            if select_num == '6':
                subprocess.run(self.start_msf2,shell=True)
                continue
            if select_num == '7':
                subprocess.run(self.stop_badstore,shell=True)
                continue
            if select_num == '8':
                subprocess.run(self.stop_bwapp,shell=True)
                continue
            if select_num == '9':
                subprocess.run(self.stop_dvwa,shell=True)
                continue
            if select_num == '10':
                subprocess.run(self.stop_juiceshop,shell=True)
                continue
            if select_num == '11':
                subprocess.run(self.stop_msf2,shell=True)
                continue
            if select_num == 'show':
                subprocess.run(self.show_run,shell=True)
                continue
            if select_num == 'all':
                subprocess.run(self.stop_all,shell=True)
                continue
            if select_num == 'm':
                print(self.menu_msg)
                continue
            if select_num == 'q':
                print('Exited from processing.')
                break
            else:
                print("Please enter agein.")                
        print('All processing is completed.')

if __name__ == "__main__":
    DockerCctl = DockerCctl()
    DockerCctl.run()
