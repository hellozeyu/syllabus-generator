### Introduction

This is a dashboard built to help professors create syllabus based on word document template. The dashboard was created using [Shiny for Python](https://shiny.rstudio.com/py/)
<hr>

### How to use the app
- Install all the dependencies by running `pip install -r requirements.txt`
- To deploy the app locally, run the following command on the terminal. `shiny run --reload app.py`
- The app will open Microsoft Word to render the file after you click the "Generate" button. It will also show the preview of the file on the main panel.
- To update the template word document, follow the documentation [here](https://docxtpl.readthedocs.io/en/latest/#) and update the Jinja2 variable under `templates/syllabus_template.docx`accordingly.