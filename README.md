NAME
    concatenate - OpenFIDO concatenate pipeline

DESCRIPTION
    This pipeline concatenates the contents of the input and writes it to the output
    
    INPUTS
    
      List of input files to be concatenated. If input is omitted, input is read to /dev/stdin.
    
    OUTPUTS
    
      List of transposed output files. If output omitted, output is written to /dev/stdout.
    
    OPTIONS
    
      -i|--inplace   write outputs to inputs (output file list is ignored)

PACKAGE CONTENTS


FUNCTIONS
    main(inputs, outputs, options)

