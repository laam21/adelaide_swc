#test for the function dna_starts_with

def dna_starts_with(string1,string2):
    return string1[0:len(string2)]==string2

def test_dna_starts_with_itself():
    dna='acgtgtcgat'
    assert dna_starts_with(dna,dna)

def test_dna_starts_with_one():
    assert dna_starts_with('cgtgc','c')

def test_dna_starts_with_bigger():
    dna='acgtgtcgat'
    assert dna_starts_with(dna,dna+dna)

test_dna_starts_with_itself()
test_dna_starts_with_one()
test_dna_starts_with_bigger()
