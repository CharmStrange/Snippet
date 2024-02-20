-- LuaContainers.lua

List = {}
Stack = {}
Queue = {}
Deque = {}
LuaContainers = {List, Stack, Queue, Deque}

function List:new()
    local container = setmetatable({}, self)

    function container:INSERT(value)
        container.insert(value)
    end
    
    function continaer:REMOVE(index)
        container.remove(container, index)
    end
    
    function container:CLEAR()
        
    end
    
    return container
    
end

function Stack:new()
    local container = setmetatable({}, self)
    
    function container:INSERT(value)
        container.insert(value)
    end
    
    function continaer:REMOVE(index)
        container.remove(container, index)
    end
    
    function container:CLEAR()
        
    end
    
    return container
end

function Queue:new()
    local container = setmetatable({}, self)
    
    function container:INSERT(value)
        container.insert(value)
    end
    
    function continaer:REMOVE(index)
        container.remove(container, index)
    end
    
    function container:CLEAR()
        
    end
    
    return container
end

function Deque:new()
    local container = setmetatable({}, self)
    
    function container:INSERT(value)
        container.insert(value)
    end
    
    function continaer:REMOVE(index)
        container.remove(container, index)
    end
    
    function container:CLEAR()
        
    end
    
    return container
end

--return LuaContainers  -- Returning LuaContainers at the end
