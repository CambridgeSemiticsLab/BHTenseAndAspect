# Biblical Hebrew Time Collocations

<a href="https://www.ames.cam.ac.uk/people/current-phd-students"><img src="images/sponsor_banner.png" align="middle"></a> 

This repository will store data for Cody Kingham's PhD project on time expressions in Biblical Hebrew and their collocations with verbal and discourse constructions. This project combines methodologies from the fields of cognitive linguistics, construction grammar, and corpus-driven collostructional analysis (e.g. Stefanowitsch and Gries 2003).

The primary data for this project is the Hebrew syntax data from the [ETCBC, VU Amsterdam](https://github.com/ETCBC). The dataset is accessed and manipulated using the corpus analysis and annotation tool, [Text-Fabric](https://github.com/Dans-labs/text-fabric), of [DANS](https://dans.knaw.nl/en/about/organisation-and-policy/staff/roorda) (Netherlands). 

## Studies

The links below connect to notebooks found in the analysis directory.

* [Time Phrases in Standard Biblical Hebrew](https://nbviewer.jupyter.org/github/CambridgeSemiticsLab/BH_time_collocations/blob/master/analysis/SBH_time_expressions.ipynb) — Exploratory analysis of the ETCBC "Time" phrase in Genesis–Kings.
* [Verb Collocations with Atelic Time Duration Adverbials](https://nbviewer.jupyter.org/github/CambridgeSemiticsLab/BH_time_collocations/blob/master/analysis/duratives.ipynb) - A pilot study examining the collocations of atelic time duration adverbials with various verb lexemes in the Hebrew Bible, based on Fuhs' 2010 collostructional analysis ([source](https://philpapers.org/rec/FUHTAC)).
* [Time Constructions, part 1](https://nbviewer.jupyter.org/github/CambridgeSemiticsLab/BH_time_collocations/blob/master/analysis/time_constructions1.ipynb) – An exploratory study on the primary kinds of constructions used to express time at the phrasal/semi-phrasal level. This notebook gives insight and direction for the second exploratory study.
* [Time Constructions, part 2](https://nbviewer.jupyter.org/github/CambridgeSemiticsLab/BH_time_collocations/blob/master/analysis/time_constructions2.ipynb) – A second exploratory study on the primary kinds of constructions used to express time. This analysis takes advantage of a chunk + part of speech clustering method from part 1, whereby the constructions are broken down into primary surface forms. The analysis re-examines time construction data using previous analysis from elsewhere in this repository. Finally, the analysis focuses in on the various specifications applied to time nouns within the constructions which anchor their temporal referents. It is believed these may be a key component for understanding and clustering the constructions.

## Directory Structure
* [analysis](analysis) — Jupyter notebooks that contain the primary descriptions and data analyses
	* [analysis/pyscripts](analysis/pyscripts) — Python scripts for analysis notebooks
	* [analysis/preprocessing](analysis/preprocessing) — Cleaning, correcting, and preparing BHSA for analysis
* [data](data) — modified BHSA corpus data for use in this project (in Text-Fabric format)
* [images](images) — project images for/from notebooks and markdown
* [tf](tf) – Text-Fabric features produced by and for the analyses, including new semantic/statistical features for nouns


<br>



<hr>

[![DOI](https://zenodo.org/badge/153016597.svg)](https://zenodo.org/badge/latestdoi/153016597)

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

