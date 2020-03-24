import os
#import subprocess,re

def run(cmd):
	#print(subprocess.call(re.split(" ",cmd)))
	print(os.system(cmd))

# def testFilenamePrefix(filename):
# 	print("%s wheelhouse found? " % filename,end="")
# 	out = filename in [fn[:len(filename)] for fn in os.listdir("wheelhouse")]
# 	print(out)
# 	if not(out):
# 		print("Downloading %s wheelhouse" % filename)
# 	return out

try:
	print("Testing kivy installation: ",end="")
	import kivy
	print("import successful")

except:
	print("import failure")

	# #look for the simplegui wheelhouse, else download install
	# if not(testFilenamePrefix("simplequi")):
	# 	run("pip3 download -d ./wheelhouse simplequi")
	# #look for the PySide2 wheelhouse, else download install
	# if not(testFilenamePrefix("PySide2")):
	# 	#run("pip3 download -d ./wheelhouse shibokens")
	# 	run("wget 'https://files.pythonhosted.org/packages/74/f7/738a55a81eebb854c263622822e551bcff4276b96b5a8eadfed12500ee46/PySide2-5.14.0-5.14.0-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl'")
	# 	run("mv PySide2-5.14.0-5.14.0-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl ./wheelhouse/")

	print("Installing kivy ...")
	#run("pip3 install --no-index --find-links=./wheelhouse/ --ignore-installed simplequi")
	run("date >> nohup.out")
	run("pip3 install --no-index --find-links=./wheelhouse/ kivy")
	run("date >> nohup.out")
	#run("rm ./wheelhouse/PySide2-5.14.0-5.14.0-cp35.cp36.cp37.cp38-abi3-manylinux1_x86_64.whl")
