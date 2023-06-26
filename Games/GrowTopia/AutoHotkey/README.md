### 여기 위치한 오토핫키(ahk)파일들은 전부 GrowTopia 자동 농장 시스템의 일부

클라이언트의 무한 터치 버그를 활용 : LaserGird.ahk 설명

*EXECUTE ahk File -> Client FullScreen Mode -> Touch Button On -> CLick Punch Button and PRESS 'Alt Tab' -> Return to Client -> PRESS F1*
```
; 변수 초기화

; AutoHotkey WindowSpy를 사용해 클라이언트 상 Window 좌표를 입력
grassplaceX := 1152
grassplaceY := 401

breakplaceX := 1236
breakplaceY := 663

itemlaserX:=832
itemlaserY:=704

F1::
    loop{
        MouseMove, %itemlaserX%, %itemlaserY%, 3

        loop, 10{
            MouseMove, %grassplaceX%, %grassplaceY%, 4.5
            MouseMove, %breakplaceX%, %breakplaceY%, 2.5
            ; Sleep 다음의 인자를 800으로 두면 Grass, Pepper 등의 농사
            Sleep, 1200
        }
    }

; F3 누르면 앱 종료
F3::
    ExitApp
```
