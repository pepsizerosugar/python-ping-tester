# python-ping-tester

![Version](https://img.shields.io/badge/Version-1.3.0-green)
![Update](https://img.shields.io/badge/Update-2022.02.25-blue)
[![CodeFactor](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester/badge)](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester)

* Ping test utility GUI
* Make with 'PyQt5' GUI library
  <br><br>
  <img src="./resource/img/demo.gif" alt="">
  <br><br>

## 0. Change Log

### version 1.3.0 (2022.02.25)

* Commit history
    * [pepsi-047] updated demo gif
    * [pepsi-046] updated server list
    * [pepsi-045] added rank of result
    * [pepsi-044] added ping loss parsing
    * [pepsi-043] added ping loss column
    * [pepsi-042] changed demo gif
    * [pepsi-041] changed README.md
    * [pepsi-040] changed ping result parsing flow to avoid errors from QTableWidget sorting API
    * [pepsi-039] changed group box name
    * [pepsi-038] created combobox for select specific options
    * [pepsi-037] changed analyze order
    * [pepsi-036] changed build script to add resource
    * [pepsi-035] changed icon path

<br>

## 1. Getting Started

### 1-1. Installation

1. Download the lastest version from [GitHub](https://github.com/pepsizerosugar/python-ping-tester/releases) or Clone
   the repository.
    1. ```git clone https://github.com/pepsizerosugar/python-ping-tester.git```

2. Build Main.py using build.bat or just run.
    1. When build is finish, you can run the PingPong.exe in the dist folder.
    2. server_list.json file at top-level folder is automatically copy to dist folder.
       <br>
       <img src="./resource/img/program_when_build_finished.PNG" alt="">
3. Or downaload the lastest binary file what name "PingPong.zip"
   from [GitHub](https://github.com/pepsizerosugar/python-ping-tester/releases) and unzip it.

### 1-2. How to use

* Edit server list
    1. Open the server_list.json file.
    2. Enter the list of servers you want to ping according to the server list format.
    3. Save the file.

* Server list json format

```json
{
  "server_list": {
    "ServerName01": {
      "region": "USA",
      "ip_addresses": [
        "111.222.333.444",
        "111.222.333.444"
      ]
    },
    "ServerName02": {
      "region": "OCE",
      "ip_addresses": [
        "111.222.333.444",
        "111.222.333.444"
      ]
    }
  }
}
```

* Interactions
    1. Type combo box
        1. ```All``` is default.
        2. If select ```Server```, you can select the server name from the list at Select combo box.
        3. If select ```Region```, you can select the region name from the list at Select combo box.
    2. Select combo box
        1. If select ```Server``` at type combo box, you can select the server from the list.
        2. If select ```Region``` at type combo box, you can select the region from the list.
    3. Check button
        * Check servers what you selected at Select combo box.
    4. Uncheck button
        * Uncheck all servers in the list.
    5. Ping button
        * Ping checked servers in the list.
    6. Clear button
        * Clear ping result in the list.

* When you click the Ping button, the ping result will be shown in the list.
* The ping result will automatically sort by avg ping time.
* And the best ping time result will be shown in the messagebox when all ping finished.
    * <img src="./resource/img/messagebox_when_ping_finished.PNG" alt="">

## 2. Extra

### 2-1. Analyze

* Analyze of ping result is shown in log.
    * One for server, one for region.
    * Next update will be separate the result analyzed data to other window tap.
