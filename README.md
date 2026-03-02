# indiahci2025
AI-EPIGRAPHY: An Interactive Tool for Computational Decipherment of the Indus Valley Script

For citing this work use: Atul Sharma and Shubhajit Roy Chowdhury. 2025. AI-EPIGRAPHY: An Interactive Tool for Computational Decipherment of the Indus Valley Script. In Proceedings of the 16th International Conference of Human-Computer Interaction (HCI) Design & Research (IndiaHCI '25). Association for Computing Machinery, New York, NY, USA, 69–74. https://doi.org/10.1145/3768633.3770145

# Indus Valley Script Deciphering Tool - User Guide

## Overview
The Indus Valley Script Deciphering Tool (`hciup.py`) is a comprehensive Python application for analyzing and interpreting Indus Valley script symbols. It combines statistical analysis, machine learning, and visualization to help researchers decode ancient inscriptions.

## Table of Contents
1. [Installation](#installation)
2. [Repository Files](#repository-files)
3. [Data Preparation](#data-preparation)
4. [Quick Start Guide](#quick-start-guide)
5. [Detailed Usage](#detailed-usage)
6. [Analysis Features](#analysis-features)
7. [Interpreting Results](#interpreting-results)
8. [Sample Workflow](#sample-workflow)
9. [Tips & Best Practices](#tips--best-practices)
10. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites
```bash
# Required Python packages
pip install pandas numpy matplotlib networkx scikit-learn scipy pillow sv-ttk
```

### Running the Application
```bash
# Navigate to the repository directory
cd /path/to/repository

# Run the tool
python hciup.py
```

## Repository Files

The repository contains the following files:

| File | Description |
|------|-------------|
| **`hciup.py`** | Main application code - the Indus Valley Script Deciphering Tool |
| **`indus - symbols.csv`** | Dataset containing 45 verified Indus Valley symbols with readings, meanings, and archaeological context |
| **`README.md`** | This user guide |

### 📁 Dataset Structure
The included `indus - symbols.csv` file contains:

| Column | Description | Example |
|--------|-------------|---------|
| No. | Unique identifier | IVC_001 |
| Inscription | Symbol sequence | A→B→C→D |
| Reading | Phonetic reading | a-ba-ca-da |
| Site | Archaeological site | Mohenjo-daro |
| Meaning/Interpretation | Known meaning | "Offering to deity" |
| Period | Time period | Mature Harappan |

### Symbol Format
- **Inscriptions**: Use letters for symbols, `→` for transitions (e.g., "A→B→C")
- **Readings**: Use phonetic representations (e.g., "a-ba-ca-da")
- **45 symbols**: The dataset includes 45 unique Indus Valley symbols

## Quick Start Guide

### Step 1: Run the Application
```bash
python hciup.py
```

### Step 2: Load Data
1. **Load the included dataset**: Click **File → Load Dataset** and select `indus - symbols.csv` from the repository
2. **Load Symbols Directory** (optional): Click **File → Load Symbols Directory** to select a folder containing inscription images (if available)
3. Verify status bar confirms successful loading of all 45 symbols

### Step 3: Build Models
1. Click **Analysis → Build Models** or use the "Build Analysis Models" button
2. Wait for model training completion (progress shown in results panel)
3. Models built include:
   - Frequency analysis of 45 symbols
   - Positional statistics
   - Bigram transitions
   - N-gram patterns
   - Machine learning classifiers
   - Statistical significance models

### Step 4: Analyze an Inscription
1. Enter text in the input field (e.g., "A→B→C")
2. Select mode: **Inscription** or **Reading**
3. Click **Decipher Script**
4. Review results across multiple tabs:
   - **Analysis Results**: Detailed text analysis
   - **Visualizations**: Charts and networks
   - **Inscription Images**: Matching symbol images (if available)
   - **Step-by-Step Guide**: Tutorial and methodology

## Detailed Usage

### Menu Options

#### File Menu
- **Load Symbols Directory**: Select folder with inscription images
- **Load Dataset**: Load CSV file (use `indus - symbols.csv`)
- **Exit**: Close the application

#### Analysis Menu
- **Build Models**: Process data and train all analysis models
- **Show Statistics**: Display comprehensive statistics about the corpus

#### Help Menu
- **Documentation**: Open online documentation
- **About**: Display version and developer information

### Data Loading Options
- **Load Symbols Directory**: Required for image display (optional)
- **Load Dataset CSV**: Use the included `indus - symbols.csv` (45 symbols) - **required**
- Supported image formats: PNG, JPG, JPEG, GIF, BMP

### Analysis Parameters

#### Model Building in `hciup.py`
```python
# From the source code (line 300-330):
- Frequency distributions of 45 symbols
- Positional preference maps
- Bigram transition matrices
- N-gram models (1-4 grams)
- Collocation networks
- Naive Bayes classifiers (if sufficient data)
- Statistical significance calculators
```

#### Classifier Training
- Uses the 45 labeled symbols in the dataset
- Requires at least 20 labeled examples
- Minimum 3 distinct meaning categories
- Accuracy displayed after training
- Top 10 meanings used for classification

## Analysis Features

### 1. Symbol Analysis
From `hciup.py` (lines 550-580):
- **Frequency**: How often each of the 45 symbols appears
- **Position**: Where symbols typically occur
- **Collocations**: Common neighboring symbols
- **Meanings**: Associated interpretations from corpus

### 2. Pattern Recognition
From `hciup.py` (lines 600-650):
- **Bigrams**: Two-symbol transitions
- **N-grams**: Sequences of 2-4 symbols
- **Positional clusters**: Symbol placement preferences
- **Statistical significance**: Z-test comparisons

### 3. Machine Learning
From `hciup.py` (lines 320-360):
- **Naive Bayes classifier**: Predicts meaning from symbol sequences
- **Cross-validation**: Accuracy metrics provided
- **Confidence scores**: Probability estimates for predictions

### 4. Visualization
From `hciup.py` (lines 880-950):
- **Bar charts**: Frequency distributions of all 45 symbols
- **Network graphs**: Symbol transition networks
- **Position heatmaps**: Symbol placement preferences
- **N-gram timelines**: Pattern evolution

## Interpreting Results

### Confidence Indicators
- **High confidence (70-100%)**: Strong corpus evidence
- **Medium confidence (40-69%)**: Multiple supporting patterns
- **Low confidence (<40%)**: Insufficient evidence

### Result Components

#### Symbol Analysis Output
```
Symbol: A
Frequency: 150 (12.5% of readings)
Top meanings:
  - deity (45 refs)
  - water (30 refs)
  - offering (22 refs)
```

#### Statistical Significance
```
Symbol A: Input freq=0.250, Corpus freq=0.125
  SIGNIFICANTLY OVERUSED (p=0.0032)
```

#### Final Interpretation
```
Primary Interpretation (85% confidence):
"Offering to water deity"

Alternative Interpretations:
  - Sacred water ritual (72%)
  - Deity worship (68%)
```

## Sample Workflow

### Example 1: Basic Analysis with Included Dataset
```python
# From hciup.py - Example usage
1. python hciup.py
2. File → Load Dataset → select "indus - symbols.csv"
3. Analysis → Build Models
4. Enter "A→B→C" in input field
5. Select "Inscription" mode
6. Click "Decipher Script"

# Expected output in Analysis Results tab:
Tokenized as inscription: ['A', '→', 'B', '→', 'C']

SYMBOL ANALYSIS
Symbol: A
Frequency: 45 (12.5% of readings)
Top meanings:
  - deity (15 refs)
  - water (10 refs)

FINAL INTERPRETATION
Primary Interpretation (85% confidence):
"Offering to deity"
```

### Example 2: Reading Analysis
```python
# Analyze a phonetic reading
1. Enter "a-ba-ca" in input field
2. Select "Reading" mode
3. Click "Decipher Script"

# Check Bigram Transitions
BIGRAM TRANSITIONS
Transition: a→ba
Found 12 times
80% of 'a' followed by 'ba'

# Positional Analysis
Position 1: a
Appears here 25 times (45% of readings)
```

## Tips & Best Practices

### Data Quality
- **Use included dataset**: Start with `indus - symbols.csv` (45 verified symbols)
- **Consistent notation**: Use same symbol representation throughout
- **Sufficient examples**: Dataset provides 45 symbols with multiple occurrences
- **Balanced categories**: Includes varied meanings and contexts

### Analysis Strategy
1. **Start simple**: Begin with short sequences from the 45 symbols
2. **Build patterns**: Look for recurring combinations
3. **Compare contexts**: Check how symbols behave in different positions
4. **Consider exceptions**: Unusual patterns may be significant
5. **Validate findings**: Cross-reference with archaeological evidence

### Optimization Tips
- Use the provided dataset structure as template for additional data
- Maintain consistent symbol encoding
- Include contextual information (site, period)
- Regular backups of trained models
- Batch process multiple inscriptions for comparison

## Code Structure Reference

### Key Functions in `hciup.py`

| Function | Line | Description |
|----------|------|-------------|
| `load_dataset()` | 250-280 | Loads `indus - symbols.csv` |
| `build_models()` | 300-360 | Builds all analysis models |
| `decipher_script()` | 450-500 | Main analysis function |
| `analyze_symbols()` | 550-580 | Individual symbol analysis |
| `analyze_with_ngrams()` | 600-630 | N-gram pattern detection |
| `analyze_with_ztest()` | 640-680 | Statistical significance |
| `visualize_frequencies()` | 880-910 | Creates frequency charts |
| `generate_final_interpretation()` | 780-850 | Synthesizes all evidence |

## Troubleshooting

### Common Issues

#### "No data available" messages
- Verify you've loaded `indus - symbols.csv` from the repository
- Check CSV format matches expected columns
- Ensure no missing values in required fields
- Verify symbol format consistency

#### Low classifier accuracy
- Dataset of 45 symbols provides good baseline
- Consider adding more labeled examples
- Check for imbalanced categories
- Verify meaning categories are distinct

#### Image not displaying
- Verify image filename matches ID in "No." column
- Check image format (PNG recommended)
- Ensure directory path is correct
- Note: Images are optional, text analysis works without them

#### Slow performance
- Reduce dataset size for testing
- Limit n-gram range for initial analysis
- Disable visualizations for batch processing

### Error Messages

| Error | Solution |
|-------|----------|
| "Failed to load dataset" | Check `indus - symbols.csv` format and file permissions |
| "No valid symbols found" | Verify symbol encoding and separator format (use →) |
| "Insufficient data for classifier" | Add more labeled examples beyond the 45 symbols |
| "Image not found" | Image display is optional, text analysis still works |

## Resources

### Repository Files
- **`hciup.py`**: Main application code
- **`indus - symbols.csv`**: Dataset of 45 verified Indus Valley symbols
- **`README.md`**: This user guide

### Dataset Structure
```csv
No.,Inscription,Reading,Site,Meaning/Interpretation,Period
IVC_001,A→B→C→D,a-ba-ca-da,Mohenjo-daro,"Offering to deity",Mature Harappan
IVC_002,E→F→G→H,e-fe-ge-he,Harappa,"Royal seal",Mature Harappan
...
```

## Support

### Getting Help
- Check the built-in **Step-by-Step Guide** tab in the application
- Review console output for detailed error messages
- Verify data format matches `indus - symbols.csv`
- Use the provided 45 symbols for baseline testing
- Contact developer for specific issues

### Contributing
- Report bugs with sample data
- Suggest new analysis features
- Share successful deciphering workflows
- Contribute to expanding the symbol dataset beyond 45

---

**Note**: This tool (`hciup.py`) is designed for research assistance and should be used in conjunction with expert archaeological knowledge. Always verify results against primary sources and scholarly consensus. The included `indus - symbols.csv` provides a foundation of 45 verified symbols for testing and analysis.
