from playwright.sync_api import Playwright, sync_playwright, expect
import re
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://dev.siveo.net/mmc/")
    page.locator("input[name=\"username\"]").click()
    page.locator("input[name=\"username\"]").fill("root")
    page.locator("input[name=\"password\"]").click()
    page.locator("input[name=\"password\"]").fill("siveo")
    page.locator("text=Connecter").click()
    expect(page).to_have_url("http://dev.siveo.net/mmc/main.php?module=base&submod=main&action=default")
    page.locator("#navbarcomputers").click()
    expect(page).to_have_url("http://dev.siveo.net/mmc/main.php?module=base&submod=computers&action=machinesList")
    page.locator("#computersgroupcreator").click()
    expect(page).to_have_url("http://dev.siveo.net/mmc/main.php?module=base&submod=computers&action=computersgroupcreator")
    page.locator('tr td a >> nth=0').click()
    page.locator('.listinfos tbody tr td a >> nth=5').click()
    page.locator('//*[@id="autocomplete"]').click()
    page.locator('//*[@id="autocomplete"]').fill("win")
    page.locator("//html/body/div/div[4]/div/div[3]/form/table/tbody/tr/td[4]/input[2]").click()
    page.locator("//html/body/div/div[4]/div/div[3]/table[3]/tbody/tr/td[1]/input").click()
    page.locator("//html/body/div/div[4]/div/table[2]/tbody/tr[1]/td[1]/input").click()
    page.locator("//html/body/div/div[4]/div/table[2]/tbody/tr[1]/td[1]/input").fill("Groupe Created by playwright By Peripheral serial")
    page.locator("//html/body/div/div[4]/div/table[2]/tbody/tr[2]/td[3]/input").click()
    expect(page).to_have_url(re.compile(".*submod=computers&action=save_detail*"))
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)

