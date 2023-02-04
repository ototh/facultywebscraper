import pytest
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

#Mechanical
@pytest.fixture()
def urlListMech():
    urlListMech = ['https://mees.charlotte.edu//directory/jonathan-beaman', 'https://mees.charlotte.edu//directory/anthony-bombik', 'https://mees.charlotte.edu//directory/youxing-chen', 'https://mees.charlotte.edu//directory/harish-cherukuri', 'https://mees.charlotte.edu//directory/ahmed-el-ghannam', 'https://mees.charlotte.edu//directory/gloria-d-elliott', 'https://mees.charlotte.edu//directory/terence-j-fagan', 'https://mees.charlotte.edu//directory/amir-ghasemi', 'https://mees.charlotte.edu//directory/dr-m-garry-hodgins', 'https://mees.charlotte.edu//directory/robert-e-johnson', 'https://mees.charlotte.edu//directory/erina-joyee', 'https://mees.charlotte.edu//directory/russell-keanini', 'https://mees.charlotte.edu//directory/scott-david-kelly', 'https://mees.charlotte.edu//directory/kevin-lawton', 'https://mees.charlotte.edu//directory/charles-lee', 'https://mees.charlotte.edu//directory/bamdad-lessani', 'https://mees.charlotte.edu//directory/lin-ma', 'https://mees.charlotte.edu//directory/edward-p-morse', 'https://mees.charlotte.edu//directory/brigid-mullany', 'https://mees.charlotte.edu//directory/steven-r-patterson', 'https://mees.charlotte.edu//directory/jay-raja', 'https://mees.charlotte.edu//directory/praveen-ramaprabhu', 'https://mees.charlotte.edu//directory/jeffrey-raquet', 'https://mees.charlotte.edu//directory/steven-schmid', 'https://mees.charlotte.edu//directory/ronald-e-smelser', 'https://mees.charlotte.edu//directory/stuart-t-smith', 'https://mees.charlotte.edu//directory/alireza-tabarraei', 'https://mees.charlotte.edu//directory/mesbah-uddin', 'https://mees.charlotte.edu//directory/qiuming-wei', 'https://mees.charlotte.edu//directory/artur-wolek', 'https://mees.charlotte.edu//directory/jun-xu', 'https://mees.charlotte.edu//directory/terry-t-xu', 'https://mees.charlotte.edu//directory/hong-yang', 'https://mees.charlotte.edu//directory/haitao-zhang', 'https://mees.charlotte.edu//directory/naiquan-nigel-zheng', 'https://mees.charlotte.edu//directory/horacio-v-estrada', 'https://mees.charlotte.edu//directory/christopher-j-evans', 'https://mees.charlotte.edu//directory/jerre-m-hill', 'https://mees.charlotte.edu//directory/robert-j-hocken', 'https://mees.charlotte.edu//directory/ganesh-p-mohanty', 'https://mees.charlotte.edu//directory/edgar-g-munday', 'https://mees.charlotte.edu//directory/john-c-ziegert', 'https://mees.charlotte.edu//directory/james-fox', 'https://mees.charlotte.edu//directory/debbie-ginsburg', 'https://mees.charlotte.edu//directory/franklin-green']
    return urlListMech

@pytest.fixture()
def mechObj():
    mechObj = Mechanical()
    return mechObj.facultyURLs

def test_mechanical(urlListMech, mechObj):
    assert urlListMech == mechObj

#Civil
@pytest.fixture()
def urlListCivil():
    urlListCivil = ['https://cee.charlotte.edu//directory/james-e-amburgey-phd-pe', 'https://cee.charlotte.edu//directory/james-d-bowen-phd', 'https://cee.charlotte.edu//directory/olya-keen-phd-pe', 'https://cee.charlotte.edu//directory/mariya-munir-phd', 'https://cee.charlotte.edu//directory/william-l-saunders-jr-phd-pe', 'https://cee.charlotte.edu//directory/mei-sun-phd', 'https://cee.charlotte.edu//directory/jy-s-wu-phd-pe-ph', 'https://cee.charlotte.edu//directory/nicole-braxtan-phd', 'https://cee.charlotte.edu//directory/shen-en-chen-phd-pe', 'https://cee.charlotte.edu//directory/janos-gergely-phd-se-il-pe', 'https://cee.charlotte.edu//directory/timothy-kernicky-phd', 'https://cee.charlotte.edu//directory/brett-q-tempest-phd-pe', 'https://cee.charlotte.edu//directory/david-c-weggel-phd-pe', 'https://cee.charlotte.edu//directory/matthew-j-whelan-phd-pe', 'https://cee.charlotte.edu//directory/john-l-daniels-deng-pe', 'https://cee.charlotte.edu//directory/rajaram-janardhanam-phd', 'https://cee.charlotte.edu//directory/milind-v-khire-phd-pe-bcee', 'https://cee.charlotte.edu//directory/vincent-tobi-ogunro-phd', 'https://cee.charlotte.edu//directory/kimberly-warren-phd', 'https://cee.charlotte.edu//directory/wei-david-fan-phd-pe', 'https://cee.charlotte.edu//directory/martin-r-kane-phd-pe', 'https://cee.charlotte.edu//directory/david-w-naylor-pe', 'https://cee.charlotte.edu//directory/srinivas-pulugurtha-phd-pe', 'https://cee.charlotte.edu//directory/l-ellis-king-phd', 'https://cee.charlotte.edu//directory/david-t-young-phd-pe', 'https://cee.charlotte.edu//directory/david-m-bayer-phd', 'https://cee.charlotte.edu//directory/jack-b-evett-phd', 'https://cee.charlotte.edu//directory/johnny-graham-phd-pe', 'https://cee.charlotte.edu//directory/helene-hilger-phd-pe', 'https://cee.charlotte.edu//directory/xiuli-lin-phd', 'https://cee.charlotte.edu//directory/youngjin-park-phd', 'https://cee.charlotte.edu//directory/vacant', 'https://cee.charlotte.edu//directory/sara-watson', 'https://cee.charlotte.edu//directory/kim-wilson', 'https://cee.charlotte.edu//directory/ted-brown']
    return urlListCivil

@pytest.fixture()
def civilObj():
    civilObj = Civil()
    return civilObj.facultyURLs

def test_civil(urlListCivil, civilObj):
    assert urlListCivil == civilObj

#Electrical
@pytest.fixture()
def urlListElectrical():
    urlListElectrical = ['https://ece.charlotte.edu/directory/dr-minhaj-alam-phd', 'https://ece.charlotte.edu/directory/dr-yawo-h-amengonu-phd', 'https://ece.charlotte.edu/directory/dr-ahmed-arafa-phd', 'https://ece.charlotte.edu/directory/ms-nabila-nan-bousaba', 'https://ece.charlotte.edu/directory/dr-valentina-cecchi-phd', 'https://ece.charlotte.edu/directory/dr-badrul-chowdhury-phd', 'https://ece.charlotte.edu/directory/dr-jim-conrad-phd', 'https://ece.charlotte.edu/directory/dr-robert-cox-phd', 'https://ece.charlotte.edu/directory/dr-farah-deeba-phd', 'https://ece.charlotte.edu/directory/dr-abasifreke-ebong-phd', 'https://ece.charlotte.edu/directory/dr-wei-gao-phd', 'https://ece.charlotte.edu/directory/dr-mohamed-ali-hasan-phd', 'https://ece.charlotte.edu/directory/dr-jeremy-holleman-phd', 'https://ece.charlotte.edu/directory/dr-sukumar-kamalasadan-phd', 'https://ece.charlotte.edu/directory/dr-dipankar-maity-phd', 'https://ece.charlotte.edu/directory/dr-madhav-manjrekar-phd', 'https://ece.charlotte.edu/directory/dr-michael-mazzola', 'https://ece.charlotte.edu/directory/dr-mario-j-mencagli-phd', 'https://ece.charlotte.edu/directory/dr-arindam-mukherjee-phd', 'https://ece.charlotte.edu/directory/dr-asis-nasipuri-phd', 'https://ece.charlotte.edu/directory/dr-babak-parkhideh-phd', 'https://ece.charlotte.edu/directory/dr-arun-ravindran-phd', 'https://ece.charlotte.edu/directory/dr-benny-rodriguez-medina-phd', 'https://ece.charlotte.edu/directory/dr-fareena-saqib-phd', 'https://ece.charlotte.edu/directory/dr-ronald-sass-phd', 'https://ece.charlotte.edu/directory/dr-samuel-shue-phd', 'https://ece.charlotte.edu/directory/dr-courtney-smith-orr-phd', 'https://ece.charlotte.edu/directory/dr-kathryn-smith-phd', 'https://ece.charlotte.edu/directory/dr-hamed-tabkhi-phd', 
'https://ece.charlotte.edu/directory/dr-farid-tranjan-phd', 'https://ece.charlotte.edu/directory/dr-ke-cory-wang-phd', 'https://ece.charlotte.edu/directory/dr-thomas-p-weldon-phd-pe', 'https://ece.charlotte.edu/directory/dr-andrew-r-willis-phd', 'https://ece.charlotte.edu/directory/dr-jiang-linda-xie-phd', 'https://ece.charlotte.edu/directory/dr-yong-zhang-phd', 'https://ece.charlotte.edu/directory/dr-tiefu-zhao-phd', 'https://ece.charlotte.edu/directory/dr-lee-casperson-phd', 'https://ece.charlotte.edu/directory/dr-yogendra-kakad-phd', 'https://ece.charlotte.edu/directory/dr-raphael-tsu-phd', 'https://ece.charlotte.edu/directory/michaela-barger', 'https://ece.charlotte.edu/directory/cole-carter', 'https://ece.charlotte.edu/directory/eddie-hill', 'https://ece.charlotte.edu/directory/michele-wallace', 'https://ece.charlotte.edu/directory/jocelyn-westpfahl']
    return urlListElectrical

@pytest.fixture()
def elecObj():
    elecObj = Electrical()
    return elecObj.facultyURLs

def test_electrical(urlListElectrical, elecObj):
    assert urlListElectrical == elecObj

#Engineering Tech
@pytest.fixture()
def urlListEngTech():
    urlListEngTech = ['https://et.charlotte.edu//directory/nicole-barclay-phd', 'https://et.charlotte.edu//directory/michael-benjamin-phd-gsp', 'https://et.charlotte.edu//directory/anthony-tony-brizendine-phd-pe-pls', 'https://et.charlotte.edu//directory/aidan-f-browne-phd', 'https://et.charlotte.edu//directory/tara-cavalline-phd-pe', 'https://et.charlotte.edu//directory/yuting-tina-chen-phd', 'https://et.charlotte.edu//directory/don-chen-phd-leed-ap', 'https://et.charlotte.edu//directory/michelle-demers', 'https://et.charlotte.edu//directory/austin-fifield', 'https://et.charlotte.edu//directory/dr-claudia-garrido-martins', 'https://et.charlotte.edu//directory/wayne-goff', 'https://et.charlotte.edu//directory/ronald-graham-pe', 'https://et.charlotte.edu//directory/christopher-green-phd', 'https://et.charlotte.edu//directory/rodward-hewlin-jr-phd', 'https://et.charlotte.edu//directory/jeffrey-kimble-edd', 'https://et.charlotte.edu//directory/thomas-nicholas-ii-phd-pe', 'https://et.charlotte.edu//directory/maciej-noras-phd', 'https://et.charlotte.edu//directory/jaewon-oh-phd', 'https://et.charlotte.edu//directory/carlos-orozco-phd', 'https://et.charlotte.edu//directory/stephanie-f-pilkington-phd', 'https://et.charlotte.edu//directory/jacelyn-rice-boayue-phd', 'https://et.charlotte.edu//directory/alison-sears-phd', 'https://et.charlotte.edu//directory/omidreza-shoghli-phd', 'https://et.charlotte.edu//directory/elizabeth-smith-phd-pe', 'https://et.charlotte.edu//directory/michael-smith-phd', 'https://et.charlotte.edu//directory/jake-smithwick-phd-mpa', 'https://et.charlotte.edu//directory/weimin-wang-phd', 'https://et.charlotte.edu//directory/wesley-williams-phd', 'https://et.charlotte.edu//directory/david-yarbrough-pe', 'https://et.charlotte.edu//directory/ambrose-barry', 'https://et.charlotte.edu//directory/nan-byars', 'https://et.charlotte.edu//directory/cheng-liu', 'https://et.charlotte.edu//directory/charles-mobley', 'https://et.charlotte.edu//directory/ronald-priebe', 'https://et.charlotte.edu//directory/barry-sherlock-phd', 'https://et.charlotte.edu//directory/rachel-powell']
    return urlListEngTech

@pytest.fixture()
def engTechObj():
    engTechObj = Engineering_Tech()
    return engTechObj.facultyURLs

def test_engTech(urlListEngTech, engTechObj):
    assert urlListEngTech == engTechObj

#Motorsports
@pytest.fixture()
def urlListMotorsports():
    urlListMotorsports = ['https://motorsports.charlotte.edu/directory/mesbah-uddin', 'https://motorsports.charlotte.edu/directory/howie-fang', 'https://motorsports.charlotte.edu/directory/james-fox', 'https://motorsports.charlotte.edu/directory/amir-ghasemi', 'https://motorsports.charlotte.edu/directory/jun-xu']
    return urlListMotorsports

@pytest.fixture()
def motorsportsObj():
    motorsportsObj = Motorsports()
    return motorsportsObj.facultyURLs

def test_motorsports(urlListMotorsports, motorsportsObj):
    assert urlListMotorsports == motorsportsObj

#Systems
@pytest.fixture()
def urlListSystems():
    urlListSystems = ['https://seem.charlotte.edu/directory/dr-linquan-bai', 'https://seem.charlotte.edu/directory/dr-badrul-chowdhury', 'https://seem.charlotte.edu/directory/dr-tao-hong', 'https://seem.charlotte.edu/directory/dr-simon-m-hsiang-pe-cpe', 'https://seem.charlotte.edu/directory/dr-churlzu-lim', 'https://seem.charlotte.edu/directory/dr-agnes-galambosi-ozelkan', 'https://seem.charlotte.edu/directory/dr-ertunga-c-ozelkan', 'https://seem.charlotte.edu/directory/dr-yesim-sireli', 'https://seem.charlotte.edu/directory/john-f-small', 'https://seem.charlotte.edu/directory/dr-s-gary-teng-pe', 'https://seem.charlotte.edu/directory/dr-guanglin-xu', 'https://seem.charlotte.edu/directory/dr-lei-zhu', 'https://seem.charlotte.edu/directory/dr-vishnu-girishan-prabhu', 'https://seem.charlotte.edu/directory/alexis-jennings', 'https://seem.charlotte.edu/directory/joan-lemcke']
    return urlListSystems

@pytest.fixture()
def systemsObj():
    systemsObj = Systems()
    return systemsObj.facultyURLs

def test_systems(urlListSystems, systemsObj):
    assert urlListSystems == systemsObj

#EPIC
@pytest.fixture()
def urlListEPIC():
    urlListEPIC = ['https://epic.charlotte.edu/directory/mike-mazzola', 'https://epic.charlotte.edu/directory/robert-cox', 'https://epic.charlotte.edu/directory/lori-brown', 'https://epic.charlotte.edu/directory/marion-cantor', 'https://epic.charlotte.edu/directory/valentina-cecchi-0', 'https://epic.charlotte.edu/directory/youxing-chen', 'https://epic.charlotte.edu/directory/badrul-chowdhury', 'https://epic.charlotte.edu/directory/abasifreke-ebong', 'https://epic.charlotte.edu/directory/balu-elias-george', 'https://epic.charlotte.edu/directory/daniel-evans', 'https://epic.charlotte.edu/directory/jacob-falkiewicz', 'https://epic.charlotte.edu/directory/benjamin-futrell', 'https://epic.charlotte.edu/directory/jim-gafford', 'https://epic.charlotte.edu/directory/tao-hong-0', 'https://epic.charlotte.edu/directory/shannon-jenkins', 'https://epic.charlotte.edu/directory/sukumar-kamalasadan-1', 'https://epic.charlotte.edu/directory/timothy-kernicky', 'https://epic.charlotte.edu/directory/saffeer-m-khan', 'https://epic.charlotte.edu/directory/milind-khire', 'https://epic.charlotte.edu/directory/andrew-leclair', 'https://epic.charlotte.edu/directory/madhav-manjrekar', 'https://epic.charlotte.edu/directory/william-mendez', 'https://epic.charlotte.edu/directory/robin-moose', 'https://epic.charlotte.edu/directory/youngjin-park', 'https://epic.charlotte.edu/directory/babak-parkhideh-0', 'https://epic.charlotte.edu/directory/nenad-sarunac-0', 'https://epic.charlotte.edu/directory/ehab-shoubaki', 'https://epic.charlotte.edu/directory/matthew-whelan-0', 'https://epic.charlotte.edu/directory/tiefu-zhao-0']
    return urlListEPIC

@pytest.fixture()
def epicObj():
    epicObj = EPIC()
    return epicObj.facultyURLs

def test_epic(urlListEPIC, epicObj):
    assert urlListEPIC == epicObj

#MOSAIC
@pytest.fixture()
def urlListMOSAIC():
    urlListMOSAIC = ['https://engrmosaic.charlotte.edu/directory/sean-desgraves', 'https://engrmosaic.charlotte.edu/directory/rodney-dyer', 'https://engrmosaic.charlotte.edu/directory/jason-edgecombe', 'https://engrmosaic.charlotte.edu/directory/eric-rhodes', 'https://engrmosaic.charlotte.edu/directory/andrew-verner', 'https://engrmosaic.charlotte.edu/directory/dave-whisler']
    return urlListMOSAIC

@pytest.fixture()
def mosaicObj():
    mosaicObj = MOSAIC()
    return mosaicObj.facultyURLs

def test_mosaic(urlListMOSAIC, mosaicObj):
    assert urlListMOSAIC == mosaicObj

#Student Development
@pytest.fixture()
def urlListStudentDev():
    urlListStudentDev = ['https://osds.charlotte.edu/directory/dr-cathy-blat', 'https://osds.charlotte.edu/directory/gina-robinson', 'https://osds.charlotte.edu/directory/sid-alvis-bsee-nc-pe-nuclear-plant-design-programs-human-performance-continuous', 'https://osds.charlotte.edu/directory/rachael-ohu-phd-msc-structural-engineering-structural-strengthening-and-rehabilitation', 'https://osds.charlotte.edu/directory/jenny-becic', 
'https://osds.charlotte.edu/directory/bianca-fruscello', 'https://osds.charlotte.edu/directory/gwen-gill-msne-nuclear-engineering-pe-jd-senior-engineer-intellectual-property-business', 'https://osds.charlotte.edu/directory/courtney-green-phd-pe-structural-and-material-forensics-project-engineer', 'https://osds.charlotte.edu/directory/cindy-gregory', 'https://osds.charlotte.eduhttps://osds.charlotte.edu/directory/meg-harkins-ms-env-sci-pe-hazardous-waste-management-permitting-and-remediation-consultant', 'https://osds.charlotte.edu/directory/jim-hartman-mba-communication-systems-and-chemical-process-industry-business-development', 'https://osds.charlotte.edu/directory/shannon-keys', 'https://osds.charlotte.edu/directory/dan-latta-mce-pe-pls-urban-land-design-and-development-principal-and-chief-engineer', 'https://osds.charlotte.edu/directory/joan-lemcke', 'https://osds.charlotte.edu/directory/kevin-lindsay-ms-physics-mba-space-telescope-senior-research-and-instrument-analyst', 'https://osds.charlotte.edu/directory/chris-mcdaniel-ms-engrenv-mgmt-major-usaf-ret-facilities-and-environmental-programs', 'https://osds.charlotte.edu/directory/yolanda-mcilwaine-0', 'https://osds.charlotte.edu/directory/sherman-mumford-ms-engineering-management-manufacturing-operations-manager-quality-systems', 'https://osds.charlotte.edu/directory/michelle-prasad', 'https://osds.charlotte.edu/directory/linda-thurman-ma-advising-and-career-services']
    return urlListStudentDev

@pytest.fixture()
def studentDevObj():
    studentDevObj = Student_Development()
    return studentDevObj.facultyURLs

def test_studentDevelopment(urlListStudentDev, studentDevObj):
    assert urlListStudentDev == studentDevObj

#Dean
@pytest.fixture()
def urlListDean():
    urlListDean = ['https://engr.charlotte.edu/directory/robert-keynton']
    return urlListDean

@pytest.fixture()
def deanObj():
    deanObj = Dean()
    return deanObj.facultyURLs

def test_dean(urlListDean, deanObj):
    assert urlListDean == deanObj


#All Engineering URLS
@pytest.fixture()
def urlListALL():
    urlListALL = ['https://mees.charlotte.edu//directory/jonathan-beaman', 'https://mees.charlotte.edu//directory/anthony-bombik', 'https://mees.charlotte.edu//directory/youxing-chen', 'https://mees.charlotte.edu//directory/harish-cherukuri', 'https://mees.charlotte.edu//directory/ahmed-el-ghannam', 'https://mees.charlotte.edu//directory/gloria-d-elliott', 'https://mees.charlotte.edu//directory/terence-j-fagan', 'https://mees.charlotte.edu//directory/amir-ghasemi', 'https://mees.charlotte.edu//directory/dr-m-garry-hodgins', 'https://mees.charlotte.edu//directory/robert-e-johnson', 'https://mees.charlotte.edu//directory/erina-joyee', 'https://mees.charlotte.edu//directory/russell-keanini', 'https://mees.charlotte.edu//directory/scott-david-kelly', 'https://mees.charlotte.edu//directory/kevin-lawton', 'https://mees.charlotte.edu//directory/charles-lee', 'https://mees.charlotte.edu//directory/bamdad-lessani', 'https://mees.charlotte.edu//directory/lin-ma', 'https://mees.charlotte.edu//directory/edward-p-morse', 'https://mees.charlotte.edu//directory/brigid-mullany', 'https://mees.charlotte.edu//directory/steven-r-patterson', 'https://mees.charlotte.edu//directory/jay-raja', 'https://mees.charlotte.edu//directory/praveen-ramaprabhu', 'https://mees.charlotte.edu//directory/jeffrey-raquet', 'https://mees.charlotte.edu//directory/steven-schmid', 'https://mees.charlotte.edu//directory/ronald-e-smelser', 'https://mees.charlotte.edu//directory/stuart-t-smith', 'https://mees.charlotte.edu//directory/alireza-tabarraei', 'https://mees.charlotte.edu//directory/mesbah-uddin', 'https://mees.charlotte.edu//directory/qiuming-wei', 'https://mees.charlotte.edu//directory/artur-wolek', 'https://mees.charlotte.edu//directory/jun-xu', 'https://mees.charlotte.edu//directory/terry-t-xu', 'https://mees.charlotte.edu//directory/hong-yang', 'https://mees.charlotte.edu//directory/haitao-zhang', 'https://mees.charlotte.edu//directory/naiquan-nigel-zheng', 'https://mees.charlotte.edu//directory/horacio-v-estrada', 'https://mees.charlotte.edu//directory/christopher-j-evans', 'https://mees.charlotte.edu//directory/jerre-m-hill', 'https://mees.charlotte.edu//directory/robert-j-hocken', 'https://mees.charlotte.edu//directory/ganesh-p-mohanty', 'https://mees.charlotte.edu//directory/edgar-g-munday', 'https://mees.charlotte.edu//directory/john-c-ziegert', 'https://mees.charlotte.edu//directory/james-fox', 'https://mees.charlotte.edu//directory/debbie-ginsburg', 'https://mees.charlotte.edu//directory/franklin-green', 'https://cee.charlotte.edu//directory/james-e-amburgey-phd-pe', 'https://cee.charlotte.edu//directory/james-d-bowen-phd', 'https://cee.charlotte.edu//directory/olya-keen-phd-pe', 'https://cee.charlotte.edu//directory/mariya-munir-phd', 'https://cee.charlotte.edu//directory/william-l-saunders-jr-phd-pe', 'https://cee.charlotte.edu//directory/mei-sun-phd', 'https://cee.charlotte.edu//directory/jy-s-wu-phd-pe-ph', 'https://cee.charlotte.edu//directory/nicole-braxtan-phd', 'https://cee.charlotte.edu//directory/shen-en-chen-phd-pe', 'https://cee.charlotte.edu//directory/janos-gergely-phd-se-il-pe', 'https://cee.charlotte.edu//directory/timothy-kernicky-phd', 'https://cee.charlotte.edu//directory/brett-q-tempest-phd-pe', 'https://cee.charlotte.edu//directory/david-c-weggel-phd-pe', 'https://cee.charlotte.edu//directory/matthew-j-whelan-phd-pe', 'https://cee.charlotte.edu//directory/john-l-daniels-deng-pe', 'https://cee.charlotte.edu//directory/rajaram-janardhanam-phd', 'https://cee.charlotte.edu//directory/milind-v-khire-phd-pe-bcee', 'https://cee.charlotte.edu//directory/vincent-tobi-ogunro-phd', 'https://cee.charlotte.edu//directory/kimberly-warren-phd', 'https://cee.charlotte.edu//directory/wei-david-fan-phd-pe', 'https://cee.charlotte.edu//directory/martin-r-kane-phd-pe', 'https://cee.charlotte.edu//directory/david-w-naylor-pe', 'https://cee.charlotte.edu//directory/srinivas-pulugurtha-phd-pe', 'https://cee.charlotte.edu//directory/l-ellis-king-phd', 'https://cee.charlotte.edu//directory/david-t-young-phd-pe', 'https://cee.charlotte.edu//directory/david-m-bayer-phd', 'https://cee.charlotte.edu//directory/jack-b-evett-phd', 'https://cee.charlotte.edu//directory/johnny-graham-phd-pe', 'https://cee.charlotte.edu//directory/helene-hilger-phd-pe', 'https://cee.charlotte.edu//directory/xiuli-lin-phd', 'https://cee.charlotte.edu//directory/youngjin-park-phd', 'https://cee.charlotte.edu//directory/vacant', 'https://cee.charlotte.edu//directory/sara-watson', 'https://cee.charlotte.edu//directory/kim-wilson', 'https://cee.charlotte.edu//directory/ted-brown', 'https://ece.charlotte.edu/directory/dr-minhaj-alam-phd', 'https://ece.charlotte.edu/directory/dr-yawo-h-amengonu-phd', 'https://ece.charlotte.edu/directory/dr-ahmed-arafa-phd', 'https://ece.charlotte.edu/directory/ms-nabila-nan-bousaba', 'https://ece.charlotte.edu/directory/dr-valentina-cecchi-phd', 'https://ece.charlotte.edu/directory/dr-badrul-chowdhury-phd', 'https://ece.charlotte.edu/directory/dr-jim-conrad-phd', 'https://ece.charlotte.edu/directory/dr-robert-cox-phd', 'https://ece.charlotte.edu/directory/dr-farah-deeba-phd', 'https://ece.charlotte.edu/directory/dr-abasifreke-ebong-phd', 'https://ece.charlotte.edu/directory/dr-wei-gao-phd', 'https://ece.charlotte.edu/directory/dr-mohamed-ali-hasan-phd', 'https://ece.charlotte.edu/directory/dr-jeremy-holleman-phd', 'https://ece.charlotte.edu/directory/dr-sukumar-kamalasadan-phd', 'https://ece.charlotte.edu/directory/dr-dipankar-maity-phd', 'https://ece.charlotte.edu/directory/dr-madhav-manjrekar-phd', 'https://ece.charlotte.edu/directory/dr-michael-mazzola', 'https://ece.charlotte.edu/directory/dr-mario-j-mencagli-phd', 'https://ece.charlotte.edu/directory/dr-arindam-mukherjee-phd', 'https://ece.charlotte.edu/directory/dr-asis-nasipuri-phd', 'https://ece.charlotte.edu/directory/dr-babak-parkhideh-phd', 'https://ece.charlotte.edu/directory/dr-arun-ravindran-phd', 'https://ece.charlotte.edu/directory/dr-benny-rodriguez-medina-phd', 'https://ece.charlotte.edu/directory/dr-fareena-saqib-phd', 'https://ece.charlotte.edu/directory/dr-ronald-sass-phd', 'https://ece.charlotte.edu/directory/dr-samuel-shue-phd', 'https://ece.charlotte.edu/directory/dr-courtney-smith-orr-phd', 'https://ece.charlotte.edu/directory/dr-kathryn-smith-phd', 'https://ece.charlotte.edu/directory/dr-hamed-tabkhi-phd', 
'https://ece.charlotte.edu/directory/dr-farid-tranjan-phd', 'https://ece.charlotte.edu/directory/dr-ke-cory-wang-phd', 'https://ece.charlotte.edu/directory/dr-thomas-p-weldon-phd-pe', 'https://ece.charlotte.edu/directory/dr-andrew-r-willis-phd', 'https://ece.charlotte.edu/directory/dr-jiang-linda-xie-phd', 'https://ece.charlotte.edu/directory/dr-yong-zhang-phd', 'https://ece.charlotte.edu/directory/dr-tiefu-zhao-phd', 'https://ece.charlotte.edu/directory/dr-lee-casperson-phd', 'https://ece.charlotte.edu/directory/dr-yogendra-kakad-phd', 'https://ece.charlotte.edu/directory/dr-raphael-tsu-phd', 'https://ece.charlotte.edu/directory/michaela-barger', 'https://ece.charlotte.edu/directory/cole-carter', 'https://ece.charlotte.edu/directory/eddie-hill', 'https://ece.charlotte.edu/directory/michele-wallace', 'https://ece.charlotte.edu/directory/jocelyn-westpfahl', 'https://et.charlotte.edu//directory/nicole-barclay-phd', 'https://et.charlotte.edu//directory/michael-benjamin-phd-gsp', 'https://et.charlotte.edu//directory/anthony-tony-brizendine-phd-pe-pls', 'https://et.charlotte.edu//directory/aidan-f-browne-phd', 'https://et.charlotte.edu//directory/tara-cavalline-phd-pe', 'https://et.charlotte.edu//directory/yuting-tina-chen-phd', 'https://et.charlotte.edu//directory/don-chen-phd-leed-ap', 'https://et.charlotte.edu//directory/michelle-demers', 'https://et.charlotte.edu//directory/austin-fifield', 'https://et.charlotte.edu//directory/dr-claudia-garrido-martins', 'https://et.charlotte.edu//directory/wayne-goff', 'https://et.charlotte.edu//directory/ronald-graham-pe', 'https://et.charlotte.edu//directory/christopher-green-phd', 'https://et.charlotte.edu//directory/rodward-hewlin-jr-phd', 'https://et.charlotte.edu//directory/jeffrey-kimble-edd', 'https://et.charlotte.edu//directory/thomas-nicholas-ii-phd-pe', 'https://et.charlotte.edu//directory/maciej-noras-phd', 'https://et.charlotte.edu//directory/jaewon-oh-phd', 'https://et.charlotte.edu//directory/carlos-orozco-phd', 'https://et.charlotte.edu//directory/stephanie-f-pilkington-phd', 'https://et.charlotte.edu//directory/jacelyn-rice-boayue-phd', 'https://et.charlotte.edu//directory/alison-sears-phd', 'https://et.charlotte.edu//directory/omidreza-shoghli-phd', 'https://et.charlotte.edu//directory/elizabeth-smith-phd-pe', 'https://et.charlotte.edu//directory/michael-smith-phd', 'https://et.charlotte.edu//directory/jake-smithwick-phd-mpa', 'https://et.charlotte.edu//directory/weimin-wang-phd', 'https://et.charlotte.edu//directory/wesley-williams-phd', 'https://et.charlotte.edu//directory/david-yarbrough-pe', 'https://et.charlotte.edu//directory/ambrose-barry', 'https://et.charlotte.edu//directory/nan-byars', 'https://et.charlotte.edu//directory/cheng-liu', 'https://et.charlotte.edu//directory/charles-mobley', 'https://et.charlotte.edu//directory/ronald-priebe', 'https://et.charlotte.edu//directory/barry-sherlock-phd', 'https://et.charlotte.edu//directory/rachel-powell', 'https://motorsports.charlotte.edu/directory/mesbah-uddin', 'https://motorsports.charlotte.edu/directory/howie-fang', 'https://motorsports.charlotte.edu/directory/james-fox', 'https://motorsports.charlotte.edu/directory/amir-ghasemi', 'https://motorsports.charlotte.edu/directory/jun-xu', 'https://seem.charlotte.edu/directory/dr-linquan-bai', 'https://seem.charlotte.edu/directory/dr-badrul-chowdhury', 'https://seem.charlotte.edu/directory/dr-tao-hong', 'https://seem.charlotte.edu/directory/dr-simon-m-hsiang-pe-cpe', 'https://seem.charlotte.edu/directory/dr-churlzu-lim', 'https://seem.charlotte.edu/directory/dr-agnes-galambosi-ozelkan', 'https://seem.charlotte.edu/directory/dr-ertunga-c-ozelkan', 'https://seem.charlotte.edu/directory/dr-yesim-sireli', 'https://seem.charlotte.edu/directory/john-f-small', 'https://seem.charlotte.edu/directory/dr-s-gary-teng-pe', 'https://seem.charlotte.edu/directory/dr-guanglin-xu', 'https://seem.charlotte.edu/directory/dr-lei-zhu', 'https://seem.charlotte.edu/directory/dr-vishnu-girishan-prabhu', 'https://seem.charlotte.edu/directory/alexis-jennings', 'https://seem.charlotte.edu/directory/joan-lemcke', 'https://epic.charlotte.edu/directory/mike-mazzola', 'https://epic.charlotte.edu/directory/robert-cox', 'https://epic.charlotte.edu/directory/lori-brown', 'https://epic.charlotte.edu/directory/marion-cantor', 'https://epic.charlotte.edu/directory/valentina-cecchi-0', 'https://epic.charlotte.edu/directory/youxing-chen', 'https://epic.charlotte.edu/directory/badrul-chowdhury', 'https://epic.charlotte.edu/directory/abasifreke-ebong', 'https://epic.charlotte.edu/directory/balu-elias-george', 'https://epic.charlotte.edu/directory/daniel-evans', 'https://epic.charlotte.edu/directory/jacob-falkiewicz', 'https://epic.charlotte.edu/directory/benjamin-futrell', 'https://epic.charlotte.edu/directory/jim-gafford', 'https://epic.charlotte.edu/directory/tao-hong-0', 'https://epic.charlotte.edu/directory/shannon-jenkins', 'https://epic.charlotte.edu/directory/sukumar-kamalasadan-1', 'https://epic.charlotte.edu/directory/timothy-kernicky', 'https://epic.charlotte.edu/directory/saffeer-m-khan', 'https://epic.charlotte.edu/directory/milind-khire', 'https://epic.charlotte.edu/directory/andrew-leclair', 'https://epic.charlotte.edu/directory/madhav-manjrekar', 'https://epic.charlotte.edu/directory/william-mendez', 'https://epic.charlotte.edu/directory/robin-moose', 'https://epic.charlotte.edu/directory/youngjin-park', 'https://epic.charlotte.edu/directory/babak-parkhideh-0', 'https://epic.charlotte.edu/directory/nenad-sarunac-0', 'https://epic.charlotte.edu/directory/ehab-shoubaki', 'https://epic.charlotte.edu/directory/matthew-whelan-0', 'https://epic.charlotte.edu/directory/tiefu-zhao-0', 'https://engrmosaic.charlotte.edu/directory/sean-desgraves', 'https://engrmosaic.charlotte.edu/directory/rodney-dyer', 'https://engrmosaic.charlotte.edu/directory/jason-edgecombe', 'https://engrmosaic.charlotte.edu/directory/eric-rhodes', 'https://engrmosaic.charlotte.edu/directory/andrew-verner', 'https://engrmosaic.charlotte.edu/directory/dave-whisler', 'https://osds.charlotte.edu/directory/dr-cathy-blat', 'https://osds.charlotte.edu/directory/gina-robinson', 'https://osds.charlotte.edu/directory/sid-alvis-bsee-nc-pe-nuclear-plant-design-programs-human-performance-continuous', 'https://osds.charlotte.edu/directory/rachael-ohu-phd-msc-structural-engineering-structural-strengthening-and-rehabilitation', 'https://osds.charlotte.edu/directory/jenny-becic', 
'https://osds.charlotte.edu/directory/bianca-fruscello', 'https://osds.charlotte.edu/directory/gwen-gill-msne-nuclear-engineering-pe-jd-senior-engineer-intellectual-property-business', 'https://osds.charlotte.edu/directory/courtney-green-phd-pe-structural-and-material-forensics-project-engineer', 'https://osds.charlotte.edu/directory/cindy-gregory', 'https://osds.charlotte.eduhttps://osds.charlotte.edu/directory/meg-harkins-ms-env-sci-pe-hazardous-waste-management-permitting-and-remediation-consultant', 'https://osds.charlotte.edu/directory/jim-hartman-mba-communication-systems-and-chemical-process-industry-business-development', 'https://osds.charlotte.edu/directory/shannon-keys', 'https://osds.charlotte.edu/directory/dan-latta-mce-pe-pls-urban-land-design-and-development-principal-and-chief-engineer', 'https://osds.charlotte.edu/directory/joan-lemcke', 'https://osds.charlotte.edu/directory/kevin-lindsay-ms-physics-mba-space-telescope-senior-research-and-instrument-analyst', 'https://osds.charlotte.edu/directory/chris-mcdaniel-ms-engrenv-mgmt-major-usaf-ret-facilities-and-environmental-programs', 'https://osds.charlotte.edu/directory/yolanda-mcilwaine-0', 'https://osds.charlotte.edu/directory/sherman-mumford-ms-engineering-management-manufacturing-operations-manager-quality-systems', 'https://osds.charlotte.edu/directory/michelle-prasad', 'https://osds.charlotte.edu/directory/linda-thurman-ma-advising-and-career-services', 'https://engr.charlotte.edu/directory/robert-keynton']
    return urlListALL

@pytest.fixture()
def engObj():
    all_URLs = []
    all_URLs = Mechanical().facultyURLs + Civil().facultyURLs + Electrical().facultyURLs + Engineering_Tech().facultyURLs + Motorsports().facultyURLs + Systems().facultyURLs + EPIC().facultyURLs + MOSAIC().facultyURLs + Student_Development().facultyURLs + Dean().facultyURLs
    return all_URLs

def test_all(urlListALL, engObj):
    assert urlListALL == engObj
