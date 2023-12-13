# Brain Artery Visualization & Analysis Tool (BAVA)

BAVA is a cutting-edge online platform designed for medical researchers focusing on neurology, particularly in the study of brain artery networks. It integrates powerful visualization tools with statistical analysis and artificial intelligence (AI) capabilities to facilitate the exploration and analysis of vascular diseases.

## Features

- **3D Visualization**: Interactive 3D rendering of brain artery graphs with capabilities such as zoom, rotate, and pan to explore intricate vascular structures.
- **Data Filtering**: Advanced filtering options to refine datasets based on demographic, clinical, and morphological criteria.
- **Statistical Analysis**: Built-in tools for conducting basic statistical analysis, providing insights into the dataset through visual representations.
- **Digital Twin Simulation**: Creation of digital twins for simulated studies and analyses of brain artery networks.
- **Data Exploration**: AI models to help users explore and draw conclusions based on historical data.

## Getting Started

To get started with BAVA, please follow the instructions below:

### Prerequisites

- Ensure you have a modern web browser installed (Chrome, Firefox, Safari, Edge).
- Download and install Python on your computer.
- Have access to your OPENAI API token for AI model-based functions.

### Installation

BAVA is a web-based platform and does not require any installation. Simply fork this repository and follow the instructions in the demo video.

### Setting up locally

1. Clone/fork this repo
2. Install all pacakges using environment.yml (or setup.py)
3. Unzip subjects_all.db.zip file to data directory. It should unzip to `subjects_all.db` file (~56MB)
4. Export `PYTHONPATH` to include repo root: `export PYTHONPATH="${PYTHONPATH}:/path/to/repo/"`
5. Open terminal, start Fast API, run from repo root: `uvicorn bava.api.routers:app --reload`
6. In another terminal, start Streamlit, run from repo root: `streamlit run ./bava/streamlit/homepage.py`
7. Play around with BAVA 🧠

## Usage

1. **Data Operation**: Perform CRUD operations and manipulate visualization parameters through the GUI.
2. **Filtering Data**: Use the filter/search features to segment the data based on your research needs.
3. **Visualization**: Interact with the 3D brain artery graphs and utilize the multi-dimensional scaling features for complex datasets.
4. **Analysis**: Generate descriptive statistics and leverage the AI model for data exploration and analysis.
5. **Export**: Download your processed data and visualizations for further use or publication.

## Documentation

For detailed instructions on how to use BAVA and its features, please refer to the [User Guide](#).

Technology Review: BrainArteryNetwork/SoftwareDev/docs/TechnologyReview.pptx
Component Specification: BrainArteryNetwork/SoftwareDev/docs/Component_specification.md
Functional Specification: BrainArteryNetwork/SoftwareDev/docs/Functional_specification.md

## Contributing

We welcome contributions from the research community. If you would like to contribute, please fork the repository and submit a pull request.

## Support

If you need assistance or wish to report a bug, please email our support team at kennyz@uw.edu.

## Authors

- Kaiyu Zhang
- Sharan Ranjit S
- David Prendez
- Cherin Lim

See also the list of [contributors](#) who participated in this project.

## License

This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE.md file for details.

## Acknowledgments

- University of Washington CSE 583, Professor Dave Baker
