-- DHT22 센서 라이브러리 불러오기
local dht = require("dht")

-- DHT22 핀 설정
local dhtPin = 4  -- GPIO 핀 번호

-- 센서 데이터 읽기 함수
function readDHTSensor()
    local status, temp, humi = dht.read(dhtPin)
    if status == dht.OK then
        print(string.format("Temperature: %.1f°C, Humidity: %.1f%%", temp, humi))
    else
        print("Failed to read DHT22 sensor data")
    end
end

-- 주기적으로 센서 읽기
while true do
    readDHTSensor()
    tmr.delay(5000000)  -- 5초 대기
end
