; ���� �ʱ�ȭ

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
            Sleep, 1200
        }
    }

; F3 ������ �� ����
F3::
    ExitApp