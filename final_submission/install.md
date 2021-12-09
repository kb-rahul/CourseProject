Follow the step below for installing:
---------
(Software is tested on macos)
* Install miniconda or anaconda from [here](https://docs.conda.io/en/latest/miniconda.html)
(If you already have anaconda installed, don't bother with this step)
* In your terminal, create a fresh python (3.9) environment by typing (Press y when it request you to install base packages)
```
conda create -n proj_eval python=3.9
```
* Next, activate the environment
```
conda activate proj_eval
```
* Clone the project director from github
```
git clone https://github.com/kb-rahul/CourseProject.git
```
* Navigate to the main project directory

```
cd ./CourseProject/final_submission/
```

* Install all the python dependencies for running the application by typing
```
pip install -r requirements.txt
```
* Run the application (The first run will be a little slow because it'll download the models required for inference)
```
streamlit run app.py
```
* You should see the application below:

![Image](https://github.com/kb-rahul/CourseProject/blob/main/UI.png)