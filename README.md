## Description of python analysis scripts

**Step2_AddSeqFeaturestoDataFrame_Oct_2024.ipynb**
- Combines the data from the two replicates.
- Computes many sequence features, like net charge.


**AD_AlignmentDists.ipynb**
- This script looks at the Edit distances between pairs of sequences. It shows that many changes in sequence do not change activity.


**AD_properties Fall 2024.ipynb**
- This script explores how sequence properties, like AA abundance or motif locations, contribute to activation domain activity.
- Contains main figure panels


**Composition_ANOVA Fall 2024.ipynb**
- ANOVA analysis of OLS regression on composition and dipeptides


**Controls_oct024.ipynb**
- Barplots for control sequences
- Reproducibility analysis

**EC_Sog1_GCN4analysis_LeBlanc2024.ipynb**
- Phophomutant (Phosphomimetic, Phosphonull) activity traces

**Full_Length_TFs_Heatmaps_Fall 2024.ipynb**
- Script to make heatmaps of full-length orthologs 


**Sensu strictu v2.ipynb**
- Plot activity traces of S. cerevisiae and closest species


**Gaussian_Threshold.ipynb**
- Analysis of inactive sequences to find activity threshold


**YeastAnalysisfunctions.py**
- Support functions for visualizing data

**FigureS16_clusteringADs.ipynb**
- Clusters activation domain sequences and compares those with the WxxLF motif to those without the motif.

**FigureS3_WLF_sequence_logos.ipynb**
- Creates sequence logos for regions around the WxxLF motif

**Figure5_alignment_visualization.ipynb**
- Creates sequence logos and alignment bar plots fir region around the WxxLF motif
- Also creates html file of the alignment with given colors

**FigureS13_activitiess_on_gene_tree.ipynb**
- Plots heatmaps of smoothed tile activities on the y1000+ species tree

**FigureS14_activitiess_on_species_tree.ipynb**
- Plots heatmaps of smoothed tile activities on the estimated gene tree

**FigureS7_gain_loss_F.ipynb**
- Plots a subset of the ygob alignment on the species and gene tree
- Highlights the F residues in the alignment

**FigureS31_finches.ipynb**
- Uses finches to calculate the attraction and repulsion between tiles and Med15

**FigureS23_helix_prediction.ipynb**
- Predicts the helical propensity of the top 138 most active sequences
