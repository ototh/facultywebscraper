from Mechanical import *
from Civil import *
from Electrical import *
from Engineering_Tech import *
from Motorsports import *
from Systems import *
from EPIC import *
from MOSAIC import *
from Student_Development import *
from Dean import *
from Languages import*
from Physics import*

def main(): 
    all_URLs = []
    all_Profiles = []


    # department1 = Mechanical()
    # department2 = Civil()
    # department3 = Electrical()
    # department4 = Engineering_Tech()
    # department5 = Motorsports()
    # department6 = Systems()

    # #Unsure if needed 
    # department7 = EPIC()
    # department8 = MOSAIC()
    # department9 = Student_Development()
    # department10 = Dean()

    # all_URLs = department1.facultyURLs + department2.facultyURLs + department3.facultyURLs + department4.facultyURLs + department5.facultyURLs + department6.facultyURLs + department7.facultyURLs + department8.facultyURLs + department9.facultyURLs + department10.facultyURLs
    # all_Profiles = department1.facultyURLs + department2.facultyURLs + department3.facultyURLs + department4.facultyURLs + department5.facultyURLs + department6.facultyURLs + department7.facultyURLs + department8.facultyURLs + department9.facultyURLs + department10.facultyURLs


    lang = Languages()
    phys = Physics()

    all_URLs = phys.facultyURLs
    all_Profiles = phys.profiles


    print(all_URLs)

    #print(all_URLs)
    print("Num URLs: ", len(all_URLs))
    print("Num Profiles: ", len(all_Profiles))
    return

if __name__ == "__main__":
    main()