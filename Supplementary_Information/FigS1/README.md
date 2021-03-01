By loading ```TableS3``` on the online software [Morpheus](https://software.broadinstitute.org/morpheus), the heatmap in ```FigS1.png``` can be obtained. We recommend performing *Hierarchical Clustering*, specifying the options:

     - Metric -> Matrix values (from a precomputed distance matrix)
     - Linkage Method -> Average
     - Cluster -> Rows and Columns

The clustering is used to make sure that the rows and columns are grouped according to their Jaccard distances, and not following the input order. From *Options*, we modified *Color Scheme* and unchecked the box *Relative Color Scheme*, which allowed us to force the maximum at 0.778 (which is the maximum Jaccard distance of the dataset), therefore obtaining a better resolution for the distance matrix. We also clicked on *Add Color Stop* at 0.426, and then selected the color Yellow, to obtain a better resolution of the table.  
     
