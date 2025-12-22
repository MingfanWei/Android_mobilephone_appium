# Android Mobile Appium Automation - AI Agent Instructions

## Project Overview
This is an Appium-based mobile automation project targeting Android devices (specifically Pixel 7a with Android 16). The codebase uses Python with unittest framework to test native Android applications.

## Architecture & Key Components
- **Single Script Structure**: All test code resides in `script.py` with multiple commented-out test class examples
- **Appium 2.x Integration**: Uses UiAutomator2Options (not legacy DesiredCapabilities)
- **Target Environment**: Android 16 with UiAutomator2 automation driver

## Critical Dependencies & Environment
```bash
# Required packages (install via pip in virtual environment)
Appium-Python-Client==5.2.4
selenium==4.38.0
```

**Environment Setup:**
- Python 3.13.3 virtual environment required
- Appium Server must be running on `http://localhost:4723`
- Android device/emulator connected via ADB

## Core Patterns & Conventions

### 1. Driver Configuration (Android 15 Specific)
```python
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.device_name = 'emulator-5554'  # Use actual emulator name from 'adb devices'
options.platform_version = '16'
options.app_package = 'com.google.android.calculator'  # Calculator app (works on Android 16)
options.app_activity = 'com.android.calculator2.Calculator'
options.no_reset = False  # Force clean app start
options.new_command_timeout = 300  # Prevent Android 16 timeouts
```

### 2. Element Location Strategy
**Primary**: Resource IDs (most stable for Android)
```python
from appium.webdriver.common.appiumby import AppiumBy

# Preferred: Resource ID
element = driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2")
```

**Secondary**: XPath for complex hierarchies
```python
element = driver.find_element(AppiumBy.XPATH, "//*[@text='Settings']")
```

### 3. Wait Strategy (Critical for Android 15)
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "element_id")))
```

### 4. Test Structure Pattern
```python
import unittest
from appium import webdriver

class AndroidAppTest(unittest.TestCase):
    def setUp(self):
        # Driver setup with UiAutomator2Options
        self.driver = webdriver.Remote("http://localhost:4723", options=options)

    def test_feature(self):
        # Test logic with explicit waits
        # Visual verification delays (time.sleep(1)) for demo purposes

    def test_basic_functionality(self):
        # Verify basic Appium connection
        self.assertIsNotNone(self.driver.page_source)
        self.assertEqual(self.driver.current_context, "NATIVE_APP")

    def tearDown(self):
        if hasattr(self, 'driver'):
            self.driver.quit()
```

## Project-Specific Workflows

### Running Tests
```bash
# From project root
python script.py
# or
python -m unittest script.py
```

### Appium Server Management
```bash
# Start Appium server (external requirement)
appium --address 127.0.0.1 --port 4723
```

### Device Connection
- Ensure Android device is connected via USB
- Enable USB debugging in developer options
- Verify with `adb devices`

## Common Pitfalls & Solutions

### Android 16 Specific Issues
- **Timeout Errors**: Always set `new_command_timeout = 300`
- **App Package Names**: Use AOSP standard names, not Google internal packages
  - ❌ `com.google.android.settings` (Error Type 3)
  - ✅ `com.android.settings`
- **Activity Names**: Include full path or use dot notation
### App Launch Issues**: Some system apps may require specific activity names or may not launch as expected
- **Calculator App**: Can be launched with `com.google.android.calculator` package and `com.android.calculator2.Calculator` activity
- **Settings App**: May require specific activity names like `com.android.settings.homepage.SettingsHomepageActivity`

### Element Location Failures
- Prefer resource IDs over text/XPath when available
- Use `WebDriverWait` instead of `time.sleep()` for reliability
- Android 16 has aggressive power management - expect UI delays

### Session Management
- Always check `driver.current_package` and `driver.current_activity` for verification
- Use `no_reset = True` for faster subsequent runs, `False` for clean state
- **For pre-installed system apps**: Set `no_reset = True` (calculator, settings, etc.)
- **For APK installation**: Set `no_reset = False` and provide `app` option with APK path

### Basic Functionality Testing
```python
# Test basic Appium connection without app-specific logic
def test_basic_functionality(self):
    # Check current app state
    current_package = self.driver.current_package
    current_activity = self.driver.current_activity
    print(f"Current Package: {current_package}")
    print(f"Current Activity: {current_activity}")
    
    # Verify basic driver functionality
    self.assertIsNotNone(self.driver.page_source)
    self.assertEqual(self.driver.current_context, "NATIVE_APP")
```

### Demonstrating Appium Control
```python
# Demonstrate Appium control with basic gestures and element interaction
def test_appium_control_demo(self):
    # Get screen size for gesture coordinates
    screen_size = self.driver.get_window_size()
    
    # Perform swipe gesture
    start_x = screen_size['width'] * 0.8
    end_x = screen_size['width'] * 0.2
    center_y = screen_size['height'] * 0.5
    self.driver.swipe(start_x, center_y, end_x, center_y, 1000)
    
    # Find and interact with elements
    elements = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    if elements:
        print(f"Found element: '{elements[0].text}'")
    
    # Perform tap gesture
    center_x = screen_size['width'] * 0.5
    center_y = screen_size['height'] * 0.5
    self.driver.tap([(center_x, center_y)])
```

### Calculator App Testing Example
```python
def test_calculator_functionality(self):
    # Verify calculator app is running
    self.assertEqual(self.driver.current_package, "com.google.android.calculator")
    
    # Perform calculation: 2 + 3 = 5
    digit_2 = self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_2")
    digit_2.click()
    
    plus = self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/op_add")
    plus.click()
    
    digit_3 = self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/digit_3")
    digit_3.click()
    
    equals = self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq")
    equals.click()
    
    # Verify result
    result = self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/result_final")
    self.assertEqual(result.text, "5")
```

### WiFi Toggle Testing Example
```python
def test_wifi_toggle(self):
    # Verify Settings app is running
    self.assertEqual(self.driver.current_package, "com.android.settings")
    
    # Find and click WiFi settings
    wifi_option = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Wi-Fi']")
    wifi_option.click()
    
    # Find WiFi switch and toggle it
    wifi_switch = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.Switch")
    initial_state = wifi_switch.get_attribute("checked")
    wifi_switch.click()
    
    # Verify state changed
    final_state = wifi_switch.get_attribute("checked")
    self.assertNotEqual(initial_state, final_state)
```

### System Control via ADB Commands
```python
def test_wifi_toggle_adb(self):
    import subprocess
    
    # Check initial WiFi state
    result = subprocess.run(['adb', 'shell', 'settings', 'get', 'global', 'wifi_on'], 
                          capture_output=True, text=True)
    initial_state = result.stdout.strip()
    
    # Toggle WiFi
    new_state = "0" if initial_state == "1" else "1"
    subprocess.run(['adb', 'shell', 'settings', 'put', 'global', 'wifi_on', new_state])
    
    # Verify state changed
    result = subprocess.run(['adb', 'shell', 'settings', 'get', 'global', 'wifi_on'], 
                          capture_output=True, text=True)
    final_state = result.stdout.strip()
    self.assertNotEqual(initial_state, final_state)
```

## Code Organization Patterns
- Multiple test classes in single file (historical examples commented out)
- Heavy commenting in Chinese for Android-specific configurations
- Visual testing with `time.sleep()` delays between actions
- Assert final results rather than intermediate states
- **Focus on basic functionality testing** rather than complex app launching scenarios

## Key Reference Files
- `script.py`: Complete examples for Settings and Calculator app testing
- Virtual environment contains all required dependencies</content>
<parameter name="filePath">c:\Automation\Pixel7aProject\.github\copilot-instructions.md