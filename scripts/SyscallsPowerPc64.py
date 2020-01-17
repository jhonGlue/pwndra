# Annotate Linux/PowerPC64 system calls and arguments.
#@author b0bb
#@category Pwn
#@keybinding
#@menupath Analysis.Pwn.Syscalls.powerpc64
#@toolbar 

from lib.Syscalls import Syscalls
import ghidra.app.util.opinion.ElfLoader as ElfLoader

def run():

    if currentProgram.getExecutableFormat() != ElfLoader.ELF_NAME:
        popup('Not an ELF file, cannot continue')
        return

    arch = 'powerpc64'
    abi  = 'default'

    obj = Syscalls(currentProgram, currentSelection, monitor, arch, abi)


run()