grassplaceX := 1152
grassplaceY := 401

breakplaceX := 1236
breakplaceY := 663

itemlaserX:=832
itemlaserY:=704

F1::
    loop{ ; root 루프는 부숴야 할 아이템을 주기적으로 선택하는 역할, 끊김없이 아이템 공급을 해 줄 수 있음
        MouseMove, %itemlaserX%, %itemlaserY%, 3

        loop, 180{ ; 루프 반복 회수는 '몇 개의 블록을 설치하고 부수냐'
            MouseMove, %grassplaceX%, %grassplaceY%, 4.5
            MouseMove, %breakplaceX%, %breakplaceY%, 2.5
            Sleep, 1200
        }
    }

F3::
    ExitApp
