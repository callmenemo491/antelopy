"""Extra type hinting types"""
from typing import Literal

ValidTypes = Literal[
    "bool",
    "int8",
    "uint8",
    "int16",
    "uint16",
    "int32",
    "uint32",
    "int64",
    "uint64",
    "int128",
    "uint128",
    "varint32",
    "varuint32",
    "float32",
    "float64",
    "float128",
    "time_point",
    "time_point_sec",
    "block_timestamp_type",
    "name",
    "bytes",
    "string",
    "checksum160",
    "checksum256",
    "checksum512",
    "public_key",
    "signature",
    "symbol",
    "symbol_code",
    "asset",
    "extended_asset",
]