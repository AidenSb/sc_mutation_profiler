from subprocess import Popen, PIPE
import subprocess
import sys

gref = "~/gary/refdata-cellranger-GRCh38-3.0.0/fasta/genome.fa"
bam_inp = sys.argv[1]
cmd1 = "samtools sort  %s  -o  %s" % (bam_inp, bam_inp[:-4]+"_temp_samsorted.bam")
subprocess.call(cmd1, shell=True)
p2 = Popen(["gatk", "AddOrReplaceReadGroups", "--INPUT","%s_temp_samsorted.bam" % (bam_inp), "--OUTPUT", "%s_temp_sort_addgroup.bam" % (bam_inp), "--RGLB", "lib1", "--RGPL","illumina","--RGPU", "unit1", "--RGSM", "20", "--SORT_ORDER", "coordinate"], stdout=PIPE)
p2.communicate()
p2.wait()
p3 = Popen(["gatk", "MarkDuplicates", "--INPUT" ,"%s_temp_sort_addgroup.bam" % (bam_inp), "--OUTPUT","%s_temp_sort_addgroup_rawdedupped.bam" % (bam_inp) ,"--METRICS_FILE", "%s_out.metrics" % (bam_inp)], stdout=PIPE)
p3.communicate()
p3.wait()
bamin = bam_inp +"_temp_sort_addgroup_rawdedupped.bam"
bamout = bam_inp +"_temp_sort_addgroup_dedupped_splitN.bam"
cmd = "gatk SplitNCigarReads -R ~/gary/refdata-cellranger-GRCh38-3.0.0/fasta/genome.fa -I %s -O %s " %(bamin, bamout)
subprocess.call(cmd, shell=True)
vcfout = bam_inp + "_gatk_wholes_genome.vcf"
cmdl = " gatk HaplotypeCaller -R %s -I %s --dont-use-soft-clipped-bases  --standard-min-confidence-threshold-for-calling 20.0 -O %s" % (
gref, bamout, vcfout)
subprocess.call(cmdl, shell=True)
cln = "rm *_temp_*"
subprocess.call(cmdl, shell=True)

