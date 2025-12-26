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


# import time
# import unittest
# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# class Android15CalculatorTest(unittest.TestCase):
#     def setUp(self) -> None:
#         # 使用 Appium Python Client 4.0 的標準 Option 配置
#         options = UiAutomator2Options()
#         options.platform_name = 'Android'
#         options.automation_name = 'UiAutomator2'
#         options.device_name = 'emulator-5554'  # options.device_name = 'Pixel_7a'
#         options.platform_version = '16'
        
#         # 明確指定要啟動的應用包名與 Activity
#         # 這是確保 Appium 能找到並啟動計算機的關鍵 [8]
#         options.app_package = 'com.google.android.calculator'
#         options.app_activity = 'com.android.calculator2.Calculator'
        
#         # 設置 no_reset 為 False，強制重啟應用，讓用戶看到「啟動」的過程
#         options.no_reset = False 
        
#         # 連接至 Appium Server
#         appium_server_url = 'http://127.0.0.1:4723'
#         print("正在啟動 Android 16 計算機應用程式...")
#         self.driver = webdriver.Remote(appium_server_url, options=options)

#     def tearDown(self) -> None:
#         if self.driver:
#             self.driver.quit()

#     def test_addition_visualization(self) -> None:
#         driver = self.driver
#         # 設定顯式等待，這是處理 Android 15 動畫延遲的最佳實踐 
#         wait = WebDriverWait(driver, 10)

#         print("步驟 1: 應用程式已啟動，正在等待 UI 加載...")
        
#         # 定位計算機按鈕
#         # 使用 Resource ID 是最穩定的方式。在 Google 計算機中，ID 通常如下：
#         # digit_2 對應數字 2，op_add 對應加號
#         el_digit_2 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "com.google.android.calculator:id/digit_2")))
#         el_plus = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add")
#         el_digit_5 = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_5")
#         el_equals = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq")

#         # 執行動作並加入人為延遲，以便肉眼觀察
#         print("步驟 2: 點擊 '2'")
#         el_digit_2.click()
#         time.sleep(1) # 暫停 1 秒，讓用戶看到數字出現

#         print("步驟 3: 點擊 '+'")
#         el_plus.click()
#         time.sleep(1)

#         print("步驟 4: 點擊 '5'")
#         el_digit_5.click()
#         time.sleep(1)

#         print("步驟 5: 點擊 '='")
#         el_equals.click()
        
#         # 驗證結果
#         result_field = wait.until(EC.presence_of_element_located(
#             (AppiumBy.ID, "com.google.android.calculator:id/result_final")))
        
#         result_text = result_field.text
#         print(f"計算結果: {result_text}")
        
#         # 斷言驗證
#         assert result_text == "7", f"預期結果為 7，但實際獲得 {result_text}"
#         print("測試通過: 成功在設備上驗證 2 + 5 = 7。")
#         time.sleep(2) # 最後暫停，展示最終畫面

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
        options.no_reset = True  # 對於系統應用，保持True以避免重新安裝
        options.new_command_timeout = 300
        
        # 連接至 Appium Server
        appium_server_url = 'http://127.0.0.1:4723'
        print("正在連接 Android 16 模擬器...")
        self.driver = webdriver.Remote(appium_server_url, options=options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

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

        print("步驟 2: 啟動 Settings 應用程式...")

        # 使用 ADB 命令啟動 Settings 應用程式
        import subprocess
        
        try:
            print("啟動 Settings 應用程式...")
            # 使用已知成功的 activity
            result = subprocess.run(['adb', 'shell', 'am', 'start', '-n', 'com.android.settings/.Settings', '--activity-clear-task'], 
                         capture_output=True, timeout=10, text=True)
            if result.returncode == 0:
                print("成功啟動 Settings 應用程式")
                time.sleep(3)  # 等待應用程式啟動
                
                # 檢查是否正確啟動
                current_package = driver.current_package
                current_activity = driver.current_activity
                print(f"檢查 - Package: {current_package}, Activity: {current_activity}")
                
                if current_package == "com.android.settings":
                    print("✅ Settings 應用程式啟動成功")
                else:
                    print(f"⚠️ 應用程式啟動但 package 不正確: {current_package}")
            else:
                print(f"ADB 啟動失敗，返回碼: {result.returncode}")
                if result.stderr:
                    print(f"ADB 錯誤: {result.stderr}")
                return
        except Exception as e:
            print(f"Settings 啟動失敗: {e}")
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

        print("步驟 5: 通過 UI 開啟 WiFi...")

        # 首先嘗試通過 UI 進入網路設定
        try:
            # 尋找網路設定項目
            network_locators = [
                (AppiumBy.XPATH, "//*[@text='Network & internet']"),
                (AppiumBy.XPATH, "//*[contains(@text, 'Network')]"),
                (AppiumBy.XPATH, "//*[@text='Network & Internet']"),
                (AppiumBy.XPATH, "//*[contains(@text, 'Network & Internet')]")
            ]

            network_found = False
            for locator_type, locator_value in network_locators:
                try:
                    network_element = wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
                    network_element.click()
                    print("已點擊 Network & internet 項目")
                    network_found = True
                    time.sleep(5)
                    break
                except:
                    continue

            if not network_found:
                print("❌ 無法找到 Network & internet 項目")
                return

            # 在 Network & internet 頁面尋找 Internet 子項目
            print("尋找 Internet 子項目...")
            internet_locators = [
                (AppiumBy.XPATH, "//*[@text='Internet']"),
                (AppiumBy.XPATH, "//*[contains(@text, 'Internet')]"),
                (AppiumBy.XPATH, "//*[@text='Wi-Fi']"),
                (AppiumBy.XPATH, "//*[contains(@text, 'Wi-Fi')]")
            ]

            internet_found = False
            for locator_type, locator_value in internet_locators:
                try:
                    internet_elements = driver.find_elements(locator_type, locator_value)
                    for element in internet_elements:
                        # 檢查是否是正確的 Internet/Wi-Fi 項目
                        try:
                            element.click()
                            print("已點擊 Internet 子項目")
                            internet_found = True
                            time.sleep(2)
                            break
                        except:
                            continue
                    if internet_found:
                        break
                except:
                    continue

            if not internet_found:
                print("❌ 無法找到 Internet 子項目")
                # 返回設定主頁面
                driver.back()
                time.sleep(1)
                return

            # 在 Internet 頁面尋找並開啟 WiFi 開關
            print("尋找 WiFi 開關...")
            wifi_switch_found = False
            wifi_switch_locators = [
                (AppiumBy.CLASS_NAME, "android.widget.Switch"),
                (AppiumBy.ID, "com.android.settings:id/switch_widget")
            ]

            for locator_type, locator_value in wifi_switch_locators:
                try:
                    switches = driver.find_elements(locator_type, locator_value)
                    if switches:
                        wifi_switch = switches[0]  # 通常第一個就是 WiFi
                        wifi_state = wifi_switch.get_attribute("checked")
                        print(f"當前 WiFi 狀態: {'開啟' if wifi_state == 'true' else '關閉'}")

                        if wifi_state != "true":
                            wifi_switch.click()
                            print("已點擊 WiFi 開關 (開啟)")
                            time.sleep(2)

                            # 檢查最終狀態
                            final_state = wifi_switch.get_attribute("checked")
                            print(f"最終 WiFi 狀態: {'開啟' if final_state == 'true' else '關閉'}")

                            if final_state == "true":
                                print("✅ 成功通過 UI 開啟 WiFi")
                                wifi_switch_found = True
                            else:
                                print("⚠️ WiFi 開關點擊後狀態未改變")
                        else:
                            print("✅ WiFi 已經開啟")
                            wifi_switch_found = True
                        break
                except Exception as e:
                    print(f"操作 WiFi 開關失敗: {e}")
                    continue

            if not wifi_switch_found:
                print("❌ 無法找到或操作 WiFi 開關")

            # 返回設定主頁面 (需要返回兩次：從Internet頁面回到Network頁面，再回到Settings主頁面)
            driver.back()
            time.sleep(1)
            driver.back()
            time.sleep(1)

        except Exception as e:
            print(f"UI 操作 WiFi 失敗: {e}")
            print("嘗試使用 ADB 命令作為備用方案...")
            try:
                subprocess.run(['adb', 'shell', 'settings', 'put', 'global', 'wifi_on', '1'], 
                             capture_output=True, timeout=10)
                subprocess.run(['adb', 'shell', 'am', 'broadcast', '-a', 'android.intent.action.WIFI_MODE_CHANGED'], 
                             capture_output=True, timeout=10)
                print("✅ 已通過 ADB 備用方案開啟 WiFi")
            except Exception as backup_e:
                print(f"ADB 備用方案也失敗: {backup_e}")

        print("步驟 6: 回到主畫面 (開機畫面)...")

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

        print("測試通過: 飛航模式開關與 WiFi 開啟演示完成")

if __name__ == '__main__':
    # 運行指定的測試方法
    suite = unittest.TestSuite()
    suite.addTest(Android15CalculatorTest('test_airplane_mode_toggle_demo'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    