
io.write(' What is your name? ')--input the name--
local name = io.read()--save the name--
local name = string.upper(name)--turn it to upper--
local NameCheck = 'HUGH'--check name against--

if string.find(name, NameCheck) then
	print("hi hugh")
else
	print ("Not hugh")
end



