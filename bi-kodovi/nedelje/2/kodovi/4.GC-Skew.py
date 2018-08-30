def main():
    
    fajl = open('ecoli.fna', 'r')
    
    fajl.readline() # Zanemaruje se prvi red datoteke u FASTA formatu
    sadrzaj = ""
    
    sadrzaj = fajl.readlines()
    sadrzaj = "".join(sadrzaj)
    sadrzaj = sadrzaj.replace('\n', '')
    sadrzaj = sadrzaj.lower()
    
    skew = calculate_skew(sadrzaj[1000000:])
    draw_skew(skew)
