class StartPageConstants:
    # SIGN IN
    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_XPATH = ".//button[text()='Sign In']"
    SIGN_IN_ERROR_MESSAGE_XPATH = ".//div[@class='alert alert-danger text-center']"
    SIGN_IN_ERROR_MESSAGE_TEXT_XPATH = "Error"
    # SIGN UP
    SIGN_UP_USERNAME_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"
    # CONSTANTS FOR TC
    LINK_COMPLEX_APP_FOR_TESTING_XPATH = ".//H4"
    TEXT_REMEMBER_WRITING_MAIN_PAGE_XPATH = ".//h1"
    TEXT_ON_SUBMIT_BUTTON_XPATH = ".//button[@type='submit']"
    TEXT_ARE_YOU_SICK_OF_SHORT_XPATH = ".//p[@class='lead text-muted']"
    LINK_OUR_APP_XPATH = ".//a[@class='text-muted']"
