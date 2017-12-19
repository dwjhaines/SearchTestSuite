###############################################################################################
#                                                                                             # 
# test_basic_search.py                                                                        #
#                                                                                             # 
# Adds a license for five users and tests that ten administrators can log in. Then repeats    #
# the test for editors and managers                                                           #
#                                                                                             #
###############################################################################################
import unittest
import time
import search_utils
import db_utils
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import pyodbc

class BasicSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        print 'Start of test: basic search'
        inst.username = "fred"
        inst.password = "quantel@"
        
        # # Set up connection to database
        # inst.connection = db_utils.connectToDb()    
        # inst.cur = inst.connection.cursor()
        
        
    def test_search_DH(self):
        searchString = "DH sQ Publish"
        # Open a browser
        print 'Opening browser........'

        # Create user and login
        self.user = search_utils.user(self.username, self.password)
        result = search_utils.login(self.user)
        if (result == 0 or result == 1):
            self.user.loggedin = True 
        time.sleep( 2 )
        
        # Select the search box
        self.user.driver.find_element_by_xpath('//*[@id="MediaListController"]/div[2]/div[1]/div[2]/button[1]').click()
        time.sleep( 2 )
        # Insert the search string into the search box
        self.user.driver.find_element_by_xpath('//*[@id="search-input-clip-bas"]').send_keys(searchString)
        time.sleep( 2 )

        print 'Search Results:'
        noMoreClips = False
        clip_index = 0
        elements = []
        
        while (noMoreClips == False):     
            try:
                element = self.user.driver.find_element_by_id("clip-index-" + str(clip_index))
            except NoSuchElementException:
                # Clip does not exist. Either there are no more clips or you have reached the end of a page
                if (clip_index % 10 == 0):
                    # End of page
                    # Scroll down another page and see if another clip exists. If so continue in main loop    
                    self.user.driver.find_element_by_xpath('//*[@id="pagination-nav"]/li[7]/a/button').click()
                    time.sleep( 5 )
                    try:
                        element = self.user.driver.find_element_by_id("clip-index-" + str(clip_index + 1))
                    except NoSuchElementException:
                        noMoreClips = True
                else: 
                    # No clip exists and not at end of page. Therefore, no more clips in list    
                    noMoreClips = True
            else:
                # Clip found. Increment index and continue
                print 'Clip ' + str(clip_index + 1) + ': ' + element.text
                elements.append (element)
                clip_index = clip_index + 1

        print
        print 'Search returned ' + str(clip_index) + ' clips'
        print
        
        # for i in range (0, len(elements)):
            # # Need to do something useful here to check the list is correct
            # print elements[i].text
        # time.sleep( 2 )

    def tearDown(inst):
        # Log out any users that were logged in and close all the browsers
        if (inst.user.loggedin == True):
            search_utils.logout(inst.user)
            inst.user.loggedin = False
        time.sleep( 1 )
        search_utils.closeBrowser(inst.user)
   
    # @classmethod
    # def tearDownClass(inst):
        # # Close connection to database
        # db_utils.closeConnection(inst.connection, inst.cur)        
    
        
if __name__ == '__main__':
    unittest.main()
    
