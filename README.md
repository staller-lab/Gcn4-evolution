# Description of analysis scripts

## Main text figures

`alignment_conservation.ipynb`
- Creates plots for **Figure 1**
- Performs pairwise alignments of all 502 sequences and calculates percent identity (including gaps) and alignment score.
- Also does this for the AD regions separately (DBD, length matched central AD, length matched upstream DBD region, IDR).
- Also performs shuffles as a control.

`analyze_paml_result.ipynb`
- Creates dN/dS plot for **Figure 1**
- dN/dS was analysis run in PAML yn00, loads results and plots distribution
- Control files and results from PAML are located in the dn_ds folder

Figure 2 plots

`AD_properties Fall 2024.ipynb` 
- Creates plots for **Figure 3**
- This script explores how sequence properties, like AA abundance or motif locations, contribute to activation domain activity.
- Contains main figure panels

`Full_Length_TFs_Heatmaps_Fall 2025 pruned sequences.ipynb`
- Creates **Figure 4** plot
- Script to make heatmaps of full-length orthologs with longest sequences removed
- 
`Full_Length_TFs_Heatmaps_Fall 2024.ipynb`
- Creates **Figure 1B**, **Figure 2F,G**, **Figure S2, S12**
- Script to make heatmaps of full-length orthologs

`evolver_simulations.ipynb` 
- Creates **Figure 5** plot
- Loads in simulation results from evolver in PAML and FoldX and summarizes activites

`AD_AlignmentDists.ipynb` 
- Creates **Figure 5** plot
- This script looks at the Edit distances between pairs of sequences. It shows that many changes in sequence do not change activity.
  
`alignment_visualization.ipynb` 
- Creates **Figure 5** plots, **Supplemental Figure 17,18**
- Creates plots in Figure 5 to visualize the alignment of the central activation domain for all unique sequences in that region (138) and the most active sequences (69).
- Creates conservation barplot, sequence logos, and an html of the sequence alignment.

`cad_tile_scatter_plots.ipynb`
- Creates **Figure 5E** scatter plots of property vs. activity for central ADs.  

`Random_N_term_explore.ipynb`  
- Creates plots in **Figure 6** comparing closely related homologs
- Compares pairs of sequences that differ in N-terminal activity.
- Creates activity traces for these sequences and highlights regions of difference.

`counting_N_term_ADs.ipynb` 
- Creates tree plot in **Figure 7**
- Counts the number of N-term ADs by either combining overlapping active tiles or counting the number of peaks in the smoothed activity traces
- Plots the count of N-terminal ADs using both methods on the gene and species trees

`FigureS23_helix_prediction.ipynb` 
- Creats plots in **Figure 6** 
- Predicts the helical propensity of the top 138 most active sequences
  
## Supplemental Figures

`motifs_on_tree.ipynb`
- Creates plots in **Supplemental Figure X**
- Creates figure with the motifs on the gene and species trees
- Creates figure with the alignment of the central AD on the tree, highlighting gain of the FF motif

`Ino2_search_analysis.ipynb`
- Creates plots in **Supplemental Figure 21**
- For Ino2 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae Ino2 AD. 

`War1_search_analysis.ipynb`
- Creates plots in **Supplemental Figure 21**
- For War1 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae War1 AD.

`Met4_search_analysis.ipynb`
- Creates plots in **Supplemental Figure 21**
- For Met4 homologs (identified by the Y1000+ project), identify AD regions and create plot of conservation within AD.
- AD is identified using a consensus approach (at least 3/5 AD predictors must predict the region as active).
- Additionally, if there are multiple ADs per TF, we only include the last one, as this corresponds to the cerevisiae Met4 AD.

`Pdr1_search_analysis.ipynb`
- Creates plots in **Supplemental Figure 21**
- For Pdr1 homolog ADs (identified by Sanborn et. al 2021) create plot of conservation within AD.

`SP_on_tree.ipynb` 
- Creates plots in **Supplemental Figure 15**
- Creates a figure with the number of SP and TP motifs in the central AD (the region surrounding the WxxLF motif) on the gene tree. 

`tile_diversity.ipynb` 
- Creates plot in **Figure S22**
- Calculates pairwise edit distance between all tiles and active tiles
  
`Controls_oct024.ipynb`
- Creates plots in **Figure S4**, **Figure S5**
- Barplots for control sequences
- Reproducibility analysis

`activities_on_gene_tree.ipynb`
- Creates plots in **Supplemental Figure S12**
- Plots heatmaps of smoothed tile activities on the estimated gene tree

`activities_on_species_tree.ipynb`
- Creates plots in **Supplemental Figure 14**
- Plots heatmaps of smoothed tile activities on the y1000+ species tree

`counting_motifs.ipynb`
-  Creates plots in **Supplemental Figure 3**

`make_activity_traces.ipynb` 
-  Creates plots in **Supplemental Figure 1**
- Plots the trace (along with AD count) for each ful length sequence

`predict-tiles.py`
- Runs FINCHES on tiles and ABD1 domain of Med15
- Data used in **Supplemental Figure 7**

`finches.ipynb`
- Creates bar plots in **Supplemental Figure 7**
- Compares finches scores for active and non-active tiles

`generate_mutations_TADA.ipynb` 
- Creates plots in **Supplemental Figure 24**
- Generates all possible F->A mutations (single, double, etc.) and calculates change in activity 
- Calculates change in activity for single mutants based on alignment position

`Gaussian_Threshold.ipynb`
- Creates plots in **Supplemental Figure 6**
- Analysis of inactive sequences to find activity threshold

`compare-predictors-Copy1.ipynb`
- Creates plots in **Supplemental Figure 23**
- Compares NNs trained on Gcn4 homolog data to other neural networks

`activity_integral.ipynb`
- Creates plots in **Supplemental Figure 25**
- Computes integral of smoothed activity and compares to null distribution of shuffled activities
  
  
## Other important analyses

`Composition_ANOVA Fall 2024.ipynb`
- Creates Table 1
- ANOVA analysis of OLS regression on composition and dipeptides

`Step2_AddSeqFeaturestoDataFrame_Oct_2024.ipynb`
- Combines the data from the two replicates.
- Computes many sequence features, like net charge.

`YeastAnalysisfunctions.py`
- Support functions for visualizing data

`longest_gene_per_species.ipynb` 
- Gets the longest gene per species (124 total). Creates fasta file and pickled object of these sequences. 

`make_species_tree.ipynb`
- Creates a species tree for the species used in our screen.
- Starts with the tree from mycocosm and adds clades from the y1000+ tree for species not present in mycososm tree.
- Note that because we are merging trees estimated with different programs, branch lengths are not meaningful

`F_combinatorics.ipynb`
- Calculates the expected number of FFs in a sequence

`SortSeq Data Processing Template.ipynb`
- Used to process SortSeq data


## Not in paper

`EC_Sog1_GCN4analysis_LeBlanc2024.ipynb`
- Phophomutant (Phosphomimetic, Phosphonull) activity traces

`Sensu strictu v2.ipynb`
- Plot activity traces of S. cerevisiae and closest species

`YGOB_analysis.ipynb` 
- YGOB selection analysis, left over from earlier version of the paper
  


