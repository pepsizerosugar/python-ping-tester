# python-ping-tester

![Version](https://img.shields.io/badge/Version-1.1.0-green)
![Update](https://img.shields.io/badge/Update-2022.02.19-darkgrey)
[![CodeFactor](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester/badge)](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester)

* Ping test utility GUI
  <br><br>
  <img src="./resource/img/demo.gif" alt="">
  <br><br>

## 0. Change Log

### version 1.1.0 (2022.02.19)

* Commit history
    * [pepsi-019] added build bat
    * [pepsi-018] updated demo.gif to new GUI version
    * [pepsi-017] changed result cell type String to Integer for sorting when ping finished
    * [pepsi-016] edited ping count 4 to 5
    * [pepsi-015] replaced sample_run.gif to demo.gif
    * [pepsi-014] replaced statusBar with progressBar, disable buttons when ping started
    * [pepsi-013] removed unused keys from server_list.json
    * [pepsi-012] moved '[TEMP] Ping Test.py' to 'Temp' folder
    * [pepsi-011] removed icon.png, edited setWindowIcon file
    * [pepsi-010] added app icon.ico
    * [pepsi-009] removed duplicate code in update_progress function

<br>

## 1. Getting Started

### 1-1. Installation

1. Download the latest version from [GitHub](https://github.com/pepsizerosugar/python-ping-tester/releases) or Clone the
   repository.
    1. ```git clone https://github.com/pepsizerosugar/python-ping-tester.git```

2. Build Main.py using build.bat or just run.

### 1-2. How to use

* Server List
    1. Open the server_list.json file.
    2. Add your server to the list.
    3. Save the file.

* Example

```json
{
  "server_list": [
    {
      "name": "Seoul",
      "region": "ASI",
      "ip_addresses": [
        "127.0.0.1",
        "127.0.0.2"
      ]
    },
    {
      "name": "Germany",
      "region": "EUR",
      "ip_addresses": [
        "127.0.0.1",
        "127.0.0.2"
      ]
    }
  ]
}
```

* Buttons
    1. Check All button
        * Check all servers in the list.
    2. Uncheck All button
        * Uncheck all servers in the list.
    3. Ping button
        * Ping checked servers in the list.
    4. Clear button
        * Clear ping result in the list.