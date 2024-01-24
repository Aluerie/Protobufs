# Fork information

This fork is used to compile `.proto` files into mirrored Python `.py` files with `betterproto` compiler. Those files are later edited to be used in <https://github.com/Gobot1234/steam.py> (or partially)

This repository contains extra content.

* `proto.exe` - from <https://github.com/protocolbuffers/protobuf/releases/>.
* `compile.ps1` file in it for easy compiling files in batches.
* compiled .py proto-mirrors for
    * `./dota2/py_mirrors` - Dota 2

Unfortunately, `betterproto` doesn't type-hint stuff properly so those should be manually (or chat gpt^tm) corrected.

## Notes to remember

* Before using `compile.ps1` remember to setup to venv with `pip install "betterproto[compiler]"` installed.
* Remember to paste google `descriptor.proto` dependency if it isn't present.
* I only compiled dota2 `.proto`-files but it should work for other folders as well

## Automatically tracked protobufs for Steam and Valve's games

These protobufs are being dumped as updates come in the [SteamTracking](https://github.com/SteamDatabase/SteamTracking) repository.

Protobufs are dumped using [SteamKit's protobuf dumper](https://github.com/SteamRE/SteamKit/tree/master/Resources/ProtobufDumper).

For protobufs dumped from javascript files (in webui folder), we have a [separate dumper](https://github.com/SteamDatabase/SteamTracking/blob/master/dump_javascript_protobufs.mjs) which parses javascript files into abstract syntax tree and tries to find all the messages and services. As such, these dumps are not as complete as dumps from binary files because minified javascript files lack some information.
