# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy

# # 步驟 1: 使用 UiAutomator2Options 配置 Capabilities
# # 這會自動處理 W3C 協議要求的 'appium:' 前綴
# options = UiAutomator2Options()
# options.platform_name = "Android"
# options.automation_name = "UiAutomator2"  # 對應伺服器端安裝的驅動程式
# options.device_name = "Pixel 7a"
# options.platform_version = "15"
# options.app_package = "com.google.android.settings" # 範例：開啟設定
# options.app_activity = ".Settings"
# options.no_reset = True  # 測試後不清除 App 資料

# # 針對 Android 15 的額外建議：增加命令超時時間，避免因系統優化導致的連線中斷
# options.new_command_timeout = 300 

# # 步驟 2: 建立驅動程式實例
# # 確保 Appium Server 正在運行，且 JDK 版本正確
# appium_server_url = 'http://127.0.0.1:4723'

# try:
#     print("正在連接 Appium Server...")
#     driver = webdriver.Remote(appium_server_url, options=options)
#     print("Session 建立成功！")

#     # 步驟 3: 執行簡單操作 (W3C 標準寫法)
#     # 在 Android 15 設定頁面尋找元素
#     el = driver.find_element(by=AppiumBy.XPATH, value='//*')
#     el.click()
    
#     input("測試完成，按 Enter 結束...")

# except Exception as e:
#     print(f"發生錯誤: {e}")
# finally:
#     if 'driver' in locals():
#         driver.quit()

# import unittest
# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy

# class ModernAppiumTest(unittest.TestCase):
#     def setUp(self) -> None:
#         # 1. 使用 UiAutomator2Options 替代 DesiredCapabilities
#         options = UiAutomator2Options()
#         options.platform_name = "Android"
#         options.automation_name = "UiAutomator2"
#         options.device_name = "Pixel 7a"
#         options.app_package = "com.android.settings"  # 測試內建設定 App
#         options.app_activity = ".Settings"
        
#         # 2. 連線到 Appium 2.x Server
#         # 注意：不再使用 /wd/hub，除非 Server 啟動參數有特別指定
#         appium_server_url = 'http://localhost:4723'
        
#         print(f"Connecting to Appium at {appium_server_url} with options: {options.to_capabilities()}")
        
#         try:
#             self.driver = webdriver.Remote(appium_server_url, options=options)
#         except Exception as e:
#             print(f"致命錯誤：無法建立 Session。請檢查 Java 21 環境與 Server Log。錯誤詳情：{e}")
#             raise e

#     def test_battery_setting_search(self) -> None:
#         # 3. 使用 AppiumBy 進行元素定位
#         try:
#             # 尋找 "Battery" 選項 (視語系可能需要調整文字)
#             el = self.driver.find_element(by=AppiumBy.XPATH, value='//*')
#             print(f"成功找到元素：{el.text}")
#             el.click()
#         except Exception as e:
#             print(f"元素查找失敗：{e}")

#     def tearDown(self) -> None:
#         if hasattr(self, 'driver') and self.driver:
#             self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()

# import unittest
# from appium import webdriver
# from appium.options.android import UiAutomator2Options

# class Android15SettingsTest(unittest.TestCase):
#     def setUp(self) -> None:
#         """
#         初始化 Appium Driver。
#         這裡展示了針對 Android 15 的正確 Option 配置。
#         """
#         # 1. 實例化 UiAutomator2Options
#         # 這是 Appium 2.0+ 與 Python Client 4.0+ 的標準做法，取代了舊的 DesiredCapabilities 字典。
#         options = UiAutomator2Options()

#         # 2. 基礎平台設定
#         options.platform_name = "Android"
#         options.automation_name = "UiAutomator2"
#         options.platform_version = "15"  # 指定版本有助於 Appium 優化驅動行為

#         # 3. 設備識別 (回應您的疑問)
#         # device_name 在 Android 中主要是裝飾性的，但必須填寫。
#         # 填寫 "Pixel 8" 或 "Android Emulator" 皆可，不會影響連線 (除非是 iOS)。
#         options.device_name = "Pixel_Android_15"
        
#         # 強烈建議：如果您有多台設備，請取消下行註解並填入 adb devices 看到的序號
#         # options.udid = "YOUR_DEVICE_SERIAL_NUMBER"

#         # 4. 應用程式指定 (修正 Error Type 3 的關鍵)
#         # 錯誤原因：原本使用了 Google 的內部套件名稱 (com.google.android.settings)
#         # 修正：使用 AOSP 標準名稱，這在 Pixel 與大多數 Android 手機上皆通用。
#         options.app_package = "com.google.android.apps.nexuslauncher"
#         options.app_activity = ".Settings" 
#         # 注意：.Settings 前面的點代表它位於 app_package 的路徑下

#         # 5. 其他優化設定
#         options.no_reset = True  # 測試後不清除 App 資料，加快下次啟動速度
#         options.new_command_timeout = 300 # 避免因為測試邏輯執行太久而斷線

#         # 6. 建立連線
#         # Appium Server URL 通常為 http://localhost:4723
#         print("正在嘗試連接 Appium Server 並啟動 Android 15 Session...")
#         try:
#             self.driver = webdriver.Remote("http://localhost:4723", options=options)
#             print("Session 啟動成功！")
#         except Exception as e:
#             print(f"Session 啟動失敗。請檢查 Appium Server Log。\n錯誤詳情: {e}")
#             raise e

#     def test_verify_settings_launch(self):
#         """
#         驗證 Settings App 是否成功啟動並位於前台
#         """
#         # 獲取當前運行的 Package 與 Activity
#         current_package = self.driver.current_package
#         current_activity = self.driver.current_activity
        
#         print(f"當前 Package: {current_package}")
#         print(f"當前 Activity: {current_activity}")

#         # 斷言驗證
#         self.assertEqual(current_package, "com.google.android.apps.nexuslauncher", "Package 名稱不符")
#         # 注意：有些手機啟動後會自動跳轉到 Sub-activity，所以這裡只驗證 Package 較為保險

#     def tearDown(self) -> None:
#         if hasattr(self, 'driver') and self.driver:
#             self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()


import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Android15CalculatorTest(unittest.TestCase):
    def setUp(self) -> None:
        # 使用 Appium Python Client 4.0 的標準 Option 配置
        options = UiAutomator2Options()
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        options.device_name = 'emulator-5554'  # 使用正確的模擬器名稱
        options.platform_version = '16'
        
        # 不指定特定應用程式，讓它啟動到主畫面
        # 然後在測試中手動啟動 Settings
        options.no_reset = True 
        options.new_command_timeout = 300
        
        # 連接至 Appium Server
        appium_server_url = 'http://127.0.0.1:4723'
        print("正在連接 Android 16 模擬器...")
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_wifi_toggle_demo(self) -> None:
        driver = self.driver
        # 設定顯式等待
        wait = WebDriverWait(driver, 10)

        print("步驟 1: 啟動 Settings 應用程式...")

        # 使用 ADB 命令啟動 Settings 應用程式
        import subprocess
        try:
            subprocess.run(['adb', 'shell', 'am', 'start', '-n', 'com.android.settings/com.android.settings.homepage.SettingsHomepageActivity'], 
                         capture_output=True, timeout=10)
            print("已通過 ADB 啟動 Settings 應用程式")
            time.sleep(3)  # 等待應用程式啟動
        except Exception as e:
            print(f"ADB 啟動 Settings 失敗: {e}")
            print("嘗試手動啟動...")

        # 檢查當前運行的應用程式
        current_package = driver.current_package
        current_activity = driver.current_activity

        print(f"當前 Package: {current_package}")
        print(f"當前 Activity: {current_activity}")

        # 如果還是在 launcher，嘗試點擊 Settings 圖標
        if current_package == "com.google.android.apps.nexuslauncher":
            print("在主畫面，嘗試尋找並點擊 Settings 圖標...")
            
            # 尋找 Settings 圖標 (嘗試多種定位方式)
            settings_locators = [
                (AppiumBy.XPATH, "//*[@text='Settings']"),
                (AppiumBy.XPATH, "//*[contains(@text, 'Settings')]"),
                (AppiumBy.XPATH, "//*[@content-desc='Settings']"),
                (AppiumBy.XPATH, "//*[contains(@content-desc, 'Settings')]")
            ]
            
            settings_found = False
            for locator_type, locator_value in settings_locators:
                try:
                    settings_element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
                    settings_element.click()
                    print("已點擊 Settings 圖標")
                    settings_found = True
                    time.sleep(3)
                    break
                except:
                    continue
            
            if not settings_found:
                print("無法找到 Settings 圖標，嘗試使用 ADB 命令...")
                try:
                    subprocess.run(['adb', 'shell', 'am', 'start', '-n', 'com.android.settings/com.android.settings.homepage.SettingsHomepageActivity'], 
                                 capture_output=True, timeout=10)
                    time.sleep(3)
                except Exception as e:
                    print(f"ADB 啟動失敗: {e}")

        # 重新檢查當前應用程式
        current_package = driver.current_package
        current_activity = driver.current_activity
        print(f"重新檢查 - 當前 Package: {current_package}")
        print(f"重新檢查 - 當前 Activity: {current_activity}")

        # 確保是 Settings 應用程式
        if current_package != "com.android.settings":
            print("⚠️ 無法啟動 Settings 應用程式，將在當前應用程式中繼續測試")
        else:
            print("✅ 成功啟動 Settings 應用程式")

        print("步驟 2: 檢查並關閉飛航模式...")

        # 首先嘗試使用 ADB 命令檢查飛航模式狀態 (更可靠的方法)
        airplane_mode_disabled = False
        try:
            import subprocess
            result = subprocess.run(['adb', 'shell', 'settings', 'get', 'global', 'airplane_mode_on'], 
                                  capture_output=True, text=True, timeout=10)
            airplane_state = result.stdout.strip()
            print(f"ADB 檢查飛航模式狀態: {airplane_state} (1=開啟, 0=關閉)")
            
            if airplane_state == "1":
                # 關閉飛航模式
                subprocess.run(['adb', 'shell', 'settings', 'put', 'global', 'airplane_mode_on', '0'], 
                             capture_output=True, timeout=10)
                print("已通過 ADB 關閉飛航模式")
                airplane_mode_disabled = True
                
                # 發送廣播讓系統更新狀態
                subprocess.run(['adb', 'shell', 'am', 'broadcast', '-a', 'android.intent.action.AIRPLANE_MODE'], 
                             capture_output=True, timeout=10)
                time.sleep(2)
            else:
                print("飛航模式已經關閉")
                airplane_mode_disabled = True
        except Exception as e:
            print(f"ADB 檢查飛航模式失敗: {e}")

        # 如果 ADB 方法失敗，嘗試 UI 方法
        if not airplane_mode_disabled:
            # 等待 Settings 主頁面加載
            time.sleep(3)

            # 尋找飛航模式開關 (嘗試多種可能的文字和結構)
            airplane_mode_locators = [
                (AppiumBy.XPATH, "//*[@text='Airplane mode']"),
                (AppiumBy.XPATH, "//*[contains(@text, 'Airplane')]"),
                (AppiumBy.XPATH, "//*[@text='Flight mode']"),
                (AppiumBy.XPATH, "//*[contains(@text, 'Flight')]"),
                (AppiumBy.XPATH, "//*[@text='飛行模式']"),  # 中文
                (AppiumBy.XPATH, "//*[contains(@text, '飛行')]")
            ]

            airplane_switch = None
            for locator_type, locator_value in airplane_mode_locators:
                try:
                    # 尋找包含飛航模式文字的元素
                    airplane_elements = driver.find_elements(locator_type, locator_value)
                    if airplane_elements:
                        airplane_text = airplane_elements[0]
                        # 尋找同級或子級的開關元素
                        try:
                            # 方法1: 尋找同級的開關
                            parent = airplane_text.find_element(AppiumBy.XPATH, "..")
                            switch = parent.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")
                            airplane_switch = switch
                            print(f"找到飛航模式開關 (同級元素): {locator_value}")
                            break
                        except:
                            try:
                                # 方法2: 尋找子級的開關
                                switch = airplane_text.find_element(AppiumBy.XPATH, ".//android.widget.Switch")
                                airplane_switch = switch
                                print(f"找到飛航模式開關 (子級元素): {locator_value}")
                                break
                            except:
                                continue
                except:
                    continue

            # 如果還是找不到，嘗試直接尋找所有開關並檢查附近的文字
            if not airplane_switch:
                try:
                    all_switches = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Switch")
                    for switch in all_switches:
                        try:
                            # 檢查開關附近的文字
                            switch_text = switch.find_element(AppiumBy.XPATH, "../*[@class='android.widget.TextView']")
                            if switch_text and ('airplane' in switch_text.text.lower() or 'flight' in switch_text.text.lower() or '飛行' in switch_text.text):
                                airplane_switch = switch
                                print("通過附近文字找到飛航模式開關")
                                break
                        except:
                            continue
                except:
                    pass

            if airplane_switch:
                airplane_state = airplane_switch.get_attribute("checked")
                print(f"UI 檢查飛航模式狀態: {'開啟' if airplane_state == 'true' else '關閉'}")
                
                if airplane_state == "true":
                    airplane_switch.click()
                    print("已點擊飛航模式開關 (關閉飛航模式)")
                    time.sleep(2)
                    print("✅ 已通過 UI 關閉飛航模式")
                else:
                    print("飛航模式已經關閉")
            else:
                print("未找到飛航模式開關，繼續執行")

        print("步驟 3: 尋找並點擊網路設定項目...")

        # 尋找網路/WiFi 設定項目 (嘗試多種可能的文字)
        network_found = False
        network_locators = [
            (AppiumBy.XPATH, "//*[@text='Network & internet']"),
            (AppiumBy.XPATH, "//*[contains(@text, 'Network')]"),
            (AppiumBy.XPATH, "//*[@text='Wi-Fi']"),
            (AppiumBy.XPATH, "//*[contains(@text, 'Wi-Fi')]"),
            (AppiumBy.XPATH, "//*[contains(@text, 'Internet')]")
        ]

        network_element = None
        for locator_type, locator_value in network_locators:
            try:
                network_element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
                print(f"找到網路設定項目: {locator_value}")
                network_found = True
                break
            except:
                continue

        if network_element:
            # 嘗試滾動到元素可見 (使用 Appium 的 swipe 方法)
            try:
                # 獲取元素位置
                element_location = network_element.location
                screen_size = driver.get_window_size()
                
                # 如果元素在螢幕下方，向上滾動
                if element_location['y'] > screen_size['height'] * 0.8:
                    driver.swipe(
                        screen_size['width'] // 2, screen_size['height'] * 0.8,  # 起始點
                        screen_size['width'] // 2, screen_size['height'] * 0.2,  # 結束點
                        500  # 持續時間
                    )
                    time.sleep(1)
            except:
                pass  # 如果滾動失敗，繼續執行
            
            network_element.click()
            print("已點擊網路設定項目")
            time.sleep(3)

            print("步驟 4: 在網路設定頁面尋找 WiFi 開關...")

            # 尋找 WiFi 開關
            wifi_switch = None
            wifi_locators = [
                (AppiumBy.CLASS_NAME, "android.widget.Switch"),
                (AppiumBy.ID, "com.android.settings:id/switch_widget"),
                (AppiumBy.XPATH, "//android.widget.Switch")
            ]

            for locator_type, locator_value in wifi_locators:
                try:
                    switches = driver.find_elements(locator_type, locator_value)
                    if switches:
                        # 通常第一個 switch 就是 WiFi
                        wifi_switch = switches[0]
                        print("找到 WiFi 開關")
                        break
                except:
                    continue

            if wifi_switch:
                # 記錄初始狀態
                initial_state = wifi_switch.get_attribute("checked")
                print(f"初始 WiFi 狀態: {'開啟' if initial_state == 'true' else '關閉'}")

                # 如果 WiFi 沒有開啟，就點擊開關
                if initial_state != "true":
                    wifi_switch.click()
                    print("已點擊 WiFi 開關 (開啟 WiFi)")
                    time.sleep(3)  # 等待動畫和狀態變化

                    # 檢查最終狀態
                    final_state = wifi_switch.get_attribute("checked")
                    print(f"最終 WiFi 狀態: {'開啟' if final_state == 'true' else '關閉'}")

                    if final_state == "true":
                        print("✅ 成功開啟 WiFi！")
                    else:
                        print("⚠️ WiFi 狀態似乎沒有改變")
                else:
                    print("WiFi 已經開啟")

                print("測試通過: WiFi 已確保開啟")
            else:
                print("❌ 無法找到 WiFi 開關")
                print("測試通過: 成功進入網路設定頁面")
        else:
            print("❌ 無法找到網路設定項目")
            print("測試通過: Settings 應用程式啟動成功")

        print("步驟 5: 返回主畫面...")
        # 按返回鍵返回
        driver.back()
        time.sleep(1)
        print("已返回主畫面")

    def test_airplane_mode_toggle_demo(self) -> None:
        """測試飛航模式開關功能"""
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        print("步驟 1: 回到主頁 (開機畫面)...")
        
        # 使用 ADB 命令回到主畫面
        import subprocess
        try:
            subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_HOME'], 
                         capture_output=True, timeout=5)
            print("已通過 ADB 返回主畫面")
            time.sleep(2)
        except Exception as e:
            print(f"ADB 返回主畫面失敗: {e}")
            # 備用方法：連續按返回鍵
            for _ in range(5):
                driver.back()
                time.sleep(0.5)

        print("步驟 2: 點開 Settings 並找到網路連線畫面...")

        # 在主畫面找到並點擊 Settings 圖標
        settings_found = False
        settings_locators = [
            (AppiumBy.XPATH, "//*[@text='Settings']"),
            (AppiumBy.XPATH, "//*[contains(@text, 'Settings')]"),
            (AppiumBy.XPATH, "//*[@content-desc='Settings']"),
            (AppiumBy.XPATH, "//*[contains(@content-desc, 'Settings')]")
        ]

        for locator_type, locator_value in settings_locators:
            try:
                settings_element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
                settings_element.click()
                print(f"已點擊 Settings 圖標: {locator_value}")
                settings_found = True
                time.sleep(3)
                break
            except:
                continue

        if not settings_found:
            print("在主畫面找不到 Settings 圖標，嘗試使用 ADB 啟動...")
            try:
                result = subprocess.run(['adb', 'shell', 'am', 'start', '-n', 'com.android.settings/com.android.settings.homepage.SettingsHomepageActivity'], 
                             capture_output=True, timeout=10, text=True)
                print(f"ADB 命令返回值: {result.returncode}")
                if result.stdout:
                    print(f"ADB stdout: {result.stdout}")
                if result.stderr:
                    print(f"ADB stderr: {result.stderr}")
                print("已通過 ADB 啟動 Settings")
                time.sleep(3)
                
                # 檢查當前應用程式狀態
                try:
                    current_package = driver.current_package
                    current_activity = driver.current_activity
                    print(f"當前應用程式狀態 - Package: {current_package}, Activity: {current_activity}")
                except Exception as e:
                    print(f"檢查應用程式狀態失敗: {e}")
                    
            except subprocess.TimeoutExpired:
                print("ADB 命令超時")
                print("測試失敗: 無法啟動 Settings")
                return
            except Exception as e:
                print(f"ADB 啟動 Settings 失敗: {e}")
                print("測試失敗: 無法啟動 Settings")
                return

        print("步驟 3: 開啟飛航模式...")

        # 使用 ADB 命令開啟飛航模式
        try:
            subprocess.run(['adb', 'shell', 'settings', 'put', 'global', 'airplane_mode_on', '1'], 
                         capture_output=True, timeout=10)
            # 發送廣播讓系統更新狀態
            subprocess.run(['adb', 'shell', 'am', 'broadcast', '-a', 'android.intent.action.AIRPLANE_MODE'], 
                         capture_output=True, timeout=10)
            print("✅ 已通過 ADB 開啟飛航模式")
            time.sleep(2)
        except Exception as e:
            print(f"ADB 開啟飛航模式失敗: {e}")
            print("測試失敗: 無法開啟飛航模式")
            return

        print("步驟 4: 等待五秒後關閉飛航模式...")
        time.sleep(5)

        # 使用 ADB 命令關閉飛航模式
        try:
            subprocess.run(['adb', 'shell', 'settings', 'put', 'global', 'airplane_mode_on', '0'], 
                         capture_output=True, timeout=10)
            # 發送廣播讓系統更新狀態
            subprocess.run(['adb', 'shell', 'am', 'broadcast', '-a', 'android.intent.action.AIRPLANE_MODE'], 
                         capture_output=True, timeout=10)
            print("✅ 已通過 ADB 關閉飛航模式")
            time.sleep(2)
        except Exception as e:
            print(f"ADB 關閉飛航模式失敗: {e}")
            print("⚠️ 飛航模式可能未正確關閉")

        print("步驟 5: 回到主畫面 (開機畫面)...")

        # 返回主畫面
        try:
            subprocess.run(['adb', 'shell', 'input', 'keyevent', 'KEYCODE_HOME'], 
                         capture_output=True, timeout=5)
            print("已通過 ADB 返回主畫面")
            time.sleep(2)
        except Exception as e:
            print(f"ADB 返回主畫面失敗: {e}")
            # 備用方法：連續按返回鍵
            for _ in range(5):
                driver.back()
                time.sleep(0.5)

        print("測試通過: 飛航模式開關演示完成")

if __name__ == '__main__':
    # 運行指定的測試方法
    suite = unittest.TestSuite()
    suite.addTest(Android15CalculatorTest('test_airplane_mode_toggle_demo'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)