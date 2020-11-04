"""OpenFIDO concatenate pipeline

This pipeline concatenates the contents of the input and writes it to the output

INPUTS

  List of input files to be concatenated.

OUTPUTS

  List of transposed output files. If output omitted, output is written to /dev/stdout.

OPTIONS

  -i|--inplace   write outputs to inputs (output file list is ignored)

"""
import os, csv, pandas
def main(inputs,outputs,options):
	if not inputs:
		raise Exception("missing inputs")
	if outputs:
		if len(outputs) > 1 :
			raise Exception("too many outputs")
	else:
		outputs = ["/dev/stdout"]
	result = []
	for file in inputs:
		if not file:
			raise Exception("missing input")
		data = pandas.read_csv(file,header=None)
		result.append(data)
	result = pandas.DataFrame(pandas.concat(result))
	result.to_csv(outputs[0],header=False,index=False)
	return result
