print("Which number is bigger out of 2")

print("Enter value 1")
local value1 = tonumber(io.read())

print("Enter value 2")
local value2 = tonumber(io.read())

if value1 > value2 then
  print(value1 .. " is the biggest")

elseif value1 == value2 then
  print("The values are the same")

else
  print(value2 .. " is the biggest")
end