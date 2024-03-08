[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/545oUMxH)

### Please use the following template to add a ReadMe for your repo.

## 1. Project Title and Description
    - Title: Task Manager
    - Description: The Task Manager is a software system where you can add tasks, as well as display, update the due date, and delete any tasks no longer needed.
## 2. Installation
    - Dependencies: The dependency needed was pyodbc. It helps to use SQL SERVER programming language in a python file.
    - Installation Instructions: The library or dependency was installed through PyCharm, just like you would install any library in the IDE.
## 3. Usage
    - Examples: Include examples or code snippets to demonstrate how to use your project.
    The program starts by the program displaying 5 options and for you to enter your choice:
    
    Task Manager Menu:
    1. Create a task
    2. Display all tasks
    3. Update a task
    4. Delete a task
    5. Exit
    Enter your choice: 

    Basically, you choose between those 5 options. 
    
    To create a task, you enter a record which needs information for task title, task description, and task due date from your part. An ID gets automatically         generated for you, starting from 1 and going up 1 unit every time user creates a task. The ID being generated comes from the SQL SERVER where the table had been created, and is achieved by using IDENTITY(1,1) from TaskID INT PRIMARY KEY IDENTITY(1,1), where IDENTITY(1,1) means to increment the ID value by 1 every time a new record is entered by user from the .py file terminal.

    To display a task, user simply chooses 2 and all tasks are displayed.

    To udpate a task's due date, user enters the id of the task they want to update, followed by the new due date in YYYY-MM-DD format.

    And finally to delete a task, user enters the id of the task they want to delete and hits enter.

    When user presses 5 program terminates.
    
    - Configuration: Explain any configuration options or settings users might need to know about.
## 4. Features
    - List of Features: Outline the main features and functionalities of your project.
## 5. Contributing
    - Guidelines: Explain how others can contribute to your project, including information on submitting bug reports, feature requests, or code contributions.
    - Code Style: If applicable, provide guidelines or references to your code style.
## 6. Credits
    - Authors: List the authors or contributors of the project.
    - Acknowledgments: Mention any individuals or resources that helped inspire or support your project.
## 7. License
    - License Information: Specify the license under which your project is distributed.
## 8. Additional Sections (Optional)
    - FAQ: Include frequently asked questions and their answers.
    - Troubleshooting: Provide solutions to common issues or troubleshooting tips.
    - Roadmap: Outline the future development plans for your project.
    - Changelog: Document changes and updates to your project over time.

## Markdown Formatting Tips
  - Use headings (#, ##, ###, etc.) to structure your document.
  - Utilize lists (- or 1.) for easy-to-read information.
  - Include links to relevant resources or documentation.
  - Add code blocks using triple backticks (```) for code snippets.
  - Use images or diagrams to enhance understanding where applicable.
