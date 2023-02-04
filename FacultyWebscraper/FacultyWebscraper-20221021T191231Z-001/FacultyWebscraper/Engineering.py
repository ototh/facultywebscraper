from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

import time

import requests
from bs4 import BeautifulSoup


class Mechanical_Engineering:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://mees.charlotte.edu/"

        #Main directory
        URL = "https://mees.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://mees.charlotte.edu/directory-box/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://mees.charlotte.edu/directory/staff'

        #Main directory
        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        #Emeritus
        html_text = requests.get(URLemeritus)
        soup_Emeritus = BeautifulSoup(html_text.content, "html.parser")

        #Staff directory 
        html_text = requests.get(URLstaff)
        soup_Staff = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

        self.emeritusURLs = self.getFacultyURLs(baseURL, soup_Emeritus)
        self.emeritusProfiles = self.getProfilePage(self.emeritusURLs)

        self.staffURLs = self.getFacultyURLs(baseURL, soup_Staff)
        self.staffProfiles = self.getProfilePage(self.staffURLs)

        self.facultyURLs += self.emeritusURLs
        self.facultyURLs += self.staffURLs

        self.profiles += self.emeritusProfiles
        self.profiles += self.staffProfiles

class Civil_Engineering:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://cee.charlotte.edu/"
        URL = "https://cee.charlotte.edu/directory-box"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

class Electrical_Engineering:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://ece.charlotte.edu"

        #Main directory
        URL = "https://ece.charlotte.edu/directory/faculty"
        #Emeritus
        URLemeritus = 'https://ece.charlotte.edu/directory/professors-emeriti'
        #Staff directory - don't know if this is needed
        URLstaff = 'https://ece.charlotte.edu/directory/staff'

        #Main directory
        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        #Emeritus
        html_text = requests.get(URLemeritus)
        soup_Emeritus = BeautifulSoup(html_text.content, "html.parser")

        #Staff directory 
        html_text = requests.get(URLstaff)
        soup_Staff = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

        self.emeritusURLs = self.getFacultyURLs(baseURL, soup_Emeritus)
        self.emeritusProfiles = self.getProfilePage(self.emeritusURLs)

        self.staffURLs = self.getFacultyURLs(baseURL, soup_Staff)
        self.staffProfiles = self.getProfilePage(self.staffURLs)

        self.facultyURLs += self.emeritusURLs
        self.facultyURLs += self.staffURLs

        self.profiles += self.emeritusProfiles
        self.profiles += self.staffProfiles

class Engineering_Tech:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://et.charlotte.edu/"
        URL = "https://et.charlotte.edu/directory-box"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

class Motorsports:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://motorsports.charlotte.edu"
        URL = "https://motorsports.charlotte.edu/directory-box"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

class Systems_Engineering:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://seem.charlotte.edu"
        URL = "https://seem.charlotte.edu/directory-box"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

#The rest of these classes are the directories I'm not sure are necessary or not but I include anyway
#Contracts/Grants directory all have no profiles
#Faculty emeritus directory is just a pdf file, pretty sure it all just overlaps with emeritus directories in each department

class EPIC:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        #this one uses the stupid flip box thing and a raw link to the page
        soupList = soup.find_all(
            "a", href=True, alt=True, title=True)

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://epic.charlotte.edu"
        URL = "https://epic.charlotte.edu/epic-staff/9"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

class MOSAIC:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://engrmosaic.charlotte.edu"
        URL = "https://engrmosaic.charlotte.edu/directory-box"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

class Student_Development:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        #This one uses the same button as CCI I think
        soupList = soup.find_all(
            "a", {"class": "button button-gray"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory node-promoted clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://osds.charlotte.edu"
        URL = "https://osds.charlotte.edu/directory-list/faculty-and-staff"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

class Deans_Office:

    def getFacultyURLs(self, baseURL, soup):
        URLs = []
        soupList = soup.find_all(
            "a", {"class": "button button-green button-small"})

        for i in soupList:
            profURL = baseURL + i.get("href")
            URLs.append(profURL)

        return URLs

    def getProfilePage(self, facultyURLs):
        myList = []
        for i in facultyURLs:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, "html.parser")
                items = soup.find(
                    "article", {"class": "node node-directory clearfix"})

                for count, element in enumerate(items):
                    items[count] = element.getText()

                profileDict = {
                    'Title': soup.find("h1", {'class': 'page-header'}).getText(),
                    'Content': items,
                }
                myList.append(profileDict)
            except:
                print("Error: Doesn't have profile page")

        return myList

    def __init__(self):
        baseURL = "https://engr.charlotte.edu"
        URL = "https://engr.charlotte.edu/directory-box/dean%27s-office"

        html_text = requests.get(URL)
        soup = BeautifulSoup(html_text.content, "html.parser")

        self.facultyURLs = self.getFacultyURLs(baseURL, soup)
        self.profiles = self.getProfilePage(self.facultyURLs)

if __name__ == '__main__':
    #Mechanical
    department1 = Mechanical_Engineering()
    print("Num Mech URLs: ", len(department1.facultyURLs))    
    print("Num Mech Profiles: ", len(department1.profiles))
    
    #Civil
    department2 = Civil_Engineering()
    print("Num Civil URLs: ", len(department2.facultyURLs))    
    print("Num Civil Profiles: ", len(department2.profiles))

    #Electrical
    department3 = Electrical_Engineering()
    print("Num Electrical URLs: ", len(department3.facultyURLs))    
    print("Num Electrical Profiles: ", len(department3.profiles))

    #EngTech
    department4 = Engineering_Tech()
    print("Num EngTech URLs: ", len(department4.facultyURLs))    
    print("Num EngTech Profiles: ", len(department4.profiles))

    #Motorsports
    department5 = Motorsports()
    print("Num Motorsports URLs: ", len(department5.facultyURLs))    
    print("Num Motorsports Profiles: ", len(department5.profiles))

    #Systems Engineering
    department6 = Systems_Engineering()
    print("Num Systems URLs: ", len(department6.facultyURLs))    
    print("Num Systems Profiles: ", len(department6.profiles))

    #EPIC
    department7 = EPIC()
    print("Num EPIC URLs: ", len(department7.facultyURLs))    
    print("Num EPIC Profiles: ", len(department7.profiles))

    #MOSAIC
    department8 = MOSAIC()
    print("Num MOSAIC URLs: ", len(department8.facultyURLs))    
    print("Num MOSAIC Profiles: ", len(department8.profiles))

    #Student Development and Success
    department9 = Student_Development()
    print("Num Student Development URLs: ", len(department9.facultyURLs))    
    print("Num Student Development Profiles: ", len(department9.profiles))

    #Dean's Office
    department10 = Deans_Office()
    print("Num Dean URLs: ", len(department10.facultyURLs))    
    print("Num Dean Profiles: ", len(department10.profiles))
