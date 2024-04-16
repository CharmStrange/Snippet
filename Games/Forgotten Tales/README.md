# [forgotten Tales Online](https://forum.dmgamestudio.com/index.php)

# [Omega Vanitas](https://ov.dmgamestudio.com/index.php)

[Official Forgotten Tales PC version](https://forum.dmgamestudio.com/viewtopic.php?t=17401)

[Quick Download](https://dmgamestudio.com/files/ft8.zip)

Windows - Execute `start.bat`

Linux - Execute `start.sh`

`start.bat` and `start.sh` file can be edited with writing utilities.

---

# How to execute 2+ applications at once?
this is how I did:

![image](https://github.com/CharmStrange/Snippet/assets/105769152/5944d3cb-4ab1-4c68-aecb-fbfcc88d3d61)

Make 3 separate .jar files.

And open game directory using `Windows Powershell`, type this :
```
Start-Process java -ArgumentList "-jar desktop1.jar 660 320" -NoNewWindow
Start-Process java -ArgumentList "-jar desktop2.jar 660 320" -NoNewWindow
Start-Process java -ArgumentList "-jar desktop3.jar 660 320" -NoNewWindow
```
`660 320` is size of client, it is customizable. 

Actually, there's no need to do like that, just execute separate files! But you should know, same file cannot open twice, all clients must be different process(file).

![image](https://github.com/CharmStrange/Snippet/assets/105769152/6bc29031-2933-425c-b69b-d1768b0d07c5)

https://dmgamestudio.com/
