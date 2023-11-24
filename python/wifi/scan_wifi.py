import pywifi
from pywifi import const
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # 获取第一个 WiFi 接口
    iface.scan()  # 扫描可用的 WiFi 网络
    time.sleep(2)  # 等待扫描完成

    scan_results = iface.scan_results()

    print("附近的WiFi网络：")
    for result in scan_results:
        print(f"SSID: {result.ssid}, 信号强度: {result.signal}")

    return scan_results

def connect_to_wifi(iface, wifi, wifi_password):
    profile = pywifi.Profile()
    profile.ssid = wifi.ssid
    profile.auth = const.AUTH_ALG_OPEN  # 开放认证
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WPA2PSK 加密
    profile.cipher = const.CIPHER_TYPE_CCMP  # CCMP 加密
    profile.key = wifi_password

    iface.remove_all_network_profiles()  # 移除所有 WiFi 配置文件
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)

    time.sleep(5)  # 等待连接完成
    return iface.status() == const.IFACE_CONNECTED

# 扫描 WiFi
wifi_list = scan_wifi()
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]


# 选择一个 WiFi 进行连接
if wifi_list:
    selected_wifi = None
    for wifi in wifi_list:
        if wifi.ssid == 'ppliang':
            selected_wifi = wifi
            break

    if selected_wifi:
        wifi_password = "psl202011"  # 替换为实际的 WiFi 密码

        # 连接 WiFi
        if connect_to_wifi(iface, selected_wifi, wifi_password):
            print("WiFi 连接成功！")
        else:
            print("WiFi 连接失败！")
    else:
        print("未找到目标 WiFi 网络 ('ppliang')")
else:
    print("未发现任何 WiFi 网络")
