# Portfolio

---

Short bios of my previous research projects. 

---

### <ins> Mojave Species Conservation via Geospatial ML </ins>

*Overview:* Ecology / Geospatial ML / Harvey Mudd DS REU '19

*Research Question:* How will climate change shift the geographic overlap between Joshua trees and Desert Night Lizards?

*Outline:* Mathematical ecology project funded through the NSF REU Award #1757952, a collaboration with Prof. Stephen Adolph and Harvey Mudd College. Full Title: Assessing Climate Change Impacts on Xantusia vigilis lizards and their Joshua tree habitats with Ensemble Species Distribution Models. Conference Proceedings: SICB Meeting '21, SCCUR Meeting '19.

* <a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/drive/folders/15nZUMuGLiINuhSuP6DJ6hg27YKZxeC9A?usp=sharing">Written Outputs</a>
* <a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ensemble-climate-projections">Code Repository</a>
* <a target="_blank" rel="noopener noreferrer" href="https://nbviewer.jupyter.org/github/daniel-furman/ensemble-climate-projections/blob/main/Comparing_MLs.ipynb">Online Notebook</a>

<img src="images/range.png?raw=true"/> 

**Fig 1. <ins><a target="_blank" rel="noopener noreferrer" href="https://nbviewer.jupyter.org/github/daniel-furman/ensemble-climate-projections/blob/main/Comparing_MLs.ipynb">Species Distribution Models</a></ins>**. Geographic prediction of the near-present Desert Night Lizard species distribution, with best subset model selection among soft voters composed of up to 6 BRT classifiers. 

<img src="images/auc.png?raw=true"/>

**Fig 2. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ensemble-climate-projections">Blended Model Performance</a></ins>**. Validation performance (30% held-out) for the Desert Night Lizard's near-current species distribution model (ie. corresponding to the above geospatial prediction).  

<br><br>

---

### <ins>The Material Science of Ice Densificaiton</ins>

*Overview:* Geophysics / Experimental Material Science / UPenn Senior Thesis

*Research Question:* How does ice sheet grain size, strain state, and microstructure influence rates of ice densification?

*Outline:* Three-year experimental geophysics project with Prof. David Goldsby and the University of Pennsylvania's Ice Physics Lab, funded by UPenn's Rose Undergraduate Research Award, CURF Sustainability Action Grant, and Hayden Scholars Grant. Full Title: The Rheological Behavior of Firn: Experimental Observations of Dislocation Creep via Grain Boundary Sliding.

* <a target="_blank" rel="noopener noreferrer" href="https://drive.google.com/drive/folders/1eDXEeZ1x04-mp7oUI9cQi2PNBXxXor5x?usp=sharing">Written Outputs</a>
* <a target="_blank" rel="noopener noreferrer" href="https://www.curf.upenn.edu/project/furman-daniel-experimental-ice-compaction">CURF Grant Write-Up</a>
* <a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research">Code Repository</a><br>
* <a target="_blank" rel="noopener noreferrer" href="https://nbviewer.jupyter.org/github/daniel-furman/ice-densification-research/blob/master/Firn_notebook.ipynb">Online Notebook</a>


<img src="images/exp-interv.png?raw=true"/>

**Fig 3. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research/blob/master/exp_confidence_intervals.py">Flow Rates</a></ins>**. The data points represent laboratory densification rates for ice compaction at the steady state (aka, the final results of three-years worth of lab testing). Notice the key feature of our experimental methodology, our compaction tests were conducted on samples with uniform grain size (particle size), with grains varying between 5 to 550 micrometers in radius. 
<img src="images/map.png?raw=true"/>

<p align="center"><img src="https://render.githubusercontent.com/render/math?math=\frac{\dot{\rho}}{\rho_{ice}} (dens. rate) = \frac{2{\A}(1-{\rho}r)}{(1-(1-{\rho}r)^{1/n})^{n}} (\frac{2\sigma}{n})^{n} exp(\frac{-Q}{RT})d^{-p}"> </p>

**Fig 4. <ins><a target="_blank" rel="noopener noreferrer" href="https://github.com/daniel-furman/ice-densification-research/blob/master/mechanism_maps.py">Densification Mechanism Map</a></ins>**. Rate modeling for ice creep during densification at 233 K, a common terrestrial ice sheet temperatures. We developped the semi-empirical rate model above, with newly applied power law relationship between rate and grain size constrained with our above experimental results. 
