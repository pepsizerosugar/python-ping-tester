# python-ping-tester

![Version](https://img.shields.io/badge/Version-1.0.0-green)
![Update](https://img.shields.io/badge/Update-2022.02.18-darkgrey)
[![CodeFactor](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester/badge)](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester)

* Ping test utility GUI
![sample_run](![](https://raw.githubusercontent.com/pepsizerosugar/python-ping-tester/resource/img/sample_run.gif))
  <br><br>

## 0. Change Log

### version 1.0.0 (2022.02.18)

```
1. Commit version 1.0.0
```

<br>

## 1. Getting Started

### 1-1. Installation

```
1. Download or clone the repo.
2. Build Main.py with pyinstaller or just run.
```

### 1-2. How to use

```
1. Check All button
    1-1. Check all servers in the list.
2. UnCheck All button
    2-1. UnCheck all servers in the list.
3. Ping button
    3-1. Ping checked servers in the list.
4. Clear button
    4-1. Clear ping result in the list.
```

### 1-3. Extra

```
1. You can make your own server_list.json and put it in the same folder.
```

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
    ...
  ]
}
```