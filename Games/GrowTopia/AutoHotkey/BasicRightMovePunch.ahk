SetTitleMatchMode, 2

; F9 눌러 시작, F10 눌러 정리, F1 눌러 종료

F9::
    ;MouseClick, left, -286, 450, 5, 1
    Loop, 107
    {
        ControlSend,, {Space down}, ahk_exe Growtopia.exe
        Sleep 1550

        ControlSend,, {Space up}, ahk_exe Growtopia.exe
        
        ControlSend,, {D down}, ahk_exe Growtopia.exe
        Sleep 420

        ControlSend,, {D up}, ahk_exe Growtopia.exe
        
        if(GetKeyState("F10", "P"))
            break

    }
return

F1::ExitApp
