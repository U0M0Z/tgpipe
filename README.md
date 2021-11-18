![logo for tgboost](./images/tgBoost_logo.png)


## tgBoost
tgBoost is a **pipeline framework** to be used to develop predictive models of chemical species from SMILES notations. The pipeline comes with a **ML model** that predicts the glasss transition temperature (<em>T</em><sub>g</sub>) of organic compounds.

## Motivation
tgBoost is a kickstart project aiming at expanding the use of Machine Learning (ML), Data Engineering and Quantitative Structure–Property Relationships (QSPR) in Physical Chemistry.

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

The tgBoost library needs the independent installation of rdkit via conda-forge:

`conda install -c conda-forge rdkit`

## Build status
Build status of continus integration i.e. travis, appveyor etc. Ex. - 

[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

#### Documentation
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
