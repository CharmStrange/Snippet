-- LuaContainers.lua

local LuaContainers = {}

local List = {}
setmetatable(List, LuaContainers)
print(getmetatable(List))

local DynamicList = {}
setmetatable(DynamicList, LuaContainers)
print(getmetatable(DynamicList))

local Stack = {}
setmetatable(Stack, LuaContainers)
print(getmetatable(Stack))

local Queue = {}
setmetatable(Queue, LuaContainers)
print(getmetatable(Queue))

local Deque = {}
setmetatable(Deque, LuaContainers)
print(getmetatable(Deque))

return LuaContainers  -- Returning LuaContainers at the end
