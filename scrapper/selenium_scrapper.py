from selenium import webdriver
from query import insert_annonce, connectToDatabase, disconnectDatabase
from scrap import scrap_annonce_text

# from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = r"/usr/bin/google-chrome-beta"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_driver_path = r"/usr/local/bin/chromedriver"
browser = webdriver.Chrome(chrome_driver_path, options=chrome_options)

list_ville = [330063,330039,330318,330281,330522,330550,330249,330119,330075,330056,330162,330192]

cnx = connectToDatabase()

for id_ville in range(len(list_ville)):
    for i in range(1, 2):
        browser.get(f'https://seloger.com/list.htm?tri=initial&enterprise=0&idtypebien=2,1&idtt=1&naturebien=1&ci={list_ville[id_ville]}&sort=d_dt_crea&LISTING-LISTpg={i}')
        elements = browser.find_elements_by_class_name('CoveringLink-a3s3kt-0')

        y = 1
        for e in list(elements):
            if (y % 2) != 0:
                action = webdriver.common.action_chains.ActionChains(browser)
                action.move_to_element_with_offset(e, 400, 10)
                action.click()
                action.perform()
                print(browser.window_handles)
                window_before = browser.window_handles[0]
                try:
                    window_after = browser.window_handles[1]
                except:
                    continue

                browser.switch_to.window(window_after)

                code_source = browser.page_source
                annonce = scrap_annonce_text(code_source.encode('utf-8'))
                if annonce is not None:
                    insert_annonce(cnx,annonce)
                with open(f'./data/page{list_ville[id_ville]}-{i}-{y}.html', 'wb') as f:
                    f.write(code_source.encode('utf-8'))

                browser.close()
                browser.switch_to.window(window_before)
            y += 1

disconnectDatabase(cnx)
