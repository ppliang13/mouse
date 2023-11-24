import pywifi
from pywifi import const
import time
import timeit



class MyWifi:
    def __init__(self):
        # 创建wifi操作对象
        self.wifi = pywifi.PyWiFi()
        # 创建连接接口
        self.iface = self.wifi.interfaces()[0]
        # wifi配置信息
        self.profile = pywifi.Profile()
        self.__default_profile()
        # 附近wifi
        self.wifi_list = self.show_all_wifi()

    def update_pwd(self, ssid, password):
        self.profile.ssid = ssid
        self.profile.key = password

    def __default_profile(self):
        self.profile.auth = const.AUTH_ALG_OPEN  # 开放认证
        self.profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WPA2PSK 加密
        self.profile.cipher = const.CIPHER_TYPE_CCMP  # CCMP 加密
        self.iface.remove_all_network_profiles()  # 移除所有 WiFi 配置文件
        return self.profile

    def show_all_wifi(self):
        self.iface.scan()  # 扫描可用的 WiFi 网络
        time.sleep(2)  # 等待扫描完成
        scan_results = self.iface.scan_results()
        print("附近的WiFi网络：")
        for result in scan_results:
            print(f"SSID: {result.ssid}, 信号强度: {result.signal}")

        self.wifi_list = scan_results
        return scan_results

    def check_wifi_connect(self, name, password):
        self.update_pwd(name, password)
        tmp_profile = self.iface.add_network_profile(self.profile)
        self.iface.connect(tmp_profile)
        return self.iface.status() == const.IFACE_CONNECTED



