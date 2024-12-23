# Qwrite xpath for following
# 1. Locate the parent of an input field with
    # //*[@id='username']/parent::*

# 2. identify all child elements of a div with class container.
    # //div[@class='container']/child::*

# 3. Find all descendants ofa section With id="main-content".
    # //section[@id='main-content']/decendant::*

# 4. Locate the following sibling ofa button with id="submit"
    # //button[@id='submit']/following-sibling::*

# 5. Find the preceding sibling ofa label with for="email".
    #//label[@for='email']/preceding-sibling::*



# Q2. XPath OR/And
'''
 1. Locate an input field with either OR  id='email' or name='userEmail'
    //input[@id='email' or @name='userEmail']
 2. Find a button with both AND
    //input[@type='submit' and @class='btn-primary']

 3. Locate a link with href-"/home" OR text containing "Home".
    //link[@href='/home' or  @text='Home']

'''



# 3. ,XPatb Functions
# A. contains()
'''
1. Find an element whose id contains the word "user
    //*[contains(@id='user')]
2. Locate a button whos class contains submit-btn
    //button[contains(@class='submit-btn')]
3. Find a paragraph (<p>) with text containing "Welcome"
    //button[contains(@class='Welcome')]
    
'''


# 4. Locate a link with exact text "About Us"
# //p[text()='About Us')]

# 5. Find a span with text exactly "Submit Form".
# //span[text()='Submit Form')]


# C. starts with()
# 6. Locate an input field whose name starts with "user".
#     //input[starts-with(@name='user')]

# 7. Find a div whose id starts with "main-".
#     //div[starts-with(@id='main-')]

# 4. Mixed Challenges
# Find all descendants of a section with id="content" that contain the word "data" tn their
#     //section[@id='content']
# class.
# Locate a sibling of and hl tag with the text "Welcome" that starts With "header"
# Find all following siblings of a div with the class Item-container.
# Locate an ancestor of a paragraph tag with the text "Disclaimer"
# Find an input field with name starting with "email" and containing "Input" In Its class.
