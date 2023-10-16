from tabula import read_pdf
from tabulate import tabulate

df = read_pdf("August 2023 Monthly Revenue Report.pdf", pages="all")
print(df)
print(tabulate(df))