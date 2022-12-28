-- Program to output the number of days in the month given the month as a number:
print("Please enter the month's number:")
local month = tonumber(io.read("*n"))

-- 4 months have 30 days.

local days_print_output = "Number of days in this month is: "

if month == 4 or month == 6 or month == 9 or month == 11 then
    print(days_print_output .. "30 days")
elseif month == 2 then
    print(days_print_output .. "28 days; 29 if leap year.")
else
    print(days_print_output .. "31")
end
