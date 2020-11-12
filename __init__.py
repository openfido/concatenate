"""OpenFIDO concatenate pipeline

This pipeline concatenates the contents of the input and writes it to the output

INPUTS

  List of input files to be concatenated. If input is omitted, input is read to /dev/stdin.

OUTPUTS

  List of transposed output files. If output omitted, output is written to /dev/stdout.

OPTIONS

  -i|--inplace   write outputs to inputs (output file list is ignored)

"""
def main(inputs,outputs,options):
	import openfido_util as of
	import pandas as pd
	of.setup_io(inputs,outputs)
	data = []
	for file in inputs:
		data.append(of.read_input(file,options))
	result = pd.concat(data)
	of.write_output(result,outputs[0],options)
	return {outputs[0],result}
