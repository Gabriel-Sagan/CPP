import random
#diationic chords
Cmaj7 = [36, 40, 43, 47]
Dmin7 = [38, 41, 45, 48]
Emin7 = [40, 43, 47, 50]
Fmaj7 = [41, 45, 48, 52]
Gdom7 = [43, 47, 50, 53]
Amin7 = [45, 48, 52, 55]
Bdim7 = [47, 50, 53, 57]

#secondary dominants
Ddom7 = [38, 42, 45, 48]
Edom7 = [40, 44, 47, 50] #used in minor as V
Adom7 = [45, 49, 52, 55]
Bdom7 = [47, 51, 54, 57]
Cdom7 = [36, 40, 43, 46]
Gbdom7 = [42, 46, 49, 52]

#predominants
Edim7 = [40, 43, 46, 50]
Fsdim7 = [42, 45, 48, 52]
Gmin7 = [43, 46, 50, 53]
Csdim7 = [37, 40, 43, 47]
Bmin7 = [47, 50, 54, 57]
Fsmin7 = [42, 45, 49, 52]

#other
Afulldim7 = [45, 48, 51, 54]


#major ac and hcs
V_I = [Gdom7, Cmaj7]
ii_V = [Dmin7, Gdom7]
MII_V = [Ddom7, Gdom7] 

#minor ac and hcs
V_i = [Edom7, Amin7]
ii0_V = [Bdim7, Edom7]
mII_V = [Bdom7, Edom7]

#dominant progressions in major:
MI = [Dmin7, Gdom7, Cmaj7]
Mii = [Edim7, Adom7, Dmin7]
Miii = [Fsdim7, Bdom7, Emin7]
MIV = [Gmin7, Cdom7, Fmaj7]
MV = [Amin7, Ddom7, Gdom7]
Mvi = [Bdim7, Edom7, Amin7]

#dominant progressions in minor
mii0 = [Csdim7, Gbdom7, Bmin7]
mV = [Fsmin7, Bdom7, Edom7]

#chord rules
major_first_chord = [Cmaj7]
minor_first_chord = [Amin7]

major_two_thru_five = [Mii, Miii, MIV, MV, Mvi]
minor_two_thru_five = [mii0, MI, Mii, mV, MIV]

major_diationic_chords = [Cmaj7, Dmin7, Fmaj7, Amin7]
minor_diationic_chords = [Amin7, Dmin7, Fmaj7]

chord_progression = []

#decides if major or minor
quality_choice = random.choice([True, False])

def major_chord_progression():
    
    while len(chord_progression) < 5:
        chord_pick = random.choice(major_diationic_chords)
        chord_progression.append(chord_pick)
    
    #replaces first chord with diationic chord
    chord_progression[0] = random.choice(major_first_chord)
    
    #75% chance each to replace 2nd-4th and 3rd-5th chord with secondary dominant progression.
    if random.random() < .75:
        if random.choice ([True, False]):
            sec_dom = random.choice(major_two_thru_five)
            chord_progression[1:4] = sec_dom
        else:
            sec_dom2 = random.choice(major_two_thru_five)
            chord_progression[2:5] = sec_dom2
        
    return chord_progression

def minor_chord_progression():
    
    while len(chord_progression) < 5:
        chord_pick = random.choice(minor_diationic_chords)
        chord_progression.append(chord_pick)
    
    #replaces first chord with diationic chord
    chord_progression[0] = random.choice(minor_first_chord)
    
    #75% for another 50% chance to replace 2-4th bar or 3-5th bar with a secondary ii V I
    if random.random() < .75:
        if random.choice ([True, False]):
            sec_dom = random.choice(minor_two_thru_five)
            chord_progression[1:4] = sec_dom
        else:
            sec_dom2 = random.choice(minor_two_thru_five)
            chord_progression[2:5] = sec_dom2
        
    return chord_progression
        
    
def hc():
    
    #major half cadences
    IV_ii_V = [Fmaj7, *ii_V]
    vi_ii_V = [Amin7, *ii_V]
    VI_ii_V = [Adom7, *ii_V]
    I_ii_V = [Cmaj7, *ii_V]
    
    IV_II_V = [Fmaj7, *MII_V]
    vi_II_V = [Amin7, *MII_V]
    VI_II_V = [Adom7, *MII_V]
    I_II_V = [Cmaj7, *MII_V]
    
    #minor half cadences
    iv_ii0_V = [Dmin7, *ii0_V]
    VI_ii0_V = [Fmaj7, *ii0_V]
    sVI_ii0_V =[Gbdom7, *ii0_V]
    i_ii0_V = [Amin7, *ii0_V]
    
    iv_mII_V = [Dmin7, *mII_V]
    VI_mII_V = [Fmaj7, *mII_V]
    sVI_mII_V =[Gbdom7, *mII_V]
    i_mII_V = [Amin7, *mII_V]
    

    major_half_cadences = [IV_ii_V, vi_ii_V, VI_ii_V, I_ii_V, IV_II_V, vi_II_V, VI_II_V, I_II_V]
    minor_half_cadences = [iv_ii0_V, VI_ii0_V, sVI_ii0_V, i_ii0_V, iv_mII_V, VI_mII_V, sVI_mII_V, i_mII_V]


    if quality_choice:
        
        selected_hc = random.choice(major_half_cadences)
    else:
        selected_hc = random.choice(minor_half_cadences)
        
    return selected_hc


def ac():
    #major authentic cadences
    ii_V_I = [Dmin7, *V_I]
    IV_V_I = [Fmaj7, *V_I]
    II_V_I = [Ddom7, *V_I]

    
    #minor authentic cadences
    ii0_V_i = [Bdim7, *V_i]
    iv_V_i = [Dmin7, *V_i]
    II_V_i = [Bdom7, *V_i]
    
    
    major_authentic_cadences = [ii_V_I, IV_V_I, II_V_I]
    minor_authentic_cadences = [ii0_V_i, iv_V_i, II_V_i]


    if quality_choice:
        
        selected_ac = random.choice(major_authentic_cadences)
    else:
        selected_ac = random.choice(minor_authentic_cadences)
        
    return selected_ac


if quality_choice:
    
    first_5 = major_chord_progression()
else:
    first_5 = minor_chord_progression()

def A():
    half_cadence = hc()
    full_a = first_5 + half_cadence
    return full_a

def Ap():
    authentic_cadence = ac()
    full_ap = first_5 + authentic_cadence
    return full_ap

B_quality = random.choice([True, False])
transposition_factor = random.choice([True, False])

chromatic_mediant = random.choice([3, 4, 8, 9])
Mm_chromatic_mediant = random.choice([0, 6, 7, 11])
mM_chromatic_mediant = random.choice([0, 1, 5, 6])

dominant = random.choice([5, 7])
Mm_dominant = random.choice([8, 10])
mM_dominant = random.choice([2, 4])

major_predom = random.choice([Dmin7, Fmaj7])
minor_predom = random.choice([Bdim7, Dmin7])
diminished_prog = ([Afulldim7, Dmin7])

M_B_hcs = random.choice([ii_V, MII_V])
m_B_hcs = random.choice([ii0_V, mII_V])

B_progression = []


def B():
    
    #creates B progression and replaces first chord with diatonic one
    #50% chance for major or minor
    while len(B_progression) < 6:
        if B_quality:
            chord_pick = random.choice(major_diationic_chords)
            B_progression.append(chord_pick)
            
        else:
            chord_pick = random.choice(minor_diationic_chords)
            B_progression.append(chord_pick)
    #replaces first thru fourth chord with a I ii or IV V I to establish new key center
    #40% chance to use a diminished progression
    if B_quality:
        B_progression[0] = major_first_chord[0]
        B_progression[1] = major_predom
        B_progression[2:4] = V_I
        if random.random() < .4:
            B_progression[4:6] = diminished_prog
    else: 
        B_progression[0] = minor_first_chord[0]
        B_progression[1] = minor_predom
        B_progression[2:4] = V_i
        if random.random() < .4:
            B_progression[4:6] = diminished_prog

    #transposes B section by chromatic mediant or dominant in relation to A
    if transposition_factor:
        if quality_choice == B_quality:
            for i in range(len(B_progression)):
                B_progression[i] = [num + chromatic_mediant for num in B_progression[i]]
        elif quality_choice and not B_quality:
            for i in range(len(B_progression)):
                B_progression[i] = [num + Mm_chromatic_mediant for num in B_progression[i]]
        elif not quality_choice and B_quality:
            for i in range(len(B_progression)):
                B_progression[i] = [num + mM_chromatic_mediant for num in B_progression[i]]
    else:
        if quality_choice == B_quality:
            for i in range(len(B_progression)):
                B_progression[i] = [num + dominant for num in B_progression[i]]
        elif quality_choice and not B_quality:
            for i in range(len(B_progression)):
                B_progression[i] = [num + Mm_dominant for num in B_progression[i]]
        elif not quality_choice and B_quality:
            for i in range(len(B_progression)):
                B_progression[i] = [num + mM_dominant for num in B_progression[i]]

    #adds a major or minor half cadence at the end 
    if quality_choice:
        B_progression.extend(M_B_hcs)
    else:
        B_progression.extend(m_B_hcs)
    
    return B_progression

transposition = random.randint(12,24)

def AABA():
    a = A()
    ap = Ap()
    b = B()
    aaba = a + ap + b + ap
    for i in range(len(aaba)):
        aaba[i] = [num + transposition for num in aaba[i]]
    return aaba

        
        
    
    
    