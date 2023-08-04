-- 필요한 라이브러리 불러오기
local httpServer = require("http.server")
local json = require("json")

-- LED 핀 설정
local ledPin = 5  -- GPIO 핀 번호
gpio.mode(ledPin, gpio.OUTPUT)

-- 웹 서버 생성
local server = httpServer.create(80)

-- LED 제어 핸들러
function ledHandler(req, res)
    if req.method == "POST" then
        local data = json.decode(req.body)
        if data.action == "on" then
            gpio.write(ledPin, gpio.HIGH)
        elseif data.action == "off" then
            gpio.write(ledPin, gpio.LOW)
        end
        res:send(json.encode({ status = "success" }))
    end
end

-- 핸들러 연결
server:route("/led", ledHandler)

-- 서버 실행
server:start()
