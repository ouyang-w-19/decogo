GETTING STARTED
---------------

1.  Install graphviz, Sphinx and Read the Docs theme
    
    ```
    conda install -c anaconda graphviz
    
    conda install sphinx
    
    pip install sphinx_rtd_theme
    ```
    
2.  Navigate to documentation directory
    
    ```cd docs```
     
    
3.  Build the documentation
    
    ```make html```
    
    It might be necessary to clean the previous html build by:
    
    ```make clean```
    
4.  Admire your work

    ```
    cd _build/html
    
    open index.html
    ```
    
