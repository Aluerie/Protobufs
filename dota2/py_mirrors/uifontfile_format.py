# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: uifontfile_format.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class CUIFontFilePB(betterproto.Message):
    font_file_name: str = betterproto.string_field(1)
    opentype_font_data: bytes = betterproto.bytes_field(2)


@dataclass
class CUIFontFilePackagePB(betterproto.Message):
    package_version: int = betterproto.uint32_field(1)
    encrypted_font_files: List[
        "CUIFontFilePackagePBCUIEncryptedFontFilePB"
    ] = betterproto.message_field(2)


@dataclass
class CUIFontFilePackagePBCUIEncryptedFontFilePB(betterproto.Message):
    encrypted_contents: bytes = betterproto.bytes_field(1)
