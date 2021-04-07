# Portfolio

---

Short bios of my previous research projects. 

---

### <ins>Biodiversity Conservation via Geospatial Machine Learning </ins>

*Funded through the NSF Award #1757952, a collaboration with Prof. Stephen Adolph. Conference Proceedings: SICB Meeting '21, SCCUR Meeting '19.*

**Overview:** Pioneered the application of geospatial machine learning frameworks for species conservation in the SW United States. Built highly predictive species distribution models (neural networks, BRTs, soft voters) through the design of Python and R programs for ensembled modeling, random sampling, and geo-statistics. 

**Research Question:** How will climate change shift geographic overlaps between Desert Night Lizards and their Joshua tree habitats?

<img src="images/range.png?raw=true"/> 

**Fig 1. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/PySDMs">Night Lizard Geo-classification.</a></ins>** A probabilistic prediction of habitat suitability (likelihood of species presence) for the Desert Night Lizard. The model correctly classifies all ~1200 presence records in binary presence/absence form, including the ~300 points held out for validation.

<img src="images/auc.png?raw=true"/>

**Fig 2. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/PySDMs">Night Lizard Model Metrics</a></ins>.** 10-fold cross validation ROC (left) and 30% hold-out validation F1 scores from dozens of runs over differing data partitions, random seeds, and background samples (right). 

**Full Title:** Assessing Climate Change Impacts on Xantusia vigilis lizards and their Joshua tree habitats with Ensemble Species Distribution Models.

* <a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/drive/folders/15nZUMuGLiINuhSuP6DJ6hg27YKZxeC9A?usp=sharing">Written Outputs</a><br>
* <a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/PySDMs">Code Repository</a><br>
* <a target="_blank" rel="noopener noreferrer" href="https://nbviewer.jupyter.org/github/daniel-furman/PySDMs/blob/main/examples/night_lizards/PySDMs_example1.ipynb">Online Notebook</a>

---

### <ins>The Material Science of Ice Sheet Densification</ins>

*Funded through Penn's Rose Undergraduate Research Award, CURF Sustainability Action Grant, and the EES Hayden Scholars Grant, a collaboration with Prof. David Goldsby.*

**Overview:** Spearheaded a three-year project with Penn's Experimental Geophysics Group, focusing on problems in the near-surface of ice sheets. Led experiments probing for microstructure sensitive flow in ice compaction. Developed and analyzed constitutive rheological models from our lab results for applications to natural settings. 

**Research Question:** How does an ice sheet's grain size, strain state, and microstructure influence the rate of near-surface densification? 

<img src="images/exp-interv.png?raw=true"/>

**Fig 3. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research/blob/master/exp_confidence_intervals.py">Flow Rates</a></ins>.** Final results from our laboratory compaction tests (2017-2020). The data points represent our experimental "steady-state creep" rates for ice densification at a given applied stress and grain size. 

<img src="images/map.png?raw=true"/>

<p align="center"><img src="https://render.githubusercontent.com/render/math?math=\frac{\dot{\rho}}{\rho_{ice}} (dens. rate) = \frac{2{\A}(1-{\rho}r)}{(1-(1-{\rho}r)^{1/n})^{n}} (\frac{2\sigma}{n})^{n} exp(\frac{-Q}{RT})d^{-p}"> </p>

**Fig 4. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research/blob/master/mechanism_maps.py">Ice Sheet Densification Model</a></ins>.** Mechanism map model for ice sheet densification at 233 K (a common temperature at the interior of terrestrial ice sheets), constructed from the semi-empirical equation above. Values for the equation's several semi-empirical parameters were directly determined from our experiments, as well as the functional form of the power law relationship between dens. rate and grain size. 

**Full Title:** The Rheological Behavior of Firn: Experimental Observations of Dislocation Creep via Grain Boundary Sliding.

* <a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/drive/folders/1eDXEeZ1x04-mp7oUI9cQi2PNBXxXor5x?usp=sharing">Written Outputs</a>
* <a target="_blank" rel="noopener noreferrer" href="https://www.curf.upenn.edu/project/furman-daniel-experimental-ice-compaction">CURF Grant Write-Up</a>
* <a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research">Code Repository</a><br>
* <a target="_blank" rel="noopener noreferrer" href="https://nbviewer.jupyter.org/github/daniel-furman/ice-densification-research/blob/master/Firn_notebook.ipynb">Online Notebook</a>
