apiRequest(0.1)

local eeObj = getEEObject()
local emuObj = getEmuObject()

local patcher = function()
eeObj.WriteMem32(0x0000, 0x1111)
eeObj.WriteMem32(0x0000, 0x2222)
end
emuObj.AddVsyncHook(patcher)
