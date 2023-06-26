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
            Sleep, 1200
        }
    }

F3::
    ExitApp
