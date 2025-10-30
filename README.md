# Description of analysis scripts

## Main text figures

`alignment_conservation.ipynb` (CJL - updated) 
- Creates plots for **Figure 1**
- Performs pairwise alignments of all 502 sequences and calculates percent identity (including gaps) and alignment score.
- Also does this for the AD regions separately (DBD, length matched central AD, length matched upstream DBD region, IDR).
- Also performs shuffles as a control.

`analyze_paml_result.ipynb` (CJL - updated)
- Creates dN/dS plot for **Figure 1**
- dN/dS was analysis run in PAML yn00, loads results and plots distribution  

Figure 2 plots

`AD_properties Fall 2024.ipynb` (MVS)
- Creates plots for **Figure 3**
- This script explores how sequence properties, like AA abundance or motif locations, contribute to activation domain activity.
- Contains main figure panels

`Full_Length_TFs_Heatmaps_Fall 2024.ipynb` (MVS)
- Creates **Figure 4** plot, **Figure 1B**, **Figure 2F,G**
- Script to make heatmaps of full-length orthologs

`evolver_simulations.ipynb` (CJL - added)
- Creates **Figure 5** plot
- Loads in simulation results from evolver in PAML and FoldX and summarizes activites

`AD_AlignmentDists.ipynb` (MVS)
- Creates **Figure 5** plot
- This script looks at the Edit distances between pairs of sequences. It shows that many changes in sequence do not change activity.
  
`alignment_visualization.ipynb` (CJL - updated) 
- Creates **Figure 5** plots, Supplemental Figure X
- Creates plots in Figure 5 to visualize the alignment of the central activation domain for all unique sequences in that region (138) and the most active sequences (69).
- Creates conservation barplot, sequence logos, and an html of the sequence alignment.

`Random_N_term_explore.ipynb` (CJL - updated) 
- Creates plots in **Figure 6** comparing closely related homologs
- Compares pairs of sequences that differ in N-terminal activity.
- Creates activity traces for these sequences and highlights regions of difference.

`counting_N_term_ADs.ipynb` (CJL - updated)
- Creates tree plot in **Figure 6**
- Counts the number of N-term ADs by either combining overlapping active tiles or counting the number of peaks in the smoothed activity traces
- Plots the count of N-terminal ADs using both methods on the gene and species trees

`FigureS23_helix_prediction.ipynb` (CJL)
- Creats plots in **Figure 6** 
- Predicts the helical propensity of the top 138 most active sequences

`generate_mutations_TADA.ipynb` (CJL - added)
- Creates plots in **Figure 7**
- Generates all possible F->A mutations (single, double, etc.) and calculates change in activity 
- Calculates change in activity for single mutants based on alignment position
  
## Supplemental Figures

`motifs_on_tree.ipynb` (CJL - updated)
- Creates plots in **Supplemental Figure X**
- Creates figure with the motifs on the gene and species trees
- Creates figure with the alignment of the central AD on the tree, highlighting gain of the FF motif

`Ino2_search_analysis.ipynb` (CJL - updated)
- Creates plots in **Supplemental Figure X**
- For Ino2 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae Ino2 AD. 

`War1_search_analysis.ipynb` (CJL - updated)
- Creates plots in **Supplemental Figure X**
- For War1 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae War1 AD. 

`Met4_search_analysis.ipynb` (CJL - updated)
- Creates plots in **Supplemental Figure X**
- For Met4 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae Met4 AD. 

`SP_on_tree.ipynb` (CJL - updated) 
- Creates plots in **Supplemental Figure X**
- Creates a figure with the number of SP and TP motifs in the central AD (the region surrounding the WxxLF motif) on the gene tree. 

`tile_diversity.ipynb` (CJL - added)
- Creates plots in **Supplemental Figure X**
  
`Controls_oct024.ipynb` (MVS) 
- Creates plots in **Supplemental Figure X**
- Barplots for control sequences
- Reproducibility analysis

`FigureS13_activitiess_on_gene_tree.ipynb` (CJL - to update) 
- Creates plots in **Supplemental Figure X**
- Plots heatmaps of smoothed tile activities on the y1000+ species tree

`FigureS14_activitiess_on_species_tree.ipynb` (CJL - to update)
- Creates plots in **Supplemental Figure X**
- Plots heatmaps of smoothed tile activities on the estimated gene tree

`counting_motifs.ipynb` (CJL - added)
-  Creates plots in **Supplemental Figure X**

`make_activity_traces.ipynb` (CJL - updated)
-  Creates plots in **Supplemental Figure X**
- Plots the trace (along with AD count) for each ful length sequence

`predict-tiles.py` (GH - added)
- Runs FINCHES on tiles and ABD1 domain of Med15
- Data used in **Supplemental Figure X**
  
## Other important analyses

`Composition_ANOVA Fall 2024.ipynb`
- Creates Table 1
- ANOVA analysis of OLS regression on composition and dipeptides

`Gaussian_Threshold.ipynb`
- Analysis of inactive sequences to find activity threshold

`Step2_AddSeqFeaturestoDataFrame_Oct_2024.ipynb`
- Combines the data from the two replicates.
- Computes many sequence features, like net charge.

`YeastAnalysisfunctions.py`
- Support functions for visualizing data

`longest_gene_per_species.ipynb` (CJL - updated) 
- Gets the longest gene per species (124 total). Creates fasta file and pickled object of these sequences. 

`make_species_tree.ipynb` (CJL - updated) 
- Creates a species tree for the species used in our screen.
- Starts with the tree from mycocosm and adds clades from the y1000+ tree for species not present in mycososm tree.
- Note that because we are merging trees estimated with different programs, branch lengths are not meaningful

ADD PAML scripts

## Not in paper

`EC_Sog1_GCN4analysis_LeBlanc2024.ipynb`
- Phophomutant (Phosphomimetic, Phosphonull) activity traces

`Sensu strictu v2.ipynb`
- Plot activity traces of S. cerevisiae and closest species

  


