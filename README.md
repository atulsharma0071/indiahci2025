# indiahci2025
AI-EPIGRAPHY: An Interactive Tool for Computational Decipherment of the Indus Valley Script




# Indus Valley Script Deciphering Tool - User Guide

## Overview
The Indus Valley Script Deciphering Tool is a comprehensive Python application for analyzing and interpreting Indus Valley script symbols. It combines statistical analysis, machine learning, and visualization to help researchers decode ancient inscriptions.

## Table of Contents
1. [Installation](#installation)
2. [Data Preparation](#data-preparation)
3. [Quick Start Guide](#quick-start-guide)
4. [Detailed Usage](#detailed-usage)
5. [Analysis Features](#analysis-features)
6. [Interpreting Results](#interpreting-results)
7. [Sample Workflow](#sample-workflow)
8. [Tips & Best Practices](#tips--best-practices)
9. [Troubleshooting](#troubleshooting)

## Installation

### Prerequisites
```bash
# Required Python packages
pip install pandas numpy matplotlib networkx scikit-learn scipy pillow sv-ttk
```

### Running the Application
```bash
python indus_valley_decipherer.py
```

## Data Preparation

### Dataset CSV Format
Your dataset should be a CSV file with the following columns:

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
- **Custom symbols**: Any Unicode characters are supported

### Directory Structure for Images
```
symbols_directory/
├── IVC_001.png
├── IVC_002.jpg
├── IVC_003.png
└── ...
```

## Quick Start Guide

### Step 1: Load Data
1. Click **File → Load Symbols Directory** to select your image folder
2. Click **File → Load Dataset** to select your CSV file
3. Verify status bar confirms successful loading

### Step 2: Build Models
1. Click **Analysis → Build Models** or use the "Build Analysis Models" button
2. Wait for model training completion (progress shown in results panel)
3. Models built include:
   - Frequency analysis
   - Positional statistics
   - Bigram transitions
   - N-gram patterns
   - Machine learning classifiers
   - Statistical significance models

### Step 3: Analyze an Inscription
1. Enter text in the input field (e.g., "A→B→C")
2. Select mode: **Inscription** or **Reading**
3. Click **Decipher Script**
4. Review results across multiple tabs:
   - **Analysis Results**: Detailed text analysis
   - **Visualizations**: Charts and networks
   - **Inscription Images**: Matching symbol images
   - **Step-by-Step Guide**: Tutorial and methodology

## Detailed Usage

### Data Loading Options
- **Load Symbols Directory**: Required for image display
- **Load Dataset CSV**: Required for all analysis
- Supported image formats: PNG, JPG, JPEG, GIF, BMP

### Analysis Parameters

#### Model Building
```python
# The tool automatically builds:
- Frequency distributions
- Positional preference maps
- Bigram transition matrices
- N-gram models (1-4 grams)
- Collocation networks
- Naive Bayes classifiers (if sufficient data)
- Statistical significance calculators
```

#### Classifier Training
- Requires at least 20 labeled examples
- Minimum 3 distinct meaning categories
- Accuracy displayed after training
- Top 10 meanings used for classification

## Analysis Features

### 1. Symbol Analysis
- **Frequency**: How often each symbol appears
- **Position**: Where symbols typically occur
- **Collocations**: Common neighboring symbols
- **Meanings**: Associated interpretations from corpus

### 2. Pattern Recognition
- **Bigrams**: Two-symbol transitions
- **N-grams**: Sequences of 2-4 symbols
- **Positional clusters**: Symbol placement preferences
- **Statistical significance**: Z-test comparisons

### 3. Machine Learning
- **Naive Bayes classifier**: Predicts meaning from symbol sequences
- **Cross-validation**: Accuracy metrics provided
- **Confidence scores**: Probability estimates for predictions

### 4. Visualization
- **Bar charts**: Frequency distributions
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

### Example 1: Basic Analysis
```python
# Input: "A→B→C" (as inscription)
1. Load dataset with known meanings
2. Build models
3. Enter "A→B→C" as inscription
4. Review frequency analysis:
   - A appears 150 times (high frequency → likely common word)
   - B appears 45 times (medium frequency → content word)
   - C appears 220 times (highest → grammatical marker)
5. Check bigram patterns:
   - A→B common (found 30 times)
   - B→C rare (found 3 times)
6. Final interpretation:
   "Offering to deity" (from corpus matches)
```

### Example 2: Comparative Analysis
```python
# Input: "X→Y→Z" (new symbol sequence)
1. Load dataset
2. Enter sequence for analysis
3. Examine positional preferences:
   - X never appears in first position
   - Y most common in middle positions
   - Z frequently at end
4. Check statistical significance:
   - X overused vs corpus
   - Y within expected range
   - Z underused
5. Synthesize evidence:
   "Unusual text with emphasis on X"
```

## Tips & Best Practices

### Data Quality
- **Consistent notation**: Use same symbol representation throughout
- **Sufficient examples**: Aim for 50+ inscriptions minimum
- **Balanced categories**: Include varied meanings and contexts
- **Clean images**: Clear, standardized symbol images

### Analysis Strategy
1. **Start simple**: Begin with short, well-attested sequences
2. **Build patterns**: Look for recurring combinations
3. **Compare contexts**: Check how symbols behave in different positions
4. **Consider exceptions**: Unusual patterns may be significant
5. **Validate findings**: Cross-reference with archaeological evidence

### Optimization Tips
- Pre-process dataset for consistent symbol encoding
- Use meaningful symbol names (not just A, B, C)
- Include contextual information (site, period)
- Regular backups of trained models
- Batch process multiple inscriptions for comparison

## Troubleshooting

### Common Issues

#### "No data available" messages
- Verify CSV file format matches expected columns
- Check for missing values in required fields
- Ensure symbol format consistency

#### Low classifier accuracy
- Increase labeled examples (>50 recommended)
- Check for imbalanced categories
- Verify meaning categories are distinct
- Consider simplifying classification schema

#### Image not displaying
- Verify image filename matches ID in "No." column
- Check image format (PNG recommended)
- Ensure directory path is correct

#### Slow performance
- Reduce dataset size for testing
- Limit n-gram range for initial analysis
- Disable visualizations for batch processing

### Error Messages

| Error | Solution |
|-------|----------|
| "Failed to load dataset" | Check CSV format and file permissions |
| "No valid symbols found" | Verify symbol encoding and separator format |
| "Insufficient data for classifier" | Add more labeled examples (min 20) |
| "Image not found" | Check filename and directory path |

## Advanced Configuration

### Customizing Analysis Parameters
You can modify the following in the source code:

```python
# Adjust n-gram range (line 311)
for n in range(1, 6):  # Change to analyze up to 5-grams

# Modify classifier thresholds (line 324)
if len(meanings) > 15 and len(set(meanings)) > 2:  # Adjust minimum requirements

# Change visualization settings (line 890)
max_size = (800, 600)  # Change image display size
```

### Extending Functionality
- Add custom analysis methods in `decipher_script()`
- Implement new visualizations in `visualize_statistics()`
- Integrate external databases via additional data loaders

## Support

### Getting Help
- Check the built-in **Step-by-Step Guide** tab
- Review console output for detailed error messages
- Verify data format matches examples
- Contact developer for specific issues

### Contributing
- Report bugs with sample data
- Suggest new analysis features
- Share successful deciphering workflows
- Contribute to test datasets

---

**Note**: This tool is designed for research assistance and should be used in conjunction with expert archaeological knowledge. Always verify results against primary sources and scholarly consensus.
