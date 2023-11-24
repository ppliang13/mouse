import pywifi
from pywifi import const


def connect_to_wifi(iface, wifi_ssid, wifi_password):
    profile = pywifi.Profile()
    profile.ssid = wifi_ssid
    profile.auth = const.AUTH_ALG_OPEN  # 开放认证
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WPA2PSK加密
    profile.cipher = const.CIPHER_TYPE_CCMP  # CCMP加密
    profile.key = wifi_password

    iface.remove_all_network_profiles()  # 移除所有WiFi配置文件
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    if iface.status() == const.IFACE_CONNECTED:
        print("WiFi连接成功！")
    else:
        print("WiFi连接失败！")
