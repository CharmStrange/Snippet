-- 필요한 라이브러리 불러오기 (이 예제에서는 GPIO 라이브러리를 사용합니다)
local GPIO = require("periphery").GPIO

-- LED 핀 설정
local ledPin = GPIO("/dev/gpiochip0", 17, "out")

-- LED 켜기 함수
function turnOnLED()
    ledPin:write(true)
    print("LED is on")
end

-- LED 끄기 함수
function turnOffLED()
    ledPin:write(false)
    print("LED is off")
end

-- LED 제어 반복
while true do
    turnOnLED()
    os.execute("sleep 1")  -- 1초 대기
    turnOffLED()
    os.execute("sleep 1")  -- 1초 대기
end
