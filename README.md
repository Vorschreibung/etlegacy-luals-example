# etlegacy-luals-example
Shows an example of how to use upstream luals-definitions to get IDE/Editor
intellisense for ET:Legacy lua scripts.

To use for your own lua scripts repository:

- copy `./.luarc.json`
- copy `./defs/etlegacy-luals-definitions.lua` (and see inside how to update it)

## For Editing/IDE
e.g. get `vscode`, install the luals extension:
<https://open-vsx.org/vscode/item?itemName=sumneko.lua>, open the project 
`$ code .` and check `example.lua` for some warnings/errors, jump to etc.

## Quickstarting/testing the lua script
run e.g. `./quickstart.py "$(which etl.x86_64)" "$HOME/.etlegacy"`

the console output should entail `[luals-example]` messages printed by the
example lua script
