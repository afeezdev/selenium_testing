from selenium import webdriver
from selenium.webdriver.common.by import By


firefox_browser = webdriver.Firefox()
firefox_browser.get("https://afeezdev.pythonanywhere.com/contact.html")
firefox_browser.maximize_window()

assert 'Afeezdev\'s Portfolio' in firefox_browser.title
button_text = firefox_browser.find_elements(By.CLASS_NAME,"btn-default")

assert 'Send' in firefox_browser.page_source

email = firefox_browser.find_element(By.ID, 'email')
email.clear()
email.send_keys('talk2wale09@gmail.com')

subject = firefox_browser.find_element(By.CSS_SELECTOR, '#subject')
subject.clear()
subject.send_keys('SELENIUM TESTING')

message = firefox_browser.find_element(By.TAG_NAME, 'textarea')
message.clear()
message.send_keys("PROFILE Fullstack developer with a proven ability to adapt in both self-starting and collaborative environment while staying focused on achieving high quality results under strict deadlines using scrum, Agile, and Lean process.Innovative, Team player and Skilled in conceptualizing, designing, development and deploying software containing logical and mathematical solutions to business problems.SKILLS HTML 5, CSS3 ( SASS), JavaScript (ES6), DOM Manipulation, Typescript, Python Bootstrap / Material UI /Tailwind, Web pack / Babel Js, React Js, Firebase, React-Redux, Git / GitHub, RESTful API, JWT Auth, Node Js / Express Js, MongoDB / Mongoose / Redis, Responsive Web Design, Agile / Scrum Methodology, Single Page Application / Progressive Web Apps.")

send_button = firefox_browser.find_element(By.CSS_SELECTOR, '.btn-default')
send_button.click()

firefox_browser.close()
firefox_browser.close()
