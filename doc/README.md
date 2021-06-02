GETTING STARTED
---------------

1.  Install graphviz, Sphinx and Read the Docs theme
    
    ```
    conda install -c anaconda graphviz
    
    conda install sphinx
    
    pip install sphinx_rtd_theme
    ```
    
2.  Navigate to documentation directory
    
    ```cd doc```
     
3.  Change/update documentation: include all modules which have to be 
documented with ```:autosummary::``` directive in file ```sources/modules.rst```
    
4.  Build the documentation
    
    ```make html```
    
    It might be necessary to clean the previous html build by:
    
    ```make clean```
    
5.  Admire your work

    ```
    cd _build/html
    
    open index.html
    ```
    
6.  Repeat
    
    GOTO STEP 3