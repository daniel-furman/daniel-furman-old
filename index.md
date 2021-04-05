# Portfolio

---

Short bios of my previous research projects. 

---

### <ins>Biodiversity Conservation via Geospatial Machine Learning </ins>

*Funded through the NSF Award #1757952, a collaboration with Prof. Stephen Adolph. Conference Proceedings: SICB Meeting '21, SCCUR Meeting '19.*

**Overview:** Pioneered the application of geospatial machine learning frameworks for species conservation in the SW United States. Built highly predictive species distribution models (neural networks, BRTs, soft voters) through the design of Python and R programs for ensembled modeling, random sampling, and geo-statistics. 

**Research Question:** How will climate change shift geographic overlaps between Desert Night Lizards and their Joshua tree habitats?

<img src="images/range.png?raw=true"/> 

**Fig 1. <ins><a target="_blank" rel="noopener noreferrer" href="https://nbviewer.jupyter.org/github/daniel-furman/ensemble-climate-projections/blob/main/Comparing_MLs.ipynb">Species Distribution Models</a></ins>**. Geo-classification example for the Night Lizard's distribution, utilizing a soft voting ensemble of BRTs and neural networks. 

<img src="images/auc.png?raw=true"/>

**Fig 2. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ensemble-climate-projections">Model Performance</a></ins>**. Performance metrics for the Night Lizard distribution model: an example of 10-fold cross validation ROC (left) and a boxplot of hold out (30%) F1 scores across dozens of modeling runs (right), both for the Night Lizard SDM.

**Full Title:** Assessing Climate Change Impacts on Xantusia vigilis lizards and their Joshua tree habitats with Ensemble Species Distribution Models.

* <a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/drive/folders/15nZUMuGLiINuhSuP6DJ6hg27YKZxeC9A?usp=sharing">Written Outputs</a><br>
* <a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ensemble-climate-projections">Code Repository</a><br>
* <a target="_blank" rel="noopener noreferrer" href="https://nbviewer.jupyter.org/github/daniel-furman/ensemble-climate-projections/blob/main/Comparing_MLs.ipynb">Online Notebook</a>

---

### <ins>The Material Science of Ice Sheet Densification</ins>

*Funded through Penn's Rose Undergraduate Research Award, CURF Sustainability Action Grant, and the EES Hayden Scholars Grant, a collaboration with Prof. David Goldsby.*

**Overview:** Spearheaded a three-year project with Penn's Experimental Geophysics Group, focusing on problems in the near-surface of ice sheets. Led experiments probing for microstructure sensitive flow in ice compaction. Developed and analyzed constitutive rheological models from our lab results for applications to natural settings. 

**Research Question:** How does an ice sheet's grain size, strain state, and microstructure influence the rate of near-surface densification? 

<img src="images/exp-interv.png?raw=true"/>

**Fig 3. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research/blob/master/exp_confidence_intervals.py">Flow Rates</a></ins>**. The data points represent the final results of our lab compaction tests, steady-state flow rates during ice densification. Our samples were synthesized across an order of magnitude of grain size (i.e., the individual ice particles), from 5 to 550 micrometers in radius. 

<img src="images/map.png?raw=true"/>

<p align="center"><img src="https://render.githubusercontent.com/render/math?math=\frac{\dot{\rho}}{\rho_{ice}} (dens. rate) = \frac{2{\A}(1-{\rho}r)}{(1-(1-{\rho}r)^{1/n})^{n}} (\frac{2\sigma}{n})^{n} exp(\frac{-Q}{RT})d^{-p}"> </p>

**Fig 4. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research/blob/master/mechanism_maps.py">Densification Mechanism Map</a></ins>**. Ice sheet densification model at 233 K (a common temperature at the interior of terrestrial ice sheets) constructed from the semi-empirical rate model above. The equation was parametrized by our lab results and included the novel power law relationship between rate and grain size uncovered by our study. 

**Full Title:** The Rheological Behavior of Firn: Experimental Observations of Dislocation Creep via Grain Boundary Sliding.

* <a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/drive/folders/1eDXEeZ1x04-mp7oUI9cQi2PNBXxXor5x?usp=sharing">Written Outputs</a>
* <a target="_blank" rel="noopener noreferrer" href="https://www.curf.upenn.edu/project/furman-daniel-experimental-ice-compaction">CURF Grant Write-Up</a>
* <a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research">Code Repository</a><br>
* <a target="_blank" rel="noopener noreferrer" href="https://nbviewer.jupyter.org/github/daniel-furman/ice-densification-research/blob/master/Firn_notebook.ipynb">Online Notebook</a>
