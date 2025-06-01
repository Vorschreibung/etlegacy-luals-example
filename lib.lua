local lib = {}

function lib.print(msg)
    et.G_Print("[luals-example] " .. msg .. "\n")
end

function lib.status_serveripv4()
	return et.trap_Cvar_Get("net_ip")
end

function lib.map(mapname)
	return et.trap_SendConsoleCommand(et.EXEC_APPEND, 'map "' .. mapname .. '"')
end

return lib
