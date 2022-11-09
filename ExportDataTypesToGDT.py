# Export data types and function definitions (from program analysis and DWARF) to an external GDT file

#@author Andrea Oliveri
#@category Exporter
#@keybinding 
#@menupath 
#@toolbar 

from ghidra.app.cmd.function import CaptureFunctionDataTypesCmd
from ghidra.app.script import GhidraScript
from ghidra.program.model.data import FileDataTypeManager
from ghidra.app.cmd.function import CaptureFunctionDataTypesListener
from ghidra.app.util.bin.format.dwarf4.next import DWARFProgram
from java.io import File

# Check if the file has DWARF4 symbols
if not DWARFProgram.isDWARF(currentProgram):
	print("No DWARF info available!")
	exit(0)

# Create GDT archive
gdtfile = File(currentProgram.getName() + ".gdt")
gdtarchive = FileDataTypeManager.createFileArchive(gdtfile)

# Dump DWARF info
class Listener(CaptureFunctionDataTypesListener):
	def captureFunctionDataTypesCompleted(cmd):
		print("Data capture completed!")
cmd = CaptureFunctionDataTypesCmd(gdtarchive, currentProgram.getMemory(), Listener())
cmd.applyTo(currentProgram)

gdtarchive.save()
gdtarchive.close()

