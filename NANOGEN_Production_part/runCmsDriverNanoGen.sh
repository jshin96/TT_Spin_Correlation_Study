#! /bin/bash

#TODO: Make this a proper script that also creates a crab_submit file
if [[ $# -lt 2 ]]; then
    echo "Must have at least two arguments: runCmsDriverNanoGen.sh <config fragment> <outputfile> <numcores>"
    exit 1
fi

export random_seed=$(( $RANDOM % 99999 + 1 ))

customize="--customise_commands process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=$random_seed"
if [[ $# -gt 2 ]]; then
    customize="${customize}\nprocess.externalLHEProducer.generateConcurrently=True --nThreads $3"
fi

fragment=${1}
cmsDriver.py Configuration/TT_Spin_Corr/python/$fragment \
    --fileout file:$2 --mc --eventcontent NANOAODGEN \
    --datatier NANOAOD --conditions auto:mc --step LHE,GEN,NANOGEN \
    --python_filename configs/${fragment/cff/cfg} \
    $customize \
    -n 5000 --no_exec



