# etlegacy-luals-example
Shows an example of how to use upstream luals-definitions to get IDE/Editor
intellisense and documentation for ET:Legacy lua functionality.

Watch it in action: <https://youtu.be/kt4jnDGUR70>

To use for your own lua scripts repository:

- copy [`./.luarc.json`](./.luarc.json)  
- copy [`./defs/etlegacy-luals-definitions.lua`](./defs/etlegacy-luals-definitions.lua) (and see inside how to update it)

Intellisense should then work out of the box for your lua scripts, e.g. check
for autocompleting `et.` to see all available functions/hooks/constants.

**NOTE**: Hook functions (`et_*`) benefit from being annotated with `---@type` annotations,
see [`./example.lua`](./example.lua) for how.

## For Editing/IDE
e.g. get `vscode`, install the luals extension:
<https://open-vsx.org/vscode/item?itemName=sumneko.lua>, open the project 
`$ code .` and check [`./example.lua`](./example.lua) for some warnings/errors, jump to etc.

## Quickstarting/testing the lua script
run e.g. `./quickstart.py "$(which etl.x86_64)" "$HOME/.etlegacy"`

the console output should entail `[luals-example]` messages printed by the
example lua script
