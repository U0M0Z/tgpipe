![logo for tgApp](./images/tgApp_logo.png)


## tgApp
tgApp is a **pipeline framework** to be used to develop predictive models of chemical species from SMILES notations. The pipeline comes with a **ML model** that predicts the Transition glass temperature (T<sub>g</sub>) of organic compounds.

## Motivation
tgApp is a kickstart project aiming at expanding the use of Machine Learning (ML), Data Engineering and Quantitative Structure–Property Relationships (QSPR) in Physical Chemistry.

## Requirements
* **Python >=3.6.0** (Python 2.x is [not supported](http://www.python3statement.org/))
* [NumPy](http://www.numpy.org/)
* [pandas](http://pandas.pydata.org/)
* [scikit-learn](http://scikit-learn.org/stable/)
* [gensim](https://radimrehurek.com/gensim/)
* [RDKit](http://www.rdkit.org/docs/Install.html)
* [mol2vec](https://github.com/samoturk/mol2vec)
* [xgboost](https://pypi.org/project/xgboost/)

## Build status
Build status of continus integration i.e. travis, appveyor etc. Ex. - 

[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

#### Documentation
TODO

## Usage
### As python module
```python
from tgApp import tg_regression_model.processing.smiles_manager as sm
```

## Contribute
Contact at tommaso.galeazzo@gmail.com

## Credits
Initial development was supported by [AirUCI](https://airuci.uci.edu), Irvine, CA.

## License
BDS-3 © [Yourname](Tommaso Galeazzo)