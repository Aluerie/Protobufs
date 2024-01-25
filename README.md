# 🍴 Fork Information

This fork is used to compile `.proto` files into mirrored Python `.py` files with `betterproto` compiler. Those files or their part are later edited to be used in [Gobot1234/steam.py](<https://github.com/Gobot1234/steam.py>).

The repository contains extra content:

* `proto.exe` - from [protobuf/releases](<https://github.com/protocolbuffers/protobuf/releases/>).
* `compile.ps1` file in it for easy compiling files in batches.
* compiled `.py` proto-mirrors for
    * Dota 2: `./dota2/py_mirrors`

## 🆘 TODO

* [ ] Script to fix `.py` files
    * [ ] `CMsg` and similar `k_msg_something` pointless prefixes
    * [ ] `GC` pointless prefixes to enums (but keep GCToClient or similar ones)
    * [ ] Remove `DOTA` prefixes
    * [ ] When they repeat class name in enums vars - remove it from enum var names
    * [ ] PascalCase for enum variables and class names
    * [ ] ^Meaning remove `_` from them too
    * [ ] `@dataclass` into `@dataclass(eq=False, repr=False)`
    * [ ] Change `List` to `list`
    * [ ] Remove " in their `List["Something"]`
    * [ ] add `from __future__ import annotations`
    * [ ] Add one line-break before that^ and after `#` disclaimer comments
    * [ ] resolve `TYPE_CHECKING` relative imports from other files
    * [ ] Change `Optional` to `| None`
    * [ ] Reformat with black/isort/ruff in case some strings went below line limit or something
* [ ] Edit `compile.ps1`
    * [ ] include check if `betterproto[compiler]` is installed
    * [ ] Paste google `descriptor.proto` dependency to compiling folder if it isn't present.
    * [ ] Pull/Merge from Parent Repo
    * [ ] Loop over all root folders like `csgo`, `steam`, `tf2`
    * [ ] Clean up empty directories it sometimes makes
* [ ] Rethink folder structure - is there anything better than trashing everything into extra folder.

## 💡 Notes to remember

* Before using `compile.ps1` remember to setup to venv with `pip install "betterproto[compiler]"` installed.
* Remember to paste google `descriptor.proto` dependency if it isn't present.
* I only compiled dota2 `.proto`-files but it should work for other folders as well

## Automatically tracked protobufs for Steam and Valve's games

These protobufs are being dumped as updates come in the [SteamTracking](https://github.com/SteamDatabase/SteamTracking) repository.

Protobufs are dumped using [SteamKit's protobuf dumper](https://github.com/SteamRE/SteamKit/tree/master/Resources/ProtobufDumper).

For protobufs dumped from javascript files (in webui folder), we have a [separate dumper](https://github.com/SteamDatabase/SteamTracking/blob/master/dump_javascript_protobufs.mjs) which parses javascript files into abstract syntax tree and tries to find all the messages and services. As such, these dumps are not as complete as dumps from binary files because minified javascript files lack some information.
