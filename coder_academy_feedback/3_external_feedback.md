# Technical Documentation Review — External Feedback

The first stage of this review was an internal review where team members provided feedback on how to improve the quality of the project documentation.

This internal feedback was then implemented in the documentation, before it was provided to other teams for external review.

This log includes both feedback on our project *received* from other teams, and feedback *given* to other teams regarding their projects.  

Below is example formatting of the feedback form provided:

---

## Example Feedback Form

- **Name of person providing feedback**: Jane Doe
- **Date of Feedback:** DD/MM/YYYY  
- **Feedback Type:** Received / Given  
- **Project:** Personal Expense Tracker (Team 1)
- **Does this relate to a specific document? (If so which one)?** e.g., README.md, code comments, system requirements, data storage etc
- **Feedback:** Description of the feedback  
- **Suggestions:** What changes could be made to improve the documentation
- **References:** References to related codes or acts

The team has added the below additional field under each log:

- **Proposed Actions:** How suggestions and feedback will be applied to the documentation in this project

---

## Feedback Received from Other Teams

### Log #1

**Name of person providing feedback**: Zali Bartholomew

**Date of Feedback:** 23/10/2025  

**Feedback Type:** Received  

**Project:** [Personal Expense Tracker](https://github.com/AmeliaFFF/personal-expense-tracker) - Team 1

**Does this relate to a specific document? (If so which one)?** `README.md`

**Feedback:** It would be good if, in terms of privacy and confidentiality, for the app to explain how its storing information. Other than that really clear and easy to use!

**Suggestions:** Adding some information on how it stores users data in the Readme.

**References:**

[ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics), 2018. Association for Computing Machinery. 

- ACM Principle 1.6 - Respect Privacy
- ACM Principle 1.7 - Honour Confidentiality
- ACM Principle 2.9 - Design and implement systems that are robustly and usably secure

**Proposed Actions:** Add an explicit section in the `README.md` file which explains what types of data the application collects, how it is stored and how to ensure sensitive or personal data is not compromised. Even if data is not stored, this needs to explicitly be stated in order to be transparent.

---

### Log #2

**Name of person providing feedback**: Lorena Borges

**Date of Feedback:** 21/10/2025

**Feedback Type:** Received

**Project:** [Personal Expense Tracker](https://github.com/AmeliaFFF/personal-expense-tracker) - Team 1

**Does this relate to a specific document? (If so which one)?** `README.md`

**Feedback:** Missing explicit content about Ethical Considerations when you develop an application.
  
**Suggestions:** Create a section “Ethical Considerations” aligned with academic and open-source standards, focus on user privacy, accessibility, transparency, and safety.

**References:**

[ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics), 2018. Association for Computing Machinery.

- ACM Principle 1.6 - Respect Privacy

**Proposed Actions:** Add an explicit section in the `README.md` file which discusses user privacy, accessibility, transparency, and safety. This can include reference to ACM principles, licensing, safety of packages etc.

---

### Log #3

**Name of person providing feedback**: Courtney Macgregor

**Date of Feedback:** 23/10/2025

**Feedback Type:** Received

**Project:** [Personal Expense Tracker](https://github.com/AmeliaFFF/personal-expense-tracker) - Team 1

**Does this relate to a specific document? (If so which one)?** `README.md` `example_usage.md`

**Feedback:** The README was clear and easy to follow to get the app running. The addition of the example_usage.md was great, it made navigating the app simple and complemented the README well!
  
**Suggestions:**

- `README.md`: Enclose commands like python3 app.py and source .venv/bin/activate into code blocks so they are easier to spot.
- `README.md`: For the transactions.csv file – mention the name of the file and the location the file is saved.

**References:** N/A

**Proposed Actions:**

- Add code blocks to all commands.
- Add a section to the `README.md` document providing a comprehensive overview of the transaction CSV file including naming conventions, location of file, and format of file information.

---

### Log #4

**Name of person providing feedback**: Tamara Barnes

**Date of Feedback:** 23/10/2025

**Feedback Type:** Received

**Project:** [Personal Expense Tracker](https://github.com/AmeliaFFF/personal-expense-tracker) - Team 1

**Does this relate to a specific document? (If so which one)?** `internal_review.md` `README.md`

**Feedback:** I think the feedback given to the original README file was excellent. I liked the suggested updates to the docstrings, as they provide more insight into what each function does and its overall purpose. The added explanations for class attributes, arguments, expected returns, and potential errors make the code much easier to understand and maintain. This level of detail helps users know what to expect when running the program and makes the overall codebase far more readable and user-friendly.

I absolutely loved the visual guide! This made it so easy to run the app on my device. As a visual learner, I really appreciate having screenshots and diagrams rather than just text, and this is something I’ll implement in my next project. I also liked how it was noted that the screenshots were taken on macOS via VS Code, as this is important for users on different systems (like Windows) to know.
  
**Suggestions:**

Add a “Privacy and Data Handling” section:

Although the app does not collect personal data, it’s good practice to explicitly state this for transparency and ethics. A short section could be added at the end of the README explaining that the application does not collect or store any personal information online, and that only user-entered transaction data is stored locally in a CSV file.

Include a “Troubleshooting” section:

Adding a troubleshooting section would make the README even more user-friendly, especially for users who might not be comfortable with command-line errors. This could include common issues like missing dependencies, permission errors, or invalid date formats, along with clear instructions on how to fix them. Including this would further improve the user experience and accessibility of the project.

**References:**

[ACM Code of Ethics and Professional Conduct](https://www.acm.org/code-of-ethics), 2018. Association for Computing Machinery.

- ACM Principle 1.6 - Respect Privacy
- ACM Principle 1.7 - Honour Confidentiality

**Proposed Actions:** 

- Add an explicit section in the `README.md` file which explains what types of data the application collects, how it is stored and how to ensure sensitive or personal data is not compromised. Even if data is not stored, this needs to explicitly be stated in order to be transparent.
- Add a basic 'Troubleshooting' guide for common data entry issues, invalid formats or errors. Include steps (with screenshots) of how to fix errors, or overcome issues.

---

## Feedback Provided to Other Teams

### Log #5

**Feedback Provided by:** Brando Smith

**Date of Feedback:** 23/10/2025

**Feedback Type:** Given

**Project:** [Perilous Python](https://github.com/tamarabarnes/ISK1001-Assessment_3.git) - Team 3

**What worked well?:** I read through the original README and the updated README, the latter provided a fantastic overview of the application and how to use it. It was a very professional, refined document.

It covered privacy, information storage, use, troubleshooting, system requirements etc – and when I used the application, I was able to follow the README well.

**What could be improved?:**

The only improvements I would suggest are superficial in nature:

- There were occasional spelling mistakes which makes the project feel slightly less professional.
- I also felt as a user that there was a lot of text with not a lot to break that up, both in the documentation and in the app. Being someone who gets easily overwhelmed by a lot of text, I think the success of the app could be improved by adding game graphics to the README documentation (and as suggested in your own ‘Future Development’ section some ASCII art or formatting). It would allow you to start imagining the game a lot quicker and spark more interest.

**Suggestions/Actionable Ideas:** Considering this game discusses ancient manuscripts, skeletons and the like – including quick to make graphics could enhance the readability and interest in your documentation.

---

### Log #6

**Feedback Provided by:** Amelia

**Date of Feedback:** 24/10/2025

**Feedback Type:** Given

**Project:** [Perilous Python](https://github.com/tamarabarnes/ISK1001-Assessment_3.git) - Team 3

**What worked well?:**  
For my review, I looked at `readme.md` and `updated_readme.md`. There is a huge difference between the 2 documents - I love how much your team worked on improving this! Here are some call outs for things I really liked in the `updated_readme.md` document:
- Clearly laid out and well formatted document.
- "Features of the Game" gives a nice overview of what to expect when playing this game.
- Easy to follow "Setup & Installation" guide.
- The screenshot included in the "Map & Movement" section (under "How to Play") is a great visual aid and helps with understanding the rest of the instructions.
- The "Ethical Considerations" section is excellent - very comprehensive!
- The "Libraries Utilised" section was interesting to learn more about the native Python libraries and how they can be used.
- The "Future Development" section is very cool to see what you have planned for future iterations!

**What could be improved?:**  
Overall, the `updated_readme.md` document is a huge improvement to the original `readme.md`. I can see that your team put a lot of thought into this. Therefore, the suggestions I have are minimal:
- Setup & Installation - Installation Steps:
    - Step 3 is to navigate to the project's containing folder. 
    - The command provided for this is `cd path/to/project/Python_RPG/test/main.py` (this path is for the file itself).
    - This should to be updated to `cd path/to/project/Python_RPG/test` (i.e., remove `main.py` from the end).
- How to Play:
    - This section would benefit from having some screenshots or code blocks of the terminal output (i.e., example gameplay).
    - If wanting to keep the readme streamlined, you could create an additional file (like a "Visual Guide") that shows the example gameplay.
    - This would assist users in understanding the expected output, which is useful for verifying the game is running as intended.
    - It could also assist in making the game more enjoyable, as the user can get a better idea of what to expect (e.g., pacing of the game, combat style, etc.) before they start playing the game itself.
    - Having a visual guide could also be useful for marketing purposes (i.e., being able to visually show what your application does may entice more people to want to play).
- Example Code Documentation:
    - I really like how you've explained a function and class in here, and included things like the purpose, usage, etc.
    - I would love if you included some more examples, as they're very interesting to read!

**Suggestions/Actionable Ideas:**  
The action items from the "What could be improved?" section are:
1. Update the provided command in step 3 of the "Installation Steps" section (under "Setup & Installation").
2. Create some sort of visual guide (either screenshots or code blocks) showing example gameplay.
3. Include more code explanations under the "Example Code Documentation" section.

---

### Log #7

**Feedback Provided by:** Brando Smith

**Date of Feedback:** 24/10/2025

**Feedback Type:** Given

**Project:** [Gardening Application](https://github.com/zalirae/gardening-application) - Team 2

**Feedback:**  
*(e.g., What worked, what didn't? How could we improve functionality? Is there something you wanted but wasn't there?)*

The presentation of this document is immaculate, and the explanation of each section flows so well, and articulates the purpose/vision/usage of the app perfectly. I also liked the section on accessibility, I think that was done really well.

The only feedback I have, is that the README file doesn’t explicitly show the arguments, parameters and expected returned values for classes, methods, functions (only pytests) – it summarises them (which actually looks nicer), but it could have included some more explicit code blocks so show users how this app is functioning.

In the code source file, some of the code comments could have also had further explanation – the two section then would have complimented each other well.

**Suggestions/Actions Needed:**  

- Update the README file to include code blocks explaining arguments, parameters and returned values
- Update code comments to provide a deeper understanding of how classes, functions and methods work

**References (if required):**  
*N/A*

---

### Log #8

**Feedback Provided by:** Amelia

**Date of Feedback:** 24/10/2025

**Feedback Type:** Given

**Project:** [Gardening Application](https://github.com/zalirae/gardening-application) - Team 2

**Feedback:**  
*(e.g., What worked, what didn't? How could we improve functionality? Is there something you wanted but wasn't there?)*

For my review, I looked at the the `README.md` file. Overall, I really like this document! I have included some specific feedback below:

- What worked:
    - Quickstart guide: I like how clear and easy to follow this section is, and I like your use of code blocks. I think it's great that you include the different instructions for each operating system.
    - Features: I LOVE that you included a GIF of the application in action! This is very cool to see how it runs. As a user, it's great to see what to expect up front (and as a visual learner, this is really helpful for me to better understand what the application is).
    - Data & Save File: I like how you include information about how the data is stored, and show what that file and data looks like. This is comforting to know I can check my save data so I don't lose my progress!
    - Project Structure: I like how you've broken this down visually, with the code comments explaining the purpose of each file. It's nice to know what each part does.
    - Testing: Similar to the Quickstart, I like how easy this is to follow, and how the information is presented clearly. The "useful testing commands" code block is especially helpful with those code comments explaining the commands.

- What could be improved:
    - The order of the README could be reorganised to flow better by grouping related sections together, e.g.:
        - Overview and Features (e.g., the opening section you have at the top + the "Features" section).
        - Usage (e.g., the "Quickstart" section and the "Testing" section).
        - Internal function (e.g., "How It Works", "Data & Save File", "Project Structure", etc.)
        - Legal/credits (e.g, "Ethical & Accessibility Considerations", "Licenses", "Contributors" and "References")
    - The "Packages and Dependencies" and "How It Works" sections could be combined, as there is some duplicated information about dependencies/imported libraries across these sections.
    - The "Licences" section copy/pastes the entire Colorama License. This text could be briefly summarised instead, with a link to the official license. That would reduce the length of the README, and also cover you if Colorama choose to update their license (i.e., if you're linking to the source content, it'll always be linking to the latest version, whereas a copy/pasted version could go out of date and become incorrect).
    
- What did I want that wasn't there?:
    - More examples of the application in use (this could be included as an additional file, if you don't want to bloat the README too much). As mentioned, I love that you've included the GIF! I think you could include some code blocks with copy/pasted terminal output in there too. That way, people can look through the text at their own pace (i.e., reading a code block) instead of watching the gif multiple times.

**Suggestions/Actions Needed:**  
The action items from my feedback above are:
1. Update the order of the README to group like with like (e.g., Overview and Features, Usage, Internal Function, Legal/Credits).
2. Combine the "Packages and Dependencies" and "How It Works" sections to remove duplicated information.
3. Summarise the Colorama license and link to the official Colorama license instead.
4. Include additional examples of the application in use. These could be in the form of code blocks with copy/pasted terminal output, and screenshots. Providing different forms of this content enables readers to consume it in their preferred way.

**References (if required):**  
*N/A*

---
