-- test.lua

local LuaContainers = require("LuaContainers")

-- Create a List
local list = LuaContainers.List.new()

-- Add items to the list
list:add(1)
list:add(2)
list:add(3)

-- Check if the list contains a specific item
print("Does list contain 2?", list:contains(2))  -- Output: true

-- Remove an item from the list
list:remove(2)

-- Get the size of the list
print("Size of list:", list:size())  -- Output: 2

-- Get an item from the list
print("Item at index 1:", list:get(1))  -- Output: 1

-- Clear the list
list:clear()

-- Create a Stack
local stack = LuaContainers.Stack.new()

-- Push items onto the stack
stack:push(10)
stack:push(20)
stack:push(30)

-- Peek at the top item of the stack
print("Top item of stack:", stack:peek())  -- Output: 30

-- Pop an item from the stack
print("Popped item from stack:", stack:pop())  -- Output: 30

-- Create a Queue
local queue = LuaContainers.Queue.new()

-- Enqueue items into the queue
queue:enqueue(100)
queue:enqueue(200)
queue:enqueue(300)

-- Peek at the front item of the queue
print("Front item of queue:", queue:peek())  -- Output: 100

-- Dequeue an item from the queue
print("Dequeued item from queue:", queue:dequeue())  -- Output: 100

-- Create a Deque
local deque = LuaContainers.Deque.new()

-- Push items onto the front and back of the deque
deque:pushFront(1)
deque:pushFront(2)
deque:pushBack(3)
deque:pushBack(4)

-- Peek at the front and back items of the deque
print("Front item of deque:", deque:peekFront())  -- Output: 2
print("Back item of deque:", deque:peekBack())    -- Output: 4

-- Pop items from the front and back of the deque
print("Popped front item from deque:", deque:popFront())  -- Output: 2
print("Popped back item from deque:", deque:popBack())    -- Output: 4
