local lib = require("lib")

lib.print("INCREDIBLE, you have managed to run this lua module successful, good job!")
lib.print("As a reward, here are the runtime search paths used for the lua interpreter:")
lib.print("Lua paths: " .. package.path)
lib.print("C paths: " .. package.cpath)

---@type et_Obituary
function et_Obituary(target, _attacker, _meansOfDeath)
	-- every time player '0' dies, we `map oasis` - incredibly practical!
	if target == 0 then
		lib.map("battery")
	end
end

-- add the '---@type <same-hook-name>' annotation for some additional parameter checks (like arity) ↓
---@type et_RunFrame
function et_RunFrame(levelTime, _foo --[[ ← luals complains about `redundant-parameter` here due to the @type annotation above ]])
	-- ↑ prefixing a parameter/variable with `_` makes luals not complain about `unused-local` - see `./.luarc.json`
	local unused --[[ ← not prefixed with `_`, so luals complains ]]

	-- print the host ipv4 addr every second
	if levelTime % 1000 == 0 then
		lib.print(levelTime .. " IPv4 is still: " .. lib.status_serveripv4())
	end
end
