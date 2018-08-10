def create_string_from_path(path):

    dna_string = path[0][0].replace("'",'')

    for i in range(len(path)):
        dna_string += path[i][1].replace("'",'')[-1]

    return dna_string