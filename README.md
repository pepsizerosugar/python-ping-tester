# python-ping-tester

![Version](https://img.shields.io/badge/Version-1.4.0-green)
![Update](https://img.shields.io/badge/Update-2022.03.06-blue)
[![CodeFactor](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester/badge)](https://www.codefactor.io/repository/github/pepsizerosugar/python-ping-tester)
![GitHub all releases](https://img.shields.io/github/downloads/pepsizerosugar/python-ping-tester/total?color=orange)

* Ping test utility GUI
* Make with
    * [PyQt5](https://github.com/PyQt5) GUI library
    * [qtmodern](https://github.com/gmarull/qtmodern) theme

<br>
<img src="./Resource/Img/demo.gif" alt="">
<br><br>

## 0. Change Log

### version 1.4.0 (2022.03.06)

* Commit history
    * [pepsi-071] changed build script
    * [pepsi-070] changed logging format
    * [pepsi-069] changed init_ui method order
    * [pepsi-068] edited parsing ping time, loss
    * [pepsi-067] fixed the problem that the process does not proceed when there is no ping response
    * [pepsi-066] changed applying qtmodern theme order for applying stylesheet
    * [pepsi-065] removed QGroupBox title
    * [pepsi-064] moved logger init method to main
    * [pepsi-063] changed resource reference
    * [pepsi-062] moved server_lists to Resource\Server folder
    * [pepsi-061] changed module reference
    * [pepsi-060] added ignore folder
    * module categorize
        * [pepsi-059] module categorize (UI)
        * [pepsi-059] module categorize (Thread)
        * [pepsi-058] module categorize (Result Analyze)
        * [pepsi-057] module categorize (UI Event Handler)
    * [pepsi-056] changed folder name to Resource
    * [pepsi-055] deleted test file ([TEMP] Ping Test.py)

<br>

## 1. Getting Started

### 1-1. Installation

1. Download the lastest version from [GitHub](https://github.com/pepsizerosugar/python-ping-tester/releases) or Clone
   the repository.
    1. ```git clone https://github.com/pepsizerosugar/python-ping-tester.git```

2. Build Main.py using build.bat or just run.
    1. When build is finish, you can run the PingPong.exe in the dist folder.
    2. server_list.json file at Resource\Server folder is automatically copy to dist\Resource\Server folder.
       <br>
       <img src="./Resource/Img/program_when_build_finished.PNG" alt="">
3. Or downaload the lastest binary file what name "PingPong.zip"
   from [GitHub](https://github.com/pepsizerosugar/python-ping-tester/releases) and unzip it.

### 1-2. How to use

* Edit server list
    1. Open the server_list.json file at Resource\Server.
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
    * <img src="./Resource/Img/messagebox_when_ping_finished.PNG" alt="">

## 2. Extra

### 2-1. Analyze

* Analyze of ping result is shown in log.
    * Log file is generated at Logs\ping_test_${datetime}.log
    * One for server, one for region.
