set terminal png size 500, 500 truecolor
set output "graph.png"
set ylabel "Preço em Reais"
set xlabel "Dias"
set grid
plot "values.dat" using 1:2 title 'Real' with lines, \
     "values.dat" using 1:3 title 'Mm_10' with lines, \
     "values.dat" using 1:4 title 'Mm_50' with lines
