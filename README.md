# CG-rich Genome Regions Detection using Viterbi Algorithm

Solutions for detecting CG-rich and CG-poor regions in DNA sequences using Hidden Markov Models (HMM) and the Viterbi algorithm.

## Problem Description

**Case Study 1: Detecting CG-rich genome regions**

Real DNA sequences are heterogeneous throughout genomes in terms of nucleotide usage, particularly CG content. This project implements an HMM with two hidden states:
- **R** (CG-rich): Regions with high content of nucleotides C and G
- **P** (CG-poor): Regions with lower CG content

The Viterbi algorithm is used to find the most likely sequence of hidden states that explains an observed DNA sequence.

## Project Structure

```
CGrich_genome_regions/
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── Viterbi_Manual_Solution.md     # Step-by-step manual calculations
├── Viterbi_Solution.ipynb         # Jupyter notebook with implementation
└── data/
    ├── Case1 Detecting CG-rich genome regions.pdf
    ├── Annex_HMMcasestudy1.pdf
    └── Sequence_case1.txt
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Repository

```bash
git clone https://github.com/cguerreroto/CGrich_genome_regions
cd CGrich_genome_regions
```

Or download and extract the repository manually.

### Step 2: Create a Virtual Environment

Recommendation: Use a virtual environment to avoid conflicts with other Python projects:

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Or install the essential packages directly:

```bash
pip install numpy pandas jupyter
```

### Step 4: Launch Jupyter Notebook

Start Jupyter Notebook:

```bash
jupyter notebook
```

Or if you prefer JupyterLab:

```bash
jupyter lab
```

This will open a web browser with the Jupyter interface. Navigate to `Viterbi_Solution.ipynb` to run the implementation.

## Usage

### Option 1: Jupyter Notebook

1. Open `Viterbi_Solution.ipynb` in Jupyter Notebook
2. Run all cells sequentially (Cell → Run All) or step through them one by one
3. The notebook will display:
   - Step-by-step Viterbi algorithm calculations
   - Probability matrices
   - The most likely sequence of hidden states
   - Detailed analysis of CG-rich and CG-poor regions

### Option 2: Manual Solution

Review the step-by-step manual calculations in `Viterbi_Manual_Solution.md` to understand the algorithm in detail. Note: Open preview to view markdown files properly (in VSCode click on the top right corner "Open Preview" icon).

## HMM Parameters

The Hidden Markov Model is defined with the following parameters:

### Initial Probabilities
- π_R = 0.5 (CG-rich)
- π_P = 0.5 (CG-poor)

### Transition Probabilities
- a_RR = 0.5 (R → R)
- a_RP = 0.5 (R → P)
- a_PR = 0.6 (P → R)
- a_PP = 0.4 (P → P)

### Emission Probabilities

| Nucleotide | State R (CG-rich) | State P (CG-poor) |
|------------|-------------------|-------------------|
| T          | 0.2               | 0.3               |
| C          | 0.3               | 0.2               |
| A          | 0.2               | 0.3               |
| G          | 0.3               | 0.2               |

## Example: Sequence GGACTGAA

For the sequence **GGACTGAA**, the Viterbi algorithm determines the most likely hidden state sequence:

```
Observation:  G  G  A  C  T  G  A  A
Hidden State: R  R  P  R  P  R  P  P
```

**Result:** R-R-P-R-P-R-P-P

## Dependencies

The project requires the following Python packages:

- **numpy**: For numerical computations and matrix operations
- **pandas**: For data manipulation and visualization
- **jupyter**: For running the interactive notebook

See `requirements.txt` for the complete list of dependencies with versions.

## Algorithm Overview

The Viterbi algorithm is a dynamic programming algorithm that finds the most likely sequence of hidden states in an HMM. It works by:

1. **Initialization**: Calculate initial probabilities for each state
2. **Forward Pass**: For each observation, calculate the maximum probability of reaching each state
3. **Back tracking**: Trace back through the most probable path to find the optimal state sequence

## References

- [Viterbi Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Viterbi_algorithm)
- Case Study 1: Detecting CG-rich genome regions (see `data/` folder)
- Annex HMM Case Study 1 (see `data/` folder)

## License

This project is for educational purposes only. GNU General Public License v3.0 applies.

## Author

Created as part of a Mathematical Modeling course assignment on Hidden Markov Models and sequence analysis.

