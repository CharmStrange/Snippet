; 변수 초기화

; AutoHotkey WindowSpy를 사용해 클라이언트 상 Window 좌표를 입력
grassplaceX := 1152
grassplaceY := 401

breakplaceX := 1236
breakplaceY := 663

itemgrassX:=832
itemgrassY:=704

F1::
    loop{
        MouseMove, %itemgrassX%, %itemgrassY%, 3

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
