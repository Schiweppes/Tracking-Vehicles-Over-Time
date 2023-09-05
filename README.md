<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="image_sources\tracking.gif" alt="Logo" width="540" height="360">
  </a>

<h3 align="center">Tracking Vehicles Over Time</h3>

<p align="center">
  This project is aimed to track vehicles over time by fusing measurements from LiDAR and a camera.
  <br />
  <br />
  <a href="https://www.youtube.com/watch?v=tuzf7ZrVbGA">Watch the Demo</a>
  ·
  <a href="https://github.com/Schiweppes/Tracking-Vehicles-Over-Time/issues">Report Bug</a>
  ·
  <a href="https://github.com/Schiweppes/Tracking-Vehicles-Over-Time/issues">Request Feature</a>
</p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
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
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
In this project, I employed techniques to detect objects in 3D point clouds and then used an `Extended Kalman Filter` for sensor fusion and tracking. The extended Kalman filter (EKF) is an algorithm that allows us to estimate the state of a system and track it over time using noisy measurements. By combining the strengths of both `LiDAR` and camera sensors, we were able to improve the overall accuracy and robustness of the tracking system.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![PyTorch][Pytorch]][Pytorch-url]
* [![numpy][Numpy]][Numpy-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Clone the repository on your local machine and run the `loop_over_dataset.py`. Additional configurations are provided in the `loop_over_dataset.py`.

### Prerequisites

I have provided the `requirements.txt`. I highly recommend you to create a virtual environment before installing the prerequsite libraries.

### Installation
* create a virtual environment
  ```sh
  py -m venv env
* installing all requirements at the same time 
  ```sh
  py -m pip install -r requirements.txt
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

You can try different deep learning models to evaluate the accuracy of the tracking system.(The model needs to be trained on open-source waymo dataset that can be found [here](https://waymo.com/open/download/))
And most importantly you can use it to show the effects of different filters with adjusted hyper-parameters.


<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* Deniz Temur - deniztemur00@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgements

* (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/Schiweppes/Tracking-Vehicles-Over-Time/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/Schiweppes/Tracking-Vehicles-Over-Time/forks
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/Schiweppes/Tracking-Vehicles-Over-Time/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/Schiweppes/Tracking-Vehicles-Over-Time/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/Schiweppes/Tracking-Vehicles-Over-Time/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/deniz-temur-727dt/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Pytorch]: https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white
[Pytorch-url]: https://pytorch.org/
[Matplotlib]: https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black
[Matplotlib-url]: https://matplotlib.org/
[Numpy]: https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white
[Numpy-url]: https://numpy.org/