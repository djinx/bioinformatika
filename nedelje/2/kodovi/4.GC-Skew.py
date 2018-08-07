import matplotlib.pyplot as plt

# Racunanje GC-skew vrednosti
def calculate_skew(text):
    skew = [0 for c in text]
    
    last = 0
    
    for i in range(0,len(text)):
        
        if text[i] == 'g':
            skew[i] = last + 1
            
        elif text[i] == 'c':
            skew[i] = last - 1
            
        else:
            skew[i] = last
            
        last = skew[i]
            
    return skew


# Crtanje GC-skew grafika pomocu matplot biblioteke
def draw_skew(skew):
    x = [i for i in range(len(skew))]
        
    ax = plt.subplot()
    ax.plot(x, skew)
    
    ax.set(xlabel='G-C', ylabel='Nucleotide',
       title='Genome GC Skew')
    ax.grid()

    plt.show()
    
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
