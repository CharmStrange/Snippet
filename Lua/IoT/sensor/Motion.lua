-- PIR 센서 핀 설정
local pirPin = 2  -- GPIO 핀 번호

-- 움직임 감지 함수
function detectMotion()
    local motion = gpio.read(pirPin)
    if motion == gpio.HIGH then
        print("Motion detected! Alarm activated.")
        -- 여기에 경보 활성화 코드 추가
    else
        print("No motion.")
        -- 여기에 경보 비활성화 코드 추가
    end
end

-- 주기적으로 움직임 감지
while true do
    detectMotion()
    tmr.delay(1000000)  -- 1초 대기
end
