print("Enter name")
local name = tostring(io.read())

print("Enter Age")
local age = tonumber(io.read())

local tenByAge = age + 10

print("Hello "..tostring(name).." in 10 years you'll be "..tostring(tenByAge))
