# Introduction-to-Machine-Learning
# My recommendation
# Option-I

Step-1: Make sure Python and pip are installed, Python in your Local computer
Any version suggestion download 1-2 old version (https://www.python.org/downloads/)
Just for check go through python --version or python3 --version
pip --version
If these commands fail, you need to install Python first: (https://www.python.org/downloads/)
Upgrade pip (optional but recommended) python -m pip install --upgrade pip

Step-2: Install Jupyter Lab via pip 
Use command pip install jupyterlab
On some systems you might need python3 -m pip install jupyterlab
Launch JupyterLab
After installation, start JupyterLab with: use command jupyter lab
This will open JupyterLab in your default web browser.
The terminal will show a URL like http://localhost:8888/lab.

# Option-II
Step-1: Download and Install Anaconda
Go to the official website: https://www.anaconda.com/download
Download:
Python 3.x (latest stable version recommended)
No need to download separate Python from python.org
Run the installer:
Select Just Me
Keep default settings
No need to manually manage pip (Anaconda handles it)
After installation, open:
Anaconda Prompt
Check installation: 
conda --version

Step-2: Create a New Environment (Recommended)
Creating a separate environment keeps your ML work clean.
conda create -n ml_env python=3.11 (for example my case) 
Activate it:
conda activate ml_env (Noted frequently will require activation)
Check Python:
python --version

Step-3: Install JupyterLab
conda install jupyterlab

Step-4: Install Machine Learning Libraries
Basic ML stack:
conda install numpy pandas matplotlib seaborn scikit-learn
For Deep Learning:
conda install pytorch torchvision torchaudio -c pytorch
conda install tensorflow
Step-5: Launch JupyterLab
jupyter lab
Browser will open automatically:
http://localhost:8888/lab




