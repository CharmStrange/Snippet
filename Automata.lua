setFunction={}
setFunction["String"]={}
setFunction["newString"]={}
function setFunction.B_State()
    for i=1, 26 do
        table.insert(setFunction["String"], string.char(i+96))
        --check : print(setFunction["String"][i])
    end
    return setFunction["String"]
end
--[[ ASCII 0~127 ]]
function setFunction.Func(KEY) -- KEY : 1 ~ 101
    print("\nInitial String is { a, b, d, ... z }.\nApplying Function... KEY is", KEY)
    for i=1, 26 do
        table.insert(setFunction["newString"], i+KEY)
    end
    return setFunction["newtring"]
end
--
function setFunction.Automata(Number)
    print("BeforeState:")
    for i=1, 26 do
        print(setFunction["String"][i])
    end
    
    setFunction.Func(Number)
    print("AfterState")
    for i=1, 26 do
        print(setFunction["newString"][i])
    end
    return setFunction["newString"]
end
--
