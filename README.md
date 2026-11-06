# CogniStream – Developer Flow-State & Cognitive Load Analytics

An interactive Data Analytics project to explore developer focus, cognitive load, and productivity patterns.

## Project Overview
CogniStream analyzes developer activity indicators to understand patterns related to focus, mental workload, and productivity. It provides an interactive dashboard for exploring the generated dataset.

## Project Objectives
- Generate and prepare developer activity data.
- Perform data cleaning and validation.
- Conduct Exploratory Data Analysis (EDA).
- Visualize focus, cognitive load, and productivity patterns.
- Develop an interactive dashboard.

## Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Plotly
- Streamlit

## Dataset Description
- Total records: 1,000
- Total columns: 12
- Format: CSV
- Type: Synthetic dataset created for demonstration.

Important fields include developer ID, task type, coding hours, break minutes, interruptions, focus score, cognitive load, and productivity score.

## Key Features
- Dataset generation and cleaning
- Exploratory Data Analysis
- Focus and cognitive-load distributions
- Focus versus productivity visualization
- Correlation heatmap
- Interactive KPI cards and filters
- Developer performance summary
- Raw data exploration and CSV download

## Project Workflow
1. Generate the dataset using Python.
2. Clean and validate the data.
3. Perform exploratory data analysis.
4. Create visualizations.
5. Build and test the Streamlit dashboard.

## Project Structure
- `src/` – Dataset generation
- `data/` – Raw and cleaned datasets
- `notebooks/` – Data cleaning and EDA
- `dashboard/` – Streamlit application
- `reports/figures/` – Generated visualizations
- `docs/` – Project documentation
- `presentation/` – Presentation materials

## How to Run the Dashboard

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run dashboard/app.py
```

Open the local URL displayed in the terminal.

## Limitations
The current project uses synthetic data. Its findings are exploratory and should not be treated as conclusions about real developers.

## Future Enhancements
- Analyze real anonymized data with permission.
- Add time-based productivity trends.
- Improve dashboard filtering and analysis.
- Explore advanced analytics techniques.

## Conclusion
CogniStream demonstrates a data analytics workflow from dataset generation and cleaning to visualization and interactive dashboard development.