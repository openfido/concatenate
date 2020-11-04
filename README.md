OpenFIDO Library Documentation: concatenate

NAME
    concatenate - OpenFIDO concatenate pipeline

DESCRIPTION
    This pipeline concatenates the contents of the input and writes it to the output

    INPUTS

      List of input files to be concatenated.

    OUTPUTS

      List of concatenated output files. If output omitted, output is written to /dev/stdout.

    OPTIONS

      -i|--inplace   write outputs to inputs (output file list is ignored)
      
FILE
    `/usr/local/share/openfido/concatenate/__init__.py`
