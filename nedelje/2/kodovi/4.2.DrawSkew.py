import matplotlib.pyplot as plt

def draw_skew(skew):
    x = [i for i in range(len(skew))]
        
    ax = plt.subplot()
    ax.plot(x, skew)
    
    ax.set(xlabel='G-C', ylabel='Nucleotide',
       title='Genome GC Skew')
    ax.grid()

    plt.show()