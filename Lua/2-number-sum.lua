print("Variable A float:")
variable_a = tonumber(io.read())
print("Variable B float:")
variable_b = tonumber(io.read())

print("Which sum?\n1. addition + \n2. subtraction - \n3. multiplication *\n4. division /\n5. All\n")
-- Declare variables to store the input values
local variable_a, variable_b

-- Prompt the user to enter the values for variable_a and variable_b
-- and store the input in the corresponding variables
print("Variable A float:")
variable_a = tonumber(io.read())
print("Variable B float:")
variable_b = tonumber(io.read())

-- Declare a table of function names and function definitions
-- for each operation
local operations = {
  ["addition"] = function(a, b) return a + b end,
  ["subtraction"] = function(a, b) return a - b end,
  ["multiplication"] = function(a, b) return a * b end,
  ["division"] = function(a, b) return a / b end,
}

-- Prompt the user to choose an operation
print("Which operation do you want to perform?\n1. addition + \n2. subtraction - \n3. multiplication *\n4. division /\n")
local operation_choice = tonumber(io.read())

-- Get the name of the chosen operation
local operation_name
if operation_choice == 1 then
  operation_name = "addition"
elseif operation_choice == 2 then
  operation_name = "subtraction"
elseif operation_choice == 3 then
  operation_name = "multiplication"
elseif operation_choice == 4 then
  operation_name = "division"
else
  -- If the user entered an invalid choice,
  -- print an error message and exit the program
  print("Invalid choice.")
  return
end

-- Perform the chosen operation
local result = operations[operation_name](variable_a, variable_b)

-- Print the result
print(result)