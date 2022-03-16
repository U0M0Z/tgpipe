![logo for tgboost](./images/tgBoost_logo.png)


## tgBoost
tgBoost is a **pipeline** and QSPR model optimized for the prediction of the glass transition temperature (<em>T</em><sub>g</sub>) of monomer organic compounds. The pipeline is based on [mol2vec](https://mol2vec.readthedocs.io/en/latest/), a **machine learning** (ML) algorithm converting molecular SMILES into molecular embeddings. The pipeline can be enriched with further QSAR/QSPR models developed from SMILES notation.

## Motivation
tgBoost is a kickstart project aiming at expanding the use of ML, Data Engineering and QSAR/QSPR models in atmospheric and physical chemistry. The pipeline comes with a pretrained ML which predicting <em>T</em><sub>g</sub> of monomer organic compounds. The model is based on a Extreme Gradient Boosting framework ([XGBoost](https://xgboost.readthedocs.io/en/stable/)) and it is developed from the largest dataset of <em>T</em><sub>g</sub> measurements of monomer organic molecules ([Koop et al., 2011](https://pubs.rsc.org/en/content/articlelanding/2011/cp/c1cp22617g)).

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
`pip install https://github.com/U0M0Z/tgboost`

tgBoost library needs the independent installation of rdkit via conda-forge:

`conda install -c conda-forge rdkit`

## Build status
Build status of continus integration i.e. travis, appveyor etc. Ex. - 

[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

#### Documentation
Detailed study about tgBoost development and 

✨ 🍰 ✨
TODO

## Usage
### As python module
```python
from tgboost import tgboost.processing.smiles_manager as sm
```

## Contribute
Contact at tommaso.galeazzo@gmail.com

## Credits
Initial development was supported by [AirUCI](https://airuci.uci.edu), Irvine, CA.

## License
BSD 3-clause © [Tommaso Galeazzo](https://www.tmsglz.com)
