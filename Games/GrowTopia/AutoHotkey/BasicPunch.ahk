; 변수 초기화
start := 1

; X, Y 좌표는 WindowSpy를 사용해 적합한 좌표 탐색
grassplaceX := 1015
grassplaceY := 419

breakplaceX := 1236
breakplaceY := 663

loop {
    if (start = 1) {
        MouseMove, %grassplaceX%, %grassplaceY%, 10

        MouseMove, %breakplaceX%, %breakplaceY%, 0
        Sleep, 800
    }
    else if (start = 0) {
        break
    }
}

; F2 누르면 종료
F2::
    start := 0
    return
