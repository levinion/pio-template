import os

Import("env")

env.Replace(COMPILATIONDB_INCLUDE_TOOLCHAIN=True)

env.Replace(COMPILATIONDB_PATH="build/compile_commands.json")
