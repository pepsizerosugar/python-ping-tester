# python-ping-tester

![Version](https://img.shields.io/badge/Version-1.1.0-green)
![Update](https://img.shields.io/badge/Update-2022.02.19-darkgrey)
[![CodeFactor](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester/badge)](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester)

* Ping test utility GUI
  <br><br>
  ![sample_run](https://user-images.githubusercontent.com/84403670/154633965-3ee0d2e2-d877-4ddb-8a4b-24bd26d77e3d.gif)
  <br><br>

## 0. Change Log

### version 1.1.0 (2022.02.19)

* Commit history
    * [pepsi-013] removed unused keys from server_list.json
    * [pepsi-012] moved [TEMP] Ping Test.py to 'Temp' folder
    * [pepsi-011] removed icon.png, edited setWindowIcon file
    * [pepsi-010] added app icon.ico
    * [pepsi-009] removed duplicate code in update_progress function

<br>

## 1. Getting Started

### 1-1. Installation

1. Download the latest version from [GitHub](https://github.com/pepsizerosugar/python-ping-tester/releases)' or Clone
   the repository.
2. Build Main.py with pyinstaller or just run.

### 1-2. How to use

1. Check All button 1-1. Check all servers in the list.
2. Uncheck All button 2-1. Uncheck all servers in the list.
3. Ping button 3-1. Ping checked servers in the list.
4. Clear button 4-1. Clear ping result in the list.

### 1-3. Extra

1. You can make your own server_list.json and put it in the same folder.

<br>

## 2. Example server_list.json

```json
{
  "server_list": [
    {
      "name": "server_name",
      "region": "server_region",
      "ip_addresses": [
        "server_ip_address_01",
        "server_ip_address_02"
      ]
    },
    {
      "name": "server_name",
      "region": "server_region",
      "ip_addresses": [
        "server_ip_address_01",
        "server_ip_address_02"
      ]
    }
  ]
}
```
