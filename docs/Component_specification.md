# Graphic Interface Specification

## Name:
- GUI for Brain Artery Visualization and Analysis (BAVA)

## Core Functionalities:

### Display Data:
- Offers real-time rendering of 3D brain artery graphs with capabilities for zooming, rotating, and panning.
- Includes multi-dimensional scaling for viewing complex data in a simplified 2D format.
- Provides layered display options to show or hide various data sets or data aspects, such as demographic overlays or clinical information.


### Data Operation:
- Support for CRUD (Create, Read, Update, Delete) operations on the data.
- Enables manipulation of visualization, including adjusting imaging thresholds and changing color maps for enhanced feature distinction.

### Filter/Search:
- Advanced filtering options to view data by various parameters like age, gender, medical condition, etc.
- Search functionality to quickly locate specific data sets or patient records using keywords or phrases.

### AI Model Interaction
- User-input based data visualization utilizing the PandasAI package.
- Allows users to write a specific query about the brain artery dataset to OpenAI's large language models
- The AI model can produce statistics or data visualizations based on the user's query.
- The AI model uses data from the backend database to provide insights to the users.

### Inputs:
- **Database:** Seamless integration with the backend database to fetch and update data.
- **User Input:** Interactive forms and controls for user input to customize data queries and visualization parameters.
- **Plot Interactions (2D + 3D):** Tools to interact with both 2D and 3D plots, including selection of regions of interest, annotations, and measurements within the graph.
- **Text Input:** Text fields for entering specific query parameters or notes.
- **Filter/Subset Input:** Dropdowns, sliders, and checkboxes for setting filters and creating data subsets.

### Outputs:
- **Plot:** Dynamic generation of plots that can be adjusted in real-time based on user interaction.
- **Stats Report:** Automated generation of statistical reports that summarize the demographic, clinical, and morphological data, with options to customize the report based on user-selected parameters.

### Integration with Other Components:
- **Retrieve Data from Database:** The GUI should have a robust backend connection to pull data from various tables and collections within the database.
- **Web-Based Application:** Creates an interactive web-based application with data tables and visualizations.
- **User’s Computer Display:** The GUI should be responsive and adaptable to different screen sizes and resolutions, ensuring a consistent user experience across devices.
