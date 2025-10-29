# Description of analysis scripts

## Main text figures

`alignment_conservation.ipynb` (CJL - to add) 
- Creates plots for figure 1
- Performs pairwise alignments of all 502 sequences and calculates percent identity (including gaps) and alignment score.
- Also does this for the AD regions separately (DBD, length matched central AD, length matched upstream DBD region, IDR).
- Also performs shuffles as a control.

ADD dN/dS
  
`AD_properties Fall 2024.ipynb` (MVS)
- This script explores how sequence properties, like AA abundance or motif locations, contribute to activation domain activity.
- Contains main figure panels

`Figure5_alignment_visualization.ipynb` (CJL - to remove)
- Creates sequence logos and alignment bar plots fir region around the WxxLF motif
- Also creates html file of the alignment with given colors

`alignment_visualization.ipynb` (CJL - to add) 
- Creates plots in Figure 5 to visualize the alignment of the central activation domain for all unique sequences in that region (138) and the most active sequences (69).
- Creates conservation barplot, sequence logos, and an html of the sequence alignment.

`Random_N_term_explore.ipynb` (CJL - to add) 
- Creates plots in Figure 6 comparing closely related homologs
- Compares pairs of sequences that differ in N-terminal activity.
- Creates activity traces for these sequences and highlights regions of difference.

`counting_N_term_ADs.ipynb` (CJL - to add)
- Creates tree plot in Figure 6
- Counts the number of N-term ADs by either combining overlapping active tiles or counting the number of peaks in the smoothed activity traces
- Plots the count of N-terminal ADs using both methods on the gene and species trees

`FigureS3_WLF_sequence_logos.ipynb` (CJL)
- Creates sequence logos for regions around the WxxLF motif

`FigureS23_helix_prediction.ipynb` (CJL)
- Predicts the helical propensity of the top 138 most active sequences

`Full_Length_TFs_Heatmaps_Fall 2024.ipynb` (MVS)
- Script to make heatmaps of full-length orthologs
  
## Supplemental Figures

`motifs_on_tree.ipynb` (CJL - to add)
- Supplemental Figure X 
- Creates figure with the motifs on the gene and species trees
- Creates figure with the alignment of the central AD on the tree, highlighting gain of the FF motif

`Ino2_search_analysis.ipynb` (CJL - to add)
- Supplemental Figure X
- For Ino2 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae Ino2 AD. 

`War1_search_analysis.ipynb` (CJL - to add)
- Supplemental Figure X
- For War1 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae War1 AD. 

`Met4_search_analysis.ipynb` (CJL - to add)
- Supplemental Figure X
- For Met4 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae Met4 AD. 

`SP_on_tree.ipynb` (CJL - to add) 
- Supplemental Figure X
- Creates a figure with the number of SP and TP motifs in the central AD (the region surrounding the WxxLF motif) on the gene tree. 

`Controls_oct024.ipynb` (MVS) 
- Barplots for control sequences
- Reproducibility analysis

`FigureS13_activitiess_on_gene_tree.ipynb` (CJL - to update) 
- Plots heatmaps of smoothed tile activities on the y1000+ species tree

`FigureS14_activitiess_on_species_tree.ipynb` (CJL - to update)
- Plots heatmaps of smoothed tile activities on the estimated gene tree

`Ino2_analysis.ipynb` (CJL - remove) 
- Describes how to perform the hmmer search used to identify Ino2 orthologs
- Filters Ino2 orthologs based on domains and a reverse blast search
- Creates an alignment conservation plot

`Ino4_analysis.ipynb` (CJL - remove) 
- The same as Ino2 analysis but for Ino4

`Pdr1_analysis.ipynb` (CJL - update) 
- Makes alignment conservation plot for active Pdr1 sequences from Sanborn et al. 2021

`War1_analysis.ipynb` (CJL - remove) 
- The same as Ino2 analysis but  for War1
  
## Other important analyses

`AD_AlignmentDists.ipynb`
- This script looks at the Edit distances between pairs of sequences. It shows that many changes in sequence do not change activity.

`Composition_ANOVA Fall 2024.ipynb`
- ANOVA analysis of OLS regression on composition and dipeptides

`Gaussian_Threshold.ipynb`
- Analysis of inactive sequences to find activity threshold

`Step2_AddSeqFeaturestoDataFrame_Oct_2024.ipynb`
- Combines the data from the two replicates.
- Computes many sequence features, like net charge.

`YeastAnalysisfunctions.py`
- Support functions for visualizing data

`longest_gene_per_species.ipynb` (CJL - to add) 
- Gets the longest gene per species (124 total). Creates fasta file and pickled object of these sequences. 

`make_species_tree.ipynb` (CJL - to add) 
- Creates a species tree for the species used in our screen.
- Starts with the tree from mycocosm and adds clades from the y1000+ tree for species not present in mycososm tree.
- Note that because we are merging trees estimated with different programs, branch lengths are not meaningful
  
## Not in paper

`EC_Sog1_GCN4analysis_LeBlanc2024.ipynb`
- Phophomutant (Phosphomimetic, Phosphonull) activity traces

`FigureS16_clusteringADs.ipynb`
- Clusters activation domain sequences and compares those with the WxxLF motif to those without the motif.

`FigureS31_finches.ipynb`
- GET FROM GEAN
- Uses finches to calculate the attraction and repulsion between tiles and Med15

`Sensu strictu v2.ipynb`
- Plot activity traces of S. cerevisiae and closest species
  
`FigureS7_gain_loss_F.ipynb`
- Plots a subset of the ygob alignment on the species and gene tree
- Highlights the F residues in the alignment

  


