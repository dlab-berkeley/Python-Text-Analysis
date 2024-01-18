# Packages required for this workshop series

This workshop introduces a number of text analysis packages, including nltk, gensim, and spaCy, along with other data wrangling and visualization packages (e.g. scikit-learn and seaborn). 

Installing some of these packages might be troublesome in your local environment. To avoid version conflict, let's create a new conda environment and install required packages from there. 

# Create new anaconda environment 

```sh
conda create --name dlab-text-analysis python=3.11.4
 ```

# Activate environment

```sh
source activate dlab-text-analysis
```

# Check version (should be 3.11.4)

```sh
python --version 
```

# Install packages

Be sure to install these specific versions to make debugging easier for everyone.

```sh
conda install nltk=3.8.1
conda install -c conda-forge spacy=3.6.1
conda install scikit-learn=1.3.0
conda install pandas=2.0.3
conda install matplotlib=3.7.1
conda install jupyter=1.0.0
conda install seaborn=0.12.2
conda install gensim=4.3.0
```

## Install spaCy English model

```sh
python -m spacy download en_core_web_sm
```

# Use Jupyter notebooks

That's it! Whenever you're ready to use a Jupyter notebook in this setup, open up the terminal and navigate to the folder containing the notebook; then activate the anlp environment to access these libraries and start up the notebook:

```sh
source activate anlp
jupyter notebook
```

