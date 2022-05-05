## mpfoster-scripts
# awk programs -- some were invoked using "nawk"; replace with "awk"
(Some of these are old and may need to be updated for newer versions of awk, and newer xpk and asg file formats)
 
         a2aaa  convert 1-letter codes to three-letter amino acid names
         aaa2a  convert 3-letter code to 1-leter codes
         T_cal  determine nmr probe temperature from separation of methanol peaks
         T_calg determine NMR probe temp. from glycerol peaks
         adj_asg        systemmatic correction of NV-format assignment file (ppm.out)
         adj_xpk        uniform adjustmet of nD peak positions (NV format)
         adjust adjust upl restraint files given a subject of restraints to correct
                variants: adjust2, adjust_bound
         adjust_leu     add 25% to upper bound of Val/Leu methyls in .upl files
         amb2brook      convert AMBER-format PDB to standard PDB
         analyzeXrst    read an XPLOR-format RST file and a PDB file and analyze
                        distances of protons involved in each rst.
                        useful for evaluating ambiguous or non-stereoassigned rst
         brukpar        interactively extract paramerters from an acqus file
         cat_ual        combine several upl/ual files and eliminate redundant restraints
         check_amb      append stereoassignment mappings from map file to ual/upl file
         compare_shifts compare shifts in two assignment files
         comp_str_shifts        compare shifts in two .str files
         dat2molmol     generate MOLMOL macro to display data on the CA atom
         dih2aco        convert XPLOR-format torsion angle restraints to CYANA format
         div_err        divide two columns of numbers with errors; report result and error
         dnabend.awk    extract DNA bend parameters from Curves 5.2 output
         dnagroove.awk  extract groove parameters from Curves 5.2 output
         eff_conc.awk   compute the effective concentration pd0 of two domains
                        connected by a flexible amino acid liker of L residues
         fasta2nv       generate an NV-format sequence file from a FASTA format file
         filter_and     check datafile against list and only retain those included
         filter_not     check datafile against list and report those not in list
         getgoodr2r1    run on mfdata file to get r2/r1 data for residues with 
                        r2 within one RMSD of mean and NOE > 0.5 and dr2r1 < 0.1*r2r1
         get_HNCAcb_dav calculate weighted average shift differences, H, N, CA, CB
         get_HN_dav     calculate weighted average shift differences, using H, N
         get_mfmodel    analyze MODELFREE output and extract optimal model
         get_mfF        extract F_test data from MODELFREE mfoutfile
         getmfpar       program to extract parameters from MODELFREE mfoutfile
         getfpar_sse    extract good parameters from MODELFREE mfoutfile
         getmfresults   extract MF parameters from MODELFREE mfoutfile
         getmfsse       extract SSE parameters from MODELFREE mfoutfile
         getmodels      process the MF output files and perform 
                        model selection procedure
         isnum  only print records that begin with a number
         make.a.table   generate an assignment table (byres)
         make_map_file  generate a map file from a pdbfile
         make_property_file     map property to atom (GRASP input)
         map2ca map a property to the CA
         map2res        map a property to the entire residue
         measure        measure distnace between two atoms in a PDB file
         mf2tensor      convert MODELFREE mfdata to TENSOR format
         nv3dto2dpks    project 3D NV xpk file onto 2D
         par    extract one parameter from bruker acqus file
         pipeXtonv      convert NMRPipe xpl file to NV format
         plcalc calculate the power level of a desired pulse given a known pulse length
                and power
         pwcalc calculate the pw given known pw and pl
         print_nvasgpks print assignments and shifts from NMRView xpk file
         readseqpdb     read the sequence from a PDB file
         rechain_pdb    add chain IDs to molecules in a PDB file
         renum_pdb      renumber pdb file
         rmsd   compute mean and standard deviation of a column of numbers
         res2mols       map property to CA radius -- MOLSCRIPT
         sfofreq                calculate spectrometer transmitter frequencies
         sortxplor      sort XPLOR restraints
         stereoasg_asg  replace non-stereo assigned proton names w/ the stereo names
                        in the assignment file
         stereoasg_ppm  searches through the .ppm file to identify non-stereoassigned
                        pairs that NOE to the same proton, and "stereo-assigns" them.
                        i.e. HB+ and HB- NOE to ALA_9.MB becomes
                        HB2 to ALA_9.MB and HB3 to ALA9_MB; The volumes are averaged
         stereocor      replace non-stereo assigned proton names w/ the stereo names
         stereoxpl      ifix stereoassigned protons -- xplor format
         torsion        measure torsion atom1 atom2 atom3 atom4 file.pdb
         trim   Calculates a statistically "trimmed" mean ; and outputs the trimed list
         trmean compute the 10% trimmed mean for a column of numbers
         vert2buried    read a .vert file produced by msmsContact
                        and report the atoms and residues found to be buried
         vert2residues  read a .vert file produced by msmsContact
                        and report the atoms and residues found to be buried
                        optional input of vertex density to calculate areas
         xpk2bound      generate upl or ual files from assigned NOE peaks
         xpk2xeasy      convert NV xpk file to XEASY format
         xplor2dyana    awk script convert xplor restraint files to dyana upl files
                        skip ambiguous restraints
         xplr2dy_atoms  translate XPLOR atoms to DYANA atoms
         
         # shell scripts
         pdb_to_xyzr    extract x,y,z from PDB file, generate radius of each atom
         print_acqu     extract key parameters from acqus file
