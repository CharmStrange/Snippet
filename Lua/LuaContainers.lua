-- LuaContainers.lua

-- Define the LuaContainers class
local LuaContainers = {}

-- List Class
LuaContainers.List = {
  new = function()
    return {}
  end,
  
  add = function(list, item)
    table.insert(list, item)
  end,
  
  remove = function(list, index)
    table.remove(list, index)
  end,
  
  size = function(list)
    return #list
  end,
  
  get = function(list, index)
    return list[index]
  end,
  
  clear = function(list)
    for k in ipairs(list) do
      list[k] = nil
    end
  end,
  
  contains = function(list, item)
    for _, value in ipairs(list) do
      if value == item then
        return true
      end
    end
    return false
  end
}

-- DynamicList Class (inherits from List)
LuaContainers.DynamicList = LuaContainers.List
LuaContainers.DynamicList.add = function(list, item)
  list[#list + 1] = item
end

-- Stack Class (inherits from List)
LuaContainers.Stack = LuaContainers.List
LuaContainers.Stack.push = function(stack, item)
  table.insert(stack, item)
end
LuaContainers.Stack.pop = function(stack)
  return table.remove(stack)
end
LuaContainers.Stack.peek = function(stack)
  return stack[#stack]
end

-- Queue Class (inherits from List)
LuaContainers.Queue = LuaContainers.List
LuaContainers.Queue.enqueue = function(queue, item)
  table.insert(queue, 1, item)
end
LuaContainers.Queue.dequeue = function(queue)
  return table.remove(queue)
end
LuaContainers.Queue.peek = function(queue)
  return queue[#queue]
end

-- Deque Class (inherits from List)
LuaContainers.Deque = LuaContainers.List
LuaContainers.Deque.pushFront = function(deque, item)
  table.insert(deque, 1, item)
end
LuaContainers.Deque.popFront = function(deque)
  return table.remove(deque, 1)
end
LuaContainers.Deque.pushBack = function(deque, item)
  table.insert(deque, item)
end
LuaContainers.Deque.popBack = function(deque)
  return table.remove(deque)
end
LuaContainers.Deque.peekFront = function(deque)
  return deque[1]
end
LuaContainers.Deque.peekBack = function(deque)
  return deque[#deque]
end

return LuaContainers
