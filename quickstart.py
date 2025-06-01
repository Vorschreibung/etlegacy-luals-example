#!/usr/bin/env python3
import sys
import os
import subprocess
import shutil

from pathlib import Path

LUA_MODULE = "example.lua"
LUA_LIB = "lib.lua"


def mkdir_p(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    return path


def cp(src: Path, dst: Path):
    shutil.copy2(src, dst)


def die(*msgs, exit_status=1):
    print(*msgs, file=sys.stderr)
    exit(exit_status)


def main(args):
    # First copy lua files
    if not os.path.isfile(args.etl_binary):
        die("Pass an existing etl_binary")

    homepath = Path(args.etl_homepath)

    if not homepath.joinpath("legacy").exists():
        die("Pass an existing '<etl-homepath>/legacy' like")

    lualibs_d = mkdir_p(homepath.joinpath("legacy", "lualibs"))
    luascripts_d = mkdir_p(homepath.joinpath("legacy", "luascripts"))

    cp(Path(f"./{LUA_LIB}"), lualibs_d)
    cp(Path(f"./{LUA_MODULE}"), luascripts_d)

    # Second run the game with some arguments
    subprocess.check_call(
        [
            args.etl_binary,
            "+set",
            "lua_modules",
            Path("luascripts").joinpath(f"{LUA_MODULE}"),
            "+set",
            "sv_pure",
            "0",
            "+devmap",
            "battery",
        ]
    )


def cli():
    import argparse

    parser = argparse.ArgumentParser(
        description="Quickly copy lua files to the correct location and run the game with them"
    )

    parser.add_argument(
        "etl_binary", type=str, help="Path to the ET:L binary/executable"
    )
    parser.add_argument("etl_homepath", type=str, help="Path to the ET:L homepath")

    args = parser.parse_args(sys.argv[1:])
    main(args)


if __name__ == "__main__":
    cli()
