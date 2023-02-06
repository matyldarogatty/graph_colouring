# Graph colouring problem
Map coloring problem asks whether the countries on every map can be coloured by using as few colors as possible, in such a way that countries sharing an edge have different colours. We can achieve this problem by representing map as a graph.

In this repository you can find theoretical analysis of some graph colouring algorithm and algorithm it's self.

### Theoretical analysis of algorithm is my bachelor thesis. 
File analiza_pewnego_algorytmu_kolorujacego_grafy.pdf.
First section is introduction to graph theory and graph colouring problem. 
Next section presents some easy graph colouring algorithm step by step.
And the last section is about algorithm presented in paper M. H. Williams, (1985). \emph{A Linear Algorithm for Colouring Planar Graphs with Five Colours}, The           Computer Journal 28.1: 78-81. 
### Program written in python.
The algorithm: five_colouring_algm.py.
Some test on graphs consist of vertices of degree more than 4: icosahedral.py.

#### Ex1. Icosahedral.
<img src="https://user-images.githubusercontent.com/92950276/217048247-1757b343-717b-4c34-ace6-8a5e20a44cf6.png" width="250" height="200"><img src="https://user-images.githubusercontent.com/92950276/217048261-13f19c77-f246-4327-b7b1-731b3d3a19b1.png" width="250" height="200">

#### Ex2. Some graph with glued icosahedrons.
<img src="https://user-images.githubusercontent.com/92950276/217048441-3f047864-23f1-4f7d-b1c1-16e50eb1caa2.png" width="250" height="200"><img src="https://user-images.githubusercontent.com/92950276/217048451-c999fd90-41af-4611-93e2-e6fe9f9ac498.png" width="250" height="200">
