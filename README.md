![logo for tgboost](./images/tgBoost_logo.png)


## tgBoost
tgBoost is a **pipeline** englobing QSPR model optimized for the prediction of the glass transition temperature (<em>T</em><sub>g</sub>) of monomer organic compounds. The pipeline is based on [mol2vec](https://mol2vec.readthedocs.io/en/latest/), a **machine learning** (ML) algorithm converting molecular SMILES into molecular embeddings. The pipeline can be exapanded to include further QSAR/QSPR models developed from SMILES notation.

## Motivation
tgBoost is a kickstart project aiming at expanding the use of ML, Data Engineering and QSAR/QSPR models in atmospheric and physical chemistry. The pipeline comes with a pretrained and ML powered QSPR model predicting <em>T</em><sub>g</sub> of monomer organic compounds. The model is based on a Extreme Gradient Boosting framework ([XGBoost](https://xgboost.readthedocs.io/en/stable/)) and it is developed from the largest dataset of experimental <em>T</em><sub>g</sub> of monomer organic molecules ([Koop et al., 2011](https://pubs.rsc.org/en/content/articlelanding/2011/cp/c1cp22617g)).

## Requirements
* **Python >=3.6.0** (Python 2.x is [not supported](http://www.python3statement.org/))
* [NumPy](http://www.numpy.org/)
* [pandas](http://pandas.pydata.org/)
* [scikit-learn](http://scikit-learn.org/stable/)
* [gensim](https://radimrehurek.com/gensim/)
* [RDKit](http://www.rdkit.org/docs/Install.html)
* [mol2vec](https://github.com/samoturk/mol2vec)
* [xgboost](https://pypi.org/project/xgboost/)

## Installation
`pip install https://github.com/U0M0Z/tgpipe`

tgBoost library needs the independent installation of mol2vec via pip within the working environment:

`pip install git+https://github.com/samoturk/mol2vec`

## Build status
Build status of continus integration i.e. travis, appveyor etc. Ex. - 

[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

#### Documentation
Details on the statistical analysis performed to develop the model and pipeline are found in the supporting [article](https://pubs.rsc.org/en/content/articlelanding/2022/ea/d1ea00090j#!divRelatedContent&articles). 

## Usage
## Basic use
This code uses the tgPipeline to train tgBoost a QSPR model for <em>T</em><sub>g</sub> prediction. The QSPR model is based on rdkit, mol2vec and xgboost. In order to use the model on your machine, you need to retrain the model to be conform to the C++ signature of your processor. 

The tgBoost model is built, trained, and saved in ``` ./trained_models ``` with the command:
```
python tgPipeline/tgboost/train_pipeline.py
```

Check for the following message to confirm successful model training:

```
*** EXTRACTION step
n_input SMILES:  415 

*** TRANSFORMING step
n_output SMILES:  298 

~~ DATA info
Xtrain:  298 ytrain:  298 Xtest:  0 ytest:  0 

*** REGRESSION step

PIPELINE completed:
_ ~ ^ ~ _ ~ _ ~ ^ ~ _ ~ _ ~ ^ ~ _ ~ ^ ~ _ ~ ^ ~ _
  __       ___                __ 
 / /____ _/ _ )___  ___  ___ / /_
/ __/ _ `/ _  / _ \/ _ \(_-</ __/
\__/\_, /____/\___/\___/___/\__/ 
   /___/                         
_ ~ ^ ~ _ ~ _ ~ ^ ~ _ ~ _ ~ ^ ~ _ ~ ^ ~ _ ~ ^ ~ _
```



### As python module
```python
from tgboost import tgboost.processing.smiles_manager as sm
from tgboost import predict
```
The **first line** imports functions to open and preprocess files containing SMILES used for predictions, and the **second line** imports functions for predicting <em>T</em><sub>g</sub> of SMILES.

Check notebooks [repository](https://github.com/U0M0Z/tgpipe/tree/main/tgboost/notebooks) for examples and details. 

### How to cite?

✨ 🍰 ✨

```bib
@Article{D1EA00090J,
author ="Galeazzo, Tommaso and Shiraiwa, Manabu",
title  ="Predicting glass transition temperature and melting point of organic compounds via machine learning and molecular embeddings",
journal  ="Environ. Sci.: Atmos.",
year  ="2022",
volume  ="2",
issue  ="3",
pages  ="362-374",
publisher  ="RSC",
doi  ="10.1039/D1EA00090J",
url  ="http://dx.doi.org/10.1039/D1EA00090J"
}
```

## Contribute
Contact at tommaso.galeazzo@gmail.com

## Credits
Initial development was supported by [AirUCI](https://airuci.uci.edu), Irvine, CA.

## License
BSD 3-clause © [Tommaso Galeazzo](https://www.tmsglz.com)
