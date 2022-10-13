# Contributing Guide

## Notes

:smile: This is an open source project, feel free to contribute! :clap:
<br>
<br>
If you have any idea to improve we appreciate.
Some ways to contribute in this project:

- Implement new Algorithms
- Report bugs and give feedbacks

## **Making Contribution**

### **Fork and Clone Repository**

1. Visit the Repository to the Project on Github Website: "https://github.com/LucasPilla/Sorting-Algorithms-Visualizer.git"
2. Fork the repository: Click the "Fork" button on the upper right corner of the
Repo page.
3. Make a Local Clone: Clone the forked repository to your local machine (computer)

   - Click on the "Code" button on the Repo page
   - Copy the URL for the forked Repo
   - Create a Folder on your Local machine / Computer for the project Workspace
   - Open Command prompt / Terminal in the same folder location
   - In your Terminal, type:
     `git clone <forked repo url>`

### ***Install Requirements***

> cd into project directory

```bash
pip install -r requirements.txt
```

### **Add "Remote To" and "Pull From" Upstream**

4. Add a Remote to Upstream to your Repo:
   - In your terminal, type:
     `git clone < forked repo url >`
5. Pull from upstream to download all changes in the project using
    `git pull upstream main`

### **Finish assigned Task / Issue**

6. Open the Project up in your code Editor
7. Complete your assigned task / Feature on your local machine.

8. When you are ready to add and push your feature / task to the Repo,
   <!-- - Create a new branch with your feature / task name you are adding e.g "ft-Add new channel". To do this, type:
     `git checkout -b ft-Add new channel` -->
- Add your changes using:
     `git add file_name` or `git add .`
- Commit your changes to the branch with a message using
     `git commit -m "Commit message"`

<!-- - _\* Note: if the Feature is a bug fix, use `bug:message` for your branch and commit message_ -->

### **Push New Branch to "Origin" Repository**

9. To make sure there are no conflict, Pull from upstream using
    `git pull upstream main`
10. Push your branch changes to the Repo using
    `git push upstream main`

### **Create Pull Request**

11. Once you push the changes to your repo, the **_`Compare & pull request`_** button will appear in GitHub page of your repo.
12. Click the button and make your request. Leave a comment detailing all changes in your request
13. Click Create pull request to open a new pull request
