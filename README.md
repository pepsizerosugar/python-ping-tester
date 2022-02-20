# python-ping-tester

![Version](https://img.shields.io/badge/Version-1.2.0-green)
![Update](https://img.shields.io/badge/Update-2022.02.20-darkgrey)
[![CodeFactor](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester/badge)](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester)

* Ping test utility GUI
  <br><br>
  <img src="./resource/img/demo.gif" alt="">
  <br><br>

## 0. Change Log

### version 1.2.0 (2022.02.20)

* Commit history
    * [pepsi-026] added some resource, edited build.bat
    * [pepsi-025] separated Main class to each method type
    * [pepsi-024] changed demo to realtime version
    * [pepsi-023] committed before separate method
    * [pepsi-022] updated server list

<br>

## 1. Getting Started

### 1-1. Installation

1. Download the lastest version from [GitHub](https://github.com/pepsizerosugar/python-ping-tester/releases) or Clone the
   repository.
    1. ```git clone https://github.com/pepsizerosugar/python-ping-tester.git```

2. Build Main.py using build.bat or just run.
    1. When build is done, you can run the PingPong.exe in the dist folder.
    2. server_list.json file at top-level folder is automatically copy to dist folder.
       <br>
       <img src="./resource/img/program_when_build_finished.PNG" alt="">
3. Or downaload the lastest binary file what name "PingPong.zip" from [GitHub](https://github.com/pepsizerosugar/python-ping-tester/releases) and unzip it.

### 1-2. How to use

* Edit server list
    1. Open the server_list.json file.
    2. Enter the list of servers you want to ping according to the server list format.
    3. Save the file.

* Server list json format

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

* When you click the Ping button, the ping result will be shown in the list.
* And the best ping time result will be shown in the messagebox when all ping finished.
    * <img src="./resource/img/messagebox_when_ping_finished.PNG" alt="">
* After click the ok at messagebox, the ping result will automatically sort by ping time.
