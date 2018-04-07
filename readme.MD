# Mondo-Cluster
This repo contains source codes of the mini project proceeded under the first machine-learning workshop in LBNL (BSA-CSA Hackathon)

## Getting Started
~~~~
# get all required files
wget http://purl.obolibrary.org/obo/go.owl
wget http://purl.obolibrary.org/obo/mondo/pre/mondo.owl
wget https://github.com/realmarcin/MAK_results/blob/master/Inputs/MONDO_to_GO/mondo-leaves-to-go.tsv

# generate the closure over ontology files (i.e. reasoning) and replace the original files with the reasoned ones
robot reason --input go.owl --output go_reasoned.owl
robot reason --input mondo.owl --output mondo_reasoned.owl
rm go.owl mondo.owl -rf
mv go_reasoned.owl go.owl
mv mondo_reasoned.owl mondo.owl

# extract mondo classes corresponding to selected disease groups
# selected disease groups are three: MONDO:0000402 (small cell carcinoma), MONDO:0000602 (autoimmune disease of blood), MONDO:0018466 (late onset Parkinson disease)
robot extract --method STAR --input mondo.owl --term-file mondo_module.txt --output mondo_module.owl

# compute all graph distances between mondo classes
robot query --input mondo_module.owl --query query/mondo_dist.sparql mondo_dist.csv

# compute all graph distances between go classes
robot query --input go.owl --query query/go_dist.sparql go_dist.csv

# sums graph distances among mondo and go classes, i.e. merge these two ontologies. This produces go_dist_only.csv 
# for now, we only compute distances of go classes which are related to mondo classes. The resulting csv file does not include any mondo classes yet.
./merge_dist.py

# go_dist_only.csv is fed into Ben's script that computes dbscan over go classes. 
# The script will return core_samples.csv, which contains the list of go classes with its cluster ids (deriverd using dbscans)

# computes all labels of go classes 
robot query --input go.owl --query query/go_label.sparql go_label.csv

# maps go classes with their labels 
./map_label.py 

# the above script generates mapped_go_labels.txt, which contains the list of go classes with their labels and cluster ids.
~~~~

## Contributors
- [HyeongSik Kim](https://github.com/yy20716)
- [Ben Booth](https://github.com/benwbooth)
- [Chris Mungall](https://github.com/cmungall)
