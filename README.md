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
    
    The program starts by displaying 5 options and for you to enter your choice:
    
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
    The features are as basic as it can get. Adding a task, displaying tasks, updating a task's due date, and deleting a task.
## 5. Contributing
    - Guidelines: Individuals can adhere to the following guidelines in order to contribute to the 
    Task Manager project:
    Bug Reports: Create a thorough bug report that includes instructions on how to reproduce the issue
    if you come across any bugs or other problems.
    Feature Suggestions: Make recommendations for new features or improvements by clearly outlining the
    intended functionality.
    Code Contributions: Make sure that all coding standards and guidelines are followed when submitting
    code through pull requests on the project's repository.

    - Code Style: 
    The Task Manager project follows the PEP 8 style guide for Python code. Contributors are encouraged
    to maintain uniformity in coding style, variable naming conventions, and documentation processes.

## 6. Credits
    - Authors: Aziz Nosirov, Devanshi Arora
    - Acknowledgments: https://www.youtube.com/watch?v=eDXX5evRgQw&t=861s
    
## 7. License
    - License Information: The MIT License is used to distribute the Task Manager project. According to the terms of the MIT License, users are free to use, modify, and distribute the software.
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
