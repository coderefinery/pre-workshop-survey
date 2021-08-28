[![DOI](https://zenodo.org/badge/149784296.svg)](https://zenodo.org/badge/latestdoi/149784296)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/coderefinery/pre-workshop-survey/main)
[![License](https://img.shields.io/badge/license-%20CC--BY-blue.svg)](LICENSE)


# CodeRefinery pre-workshop survey

Participants of CodeRefinery workshops are asked to fill a pre-workshop 
survey before attending the workshop. In this survey we collect information 
on previous experience with various tools and programming practices.

The survey includes the questions [listed here](questions.md).


## License and attribution

This work is licensed under CC 4.0 BY, see the [LICENSE](LICENSE) file.

When using the data from the CodeRefinery post-workshop survey, please state following attribution:
"Post-workshop survey" by [CodeRefinery](https://coderefinery.org), licensed under CC BY 4.0.


## Processing steps
[A script](preprocess-personal.py) 
is first used to remove personal information from the registration data.
Then, a [Jupyter Notebook](pre-workshop-analysis.ipynb) is 
used to analyze the data. 

## Survey results
The main results are reported in the figures below.

#### Gender

![Gender](img/gender.png)    

#### Scientific discipline

![Gender](img/scientific-discipline.png)

#### Operating system

![OS](img/operating-system.png)    

#### Version control

![VCS](img/version-control.png)    

#### Programming experience
![experience](img/programming-experience.png)    

#### Programming languages
![languages](img/languages.png)    

#### Documentation
![documentation](img/documentation.png)    

#### Automated testing
![documentation](img/automated-testing.png)    

#### Code review
![documentation](img/code-review.png)    



