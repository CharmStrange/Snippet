-- LuaContainers.lua

local LuaContainers = {}
empty = {}

-- empty <-> LuaContainers
local List = {setmetatable(empty, LuaContainers)}


local Stack = {setmetatable(empty, LuaContainers)}


local Queue = {setmetatable(empty, LuaContainers)}


local Deque = {setmetatable(empty, LuaContainers)}




local LuaContainers = {List, Stack, Queue, Deque}

print(getmetatable(LuaContainers.List))


--return LuaContainers  -- Returning LuaContainers at the end
