from utils.db_utils import get_user
from playwright.sync_api import sync_playwright

def open_and_fill_form(url, state):
    user = get_user()

    name = user[1]
    email = user[2]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Opening:", url)
        #page.goto(url)
        try:
            page.goto(url)
        except Exception as e:
            print("Failed to open URL:", e)
            browser.close()
            return

        try:
            page.fill('input[name="name"]', name)
            page.fill('input[name="email"]', email)
            print("Filled using DB data")
        except:
            print("Fields not found, skipping...")

            answer = input("Enter value manually (or press enter to skip): ")

            if answer:
                print("User provided:", answer)
            else:
                print("Skipped field")

        page.wait_for_timeout(5000)
        browser.close()