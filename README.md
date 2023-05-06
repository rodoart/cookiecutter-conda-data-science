[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/rodolfo-arturo-gonz%C3%A1lez-trillo-93829219a/)


<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://i.ibb.co/Jyp4td6/logo.png" alt="Logo" width="80" height="80">

  <h3 align="center">Cookiecutter for Data Science Projects</h3>

  <p align="center">
    Improved template for Data Science based on <a href='https://github.com/jvelezmagic/cookiecutter-conda-data-science'>jvelezmagic</a>
    <br />
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <!--<li><a href="#license">License</a></li>-->
    <li><a href="#contact">Contact</a></li>
    <!--<li><a href="#acknowledgements">Acknowledgements</a></li>-->
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

Following the almost standard format from 
[drivendata's Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science) with useful and personal modifications.

Runing this cookiecuter produces the next structure:


    ├── LICENSE
    ├── tasks.py           <- Invoke with commands like `notebook`.
    ├── README.md          <- The top-level README for developers using this project.
    ├── install.md         <- Detailed instructions to set up this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures         <- Generated graphics and figures to be used in reporting.
    │
    ├── environment.yml    <- The requirements file for reproducing the analysis environment.
    │
    ├── .here              <- File that will stop the search if none of the other criteria
    │                         apply when searching head of project.
    │
    ├── setup.py           <- Makes project pip installable (pip install -e .)
    │                         so {{ cookiecutter.project_module_name }} can be imported.
    │
    └── {{ cookiecutter.project_module_name }}               <- Source code for use in this project.
        ├── __init__.py    <- Makes {{ cookiecutter.project_module_name }} a Python module.
        │
        ├── data           <- Scripts to download or generate data.
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling.
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions.
        │   ├── predict_model.py
        │   └── train_model.py
        │
        ├── utils          <- Scripts to help with common tasks.
            └── paths.py   <- Helper functions to relative file referencing across project.
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations.
            └── visualize.py



### Built With

* [Python](https://www.python.org/)
* [Conda](https://docs.conda.io/en/latest/)
* [Cookiecutter](https://cookiecutter.readthedocs.io/)
* [VSCode](https://code.visualstudio.com/)

<!-- GETTING STARTED -->
## Getting Started

To produce the structure you need to follow these steps.

### Prerequisites

You need to install:

* [Python](https://www.python.org/)
* [Conda](https://docs.conda.io/en/latest/)
* [Cookiecutter](https://cookiecutter.readthedocs.io/)



### Installation

1. From the terminal, inside the empty directory of the project you want to format, you must run this command:

```sh
cookiecutter https://github.com/rodoart/cookiecutter-conda-data-science
```
2. Follow the steps.

<!-- USAGE EXAMPLES -->
## Usage

Here are several projects that were made following this format:


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->

<!-- 
## License

Distributed under the MIT License. See `LICENSE` for more information.
 -->


<!-- CONTACT -->
## Contact

Rodolfo Arturo González Trillo - rodoart1 gmx.com


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/rodolfo-arturo-gonz%C3%A1lez-trillo-93829219a/



