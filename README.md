# DE-MOOT: Research on Data-driven Enterprise Raw Material Ordering and Optimal Transportation Scheme
Repository for our published paper [Research on Data-driven Enterprise Raw Material Ordering and Optimal Transportation Scheme](https://ieeexplore.ieee.org/abstract/document/9852530/)
## Abstract
Ordering and transportation optimization of raw material is a classic problem in the field of optimization. Based on the analysis, evaluation and prediction of previous data, this paper fully considers the actual situation of ordering, transshipment and storage, and establishes a multistage and large-scale mixed integer linear programming model for ordering and transporting raw materials. Combined with extensive data background, select appropriate indicators, and establish supplier evaluation systems by using entropy weight-CRITIC and RTOPSIS method. GM (1,1) is used to predict the general trend, the ARIMA model is used to predict the random fluctuation items, and a grey time series prediction model is constructed to obtain the predicted values of the data of the supply and loss rate in the next cycle. The prediction result are introduced into the planning model as parameters, and the evaluation score are used to construct a satisfaction function. The final goal of mixed integer linear programming model, as well as the three goals of sorting, transferring and storing, are obtained by reduction process. Finally, this paper uses Gurobi to solve practical problems, and obtains the ordering scheme and transshipment scheme that are superior to the historical schemes in ordering cost, transshipment loss and storage cost.

<img src="docs/DE-MOOT.png" width = "600" height = "300" align=center>

## Enviroment
```
python 3.9.12
Gurobi 10.0.0 (download: https://www.gurobi.com/downloads/gurobi-software/
license: https://www.gurobi.com/downloads/free-academic-license/)
SciencePlots (detail: https://github.com/garrettj403/SciencePlots)
numpy pandas sympy statsmodels matplotlib
```

## Note
The running results of this repository code are updated compared to the paper results.  
Please understand if there are any discrepancies.

## Citation
If our work help to your research, please cite our paper, thank you.
```
@inproceedings{mi2022research,
    title={Research on Data-driven Enterprise Raw Material Ordering and Optimal Transportation Scheme},
    author={Mi, Kerun and Gu, Hai and Liu, Jiacheng and Yang, Liu},
    booktitle={2022 Asia Conference on Algorithms, Computing and Machine Learning (CACML)},
    pages={653--658},
    year={2022},
    organization={IEEE}
}
```
**Thanks to [Gurobi](https://www.gurobi.com/)'s excellent performance, the completion of this paper is inseparable from their wonderful work.**