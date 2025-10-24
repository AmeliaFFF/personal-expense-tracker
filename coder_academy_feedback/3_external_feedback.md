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

## Feedback Received from other Teams

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

## Feedback Provided to other Teams

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

**Feedback Provided by:**

**Date of Feedback:**

**Feedback Type:** Given

**Project:** [Perilous Python](https://github.com/tamarabarnes/ISK1001-Assessment_3.git) - Team 3

**What worked well?:**

**What could be improved?:**

**Suggestions/Actionable Ideas:**

---

### Log #7

**Feedback Provided by:**

**Date of Feedback:**

**Feedback Type:** Given

**Project:** Team 2

---

### Log #8

**Feedback Provided by:**

**Date of Feedback:**

**Feedback Type:** Given

**Project:** Team 2

---
