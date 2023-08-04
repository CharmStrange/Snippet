-- 필요한 라이브러리 불러오기 (이 예제에서는 LuaSocket을 사용합니다)
local socket = require("socket")

-- 서버 정보 설정
local serverIP = "서버_IP_주소"
local serverPort = 12345

-- 가상의 온도 센서 함수
function readTemperature()
    -- 실제 센서 동작 대신 랜덤한 값 생성
    return math.random(18, 30)
end

-- 서버로 데이터 전송 함수
function sendData(data)
    local client = socket.tcp()
    client:connect(serverIP, serverPort)
    client:send(data)
    client:close()
end

-- 주기적으로 데이터 전송
while true do
    local temperature = readTemperature()
    local data = "Temperature: " .. temperature .. "°C"
    sendData(data)

    print("Sent data: " .. data)

    -- 10초 대기
    socket.sleep(10)
end
