'''
Created on Oct 1, 2017

@author: Mily
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver(website):
    driver = webdriver.Firefox(executable_path=r'C:\...\geckodriver.exe')
    driver.wait = WebDriverWait(driver, 5)
    driver.get(website) #this will refresh the page..
    return driver
 
def vote_left(driver):
    winner = driver.find_element_by_css_selector("form[name=voteA] strong").text
    box = driver.wait.until(EC.presence_of_element_located((By.NAME, "voteA")))
    button = driver.wait.until(EC.element_to_be_clickable((By.NAME, "voteA")))
    button.click()
    return winner
        
def website_checks(driver,website, winner):
    assert "puppy" in driver.title, "Puppy is not in the website title!"
    assert "mily"  not in driver.title, "Mily should not be in the website title!"

    results_winner = driver.find_element_by_css_selector("td[id=results] strong").text
    assert winner == results_winner, "The winning dog is not the dog you voted for!"
    
    winner_percentage = (driver.find_element_by_css_selector("td[id=results] em").text)
    loser_percentage = (driver.find_element_by_css_selector("td[id=results] p:nth-of-type(2) em").text)

    winner_percentage = winner_percentage.replace("[","").replace("%]","")
    loser_percentage = loser_percentage.replace("[","").replace("%]","")
    
    if winner_percentage >= loser_percentage :
        print ("Good guess! {0}'s win percentage {1}% is greater than the loser's {2}%.").format(winner,winner_percentage, loser_percentage)
    else:
        print("Bad guess! {0}'s win percentage {1}% is less than the loser's {2}%.").format(winner,winner_percentage, loser_percentage)
    return
    
if __name__ == "__main__":
    website = "http://puppywar.com/"
    driver = init_driver(website)
    for i in range (1,21):
        #print("Test {0}").format(i)
        top_dog = vote_left(driver)
        website_checks(driver, website, top_dog)
  
    driver.quit()
