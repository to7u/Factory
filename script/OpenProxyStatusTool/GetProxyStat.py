from ping3 import ping, verbose_ping
import requests
import json
from re import sub
import subprocess
import csv

'''
公開プロキシサーバーの生存確認とリスト生成スクリプト
1.対象リストの読み込み
CSV
国名コード,IP,port

2.何らかの疎通コマンド実行
応答、速度
マルチスレッドで実行したい

3.activeサーバーをリスト出力
'''

class GetProxyStat:
    
    # 対象ipから情報を入手するmethod
    def http_req(self,ip):
        req_url = "http://ipinfo.io/" + ip
        response = requests.get(req_url)
        country = response.json().get('country', '')
        region = response.json().get('region', '')
        result = []

        print(response.json())

        # DEBUG
        #print(country)
        #print(region)

        result.append([ip, country, region])
        print(result)

        return result

    # ncコマンドによるportスキャンで対象の確認を行うmethod
    def use_nc(self):      
        csv_file = open("./ProxyListAnonymous.csv", "r", encoding="ms932", errors="", newline="" )
        #リスト形式
        file_list = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        
        #csv_header = ['IP','PORT']
        csv_body = []
        
        for row in file_list:
            target_ip = row[0]
            target_port = row[1]
            get_port = f"nc -vz {target_ip} {target_port}"
            #get_port_result = ""
            
            # ping3 mod 使用パターン
            #print(ping(f"{target_ip}:{target_port}"))
            print("==============")
            try:
                get_port_result = subprocess.run(get_port, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1)
                if 'succeeded' in str(get_port_result):
                    print("target_port : " + target_port)
                    #subprocess.run(get_cuntry, shell=True)
                    target_info = self.http_req(target_ip)
                    csv_body.append(target_info)
            except:
                print("target not found...")
            print("==============")

        with open('./ProxyListActive.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(csv_body[0])
            writer.writerows(csv_body[1])
            writer.writerows(csv_body[2])
        f.close()

    # pingコマンドにて疎通確認を行うmethod
    def use_ping(self):
        csv_file = open("./ProxyListAnonymous.csv", "r", encoding="ms932", errors="", newline="" )
        #リスト形式
        file_list = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

        #csv_header = ['IP','PORT']
        csv_body = []

        for row in file_list:
            target_ip = row[0]
            target_port = row[1]
            #get_cuntry = f"curl -s ipinfo.io/{target_ip}"

            print("==============")
            try:
                # ping3 mod 使用パターン
                get_ping = ping(f"{target_ip}")
                if str(get_ping) != "None":
                    print(get_ping)
                    print("target_port : " + target_port)
                    #subprocess.run(get_cuntry, shell=True)
                    target_info = self.http_req(target_ip)
                    #print(target_info)
                    csv_body.append(target_info)
                else:
                    print("target not found...")
            except:
                print("target not found...")
            print("==============")
        
        with open('./ProxyListActive.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(csv_body[0])
            writer.writerows(csv_body[1])
            writer.writerows(csv_body[2])
        f.close()
    
    def run(self):
        #self.use_nc()
        self.use_ping()
        #self.http_req("43.154.216.109")


if __name__ == "__main__":
    com_proxt = GetProxyStat()
    com_proxt.run()