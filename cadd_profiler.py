 ## nohup CADD.sh -a -o CADD_scores_SampleName.tsv.gz Sample.vcf > cadd_analysis.txt
import numpy as np
import pandas as pd
import glob
import os

cadd_profile = pd.read_csv("CADD_scores_SampleName.tsv", sep= "\t", header=1)
deleterious_mutations = cadd_profile[(cadd_profile['PHRED'] > 20) & (cadd_profile['Type']=='SNV')]
for index, row in deleterious_mutations.iterrows():
    fname = "mutations/"+str(row['Pos'])+"_"+str(row['GeneID'])+"_.vcf"
    out = open(fname, "w")
    line1 = "chrm\tstart\tstop\tref\tvar\tgene_name\ttrv_type\n"
    line2 = str(row['#Chrom'])+"\t"+str(row['Pos'])+"\t"+str(row['Pos'])+"\t"+row['Ref']+"\t"+row['Alt']+"\t"+str(row['GeneID'])+"\t"+row['Consequence']+"\n"
    out.write(line1)
    out.write(line2)
    out.close
