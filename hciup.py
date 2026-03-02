import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import pandas as pd
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from scipy.stats import norm
from PIL import Image, ImageTk
import webbrowser
import sv_ttk  # For modern theme support

class TutorialGuide:
    def __init__(self, app):
        self.app = app
        self.create_tutorial_tab()
    
    def create_tutorial_tab(self):
        """Create the tutorial tab in the notebook"""
        self.tutorial_frame = ttk.Frame(self.app.results_notebook)
        
        # Create a canvas and scrollbar
        self.tutorial_canvas = tk.Canvas(self.tutorial_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.tutorial_frame, orient="vertical", command=self.tutorial_canvas.yview)
        
        # Configure the canvas
        self.tutorial_canvas.configure(yscrollcommand=scrollbar.set)
        self.tutorial_canvas.bind('<Configure>', lambda e: self.tutorial_canvas.configure(
            scrollregion=self.tutorial_canvas.bbox("all")))
        
        # Create a frame inside the canvas
        self.tutorial_inner_frame = ttk.Frame(self.tutorial_canvas)
        self.tutorial_canvas.create_window((0, 0), window=self.tutorial_inner_frame, anchor="nw")
        
        # Pack everything
        self.tutorial_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add to notebook
        self.app.results_notebook.add(self.tutorial_frame, text="Step-by-Step Guide")
        
        # Create tutorial content
        self.create_tutorial_content()
    
    def create_tutorial_content(self):
        """Create the tutorial content"""
        # Clear previous content
        for widget in self.tutorial_inner_frame.winfo_children():
            widget.destroy()
        
        # Tutorial header
        header = ttk.Label(self.tutorial_inner_frame, 
                         text="Indus Valley Decipherer - Step by Step Guide",
                         font=self.app.title_font)
        header.pack(pady=10, padx=10, anchor="w")
        
        # Introduction
        intro = ttk.Label(self.tutorial_inner_frame,
                         text="This guide will walk you through using the Indus Valley Script Deciphering Tool.",
                         font=self.app.normal_font,
                         wraplength=800)
        intro.pack(pady=5, padx=10, anchor="w")
        
        # Create notebook for different sections
        guide_notebook = ttk.Notebook(self.tutorial_inner_frame)
        guide_notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Step-by-step usage guide
        self.create_usage_guide(guide_notebook)
        
        # Analysis techniques
        self.create_analysis_guide(guide_notebook)
        
        # Interpretation methodology
        self.create_interpretation_guide(guide_notebook)
        
        # Sample workflow
        self.create_sample_workflow(guide_notebook)
    
    def create_usage_guide(self, notebook):
        """Create the usage guide tab"""
        frame = ttk.Frame(notebook)
        
        # Create a canvas and scrollbar for this tab
        canvas = tk.Canvas(frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        
        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        
        # Create a frame inside the canvas
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        # Pack everything
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add content
        ttk.Label(inner_frame, text="Step 1: Load Data", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="1. Click 'Load Symbols Directory' to select a folder containing inscription images\n"
                      "2. Click 'Load Dataset CSV' to load your corpus data\n"
                      "3. The dataset should contain columns for inscriptions, readings, and interpretations",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        ttk.Label(inner_frame, text="Step 2: Build Models", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="1. Click 'Build Analysis Models' to process your data\n"
                      "2. This will create statistical models and train classifiers\n"
                      "3. View basic statistics with 'Show Statistics' button",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        ttk.Label(inner_frame, text="Step 3: Analyze Inscriptions", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="1. Enter an inscription or reading in the input field\n"
                      "2. Select whether it's an 'Inscription' or 'Reading'\n"
                      "3. Click 'Decipher Script' to analyze\n"
                      "4. View results in the Analysis Results tab\n"
                      "5. See visualizations in the Visualizations tab\n"
                      "6. Check for matching images in the Inscription Images tab",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        ttk.Label(inner_frame, text="Step 4: Interpret Results", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="1. Review the statistical analysis\n"
                      "2. Check symbol frequencies and positions\n"
                      "3. Examine n-gram patterns\n"
                      "4. Consider the final interpretation synthesis\n"
                      "5. Compare with corpus matches",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Add to notebook
        notebook.add(frame, text="Usage Guide")
    
    def create_analysis_guide(self, notebook):
        """Create the analysis techniques guide"""
        frame = ttk.Frame(notebook)
        
        # Create a canvas and scrollbar for this tab
        canvas = tk.Canvas(frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        
        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        
        # Create a frame inside the canvas
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        # Pack everything
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add content
        ttk.Label(inner_frame, text="Analysis Techniques", font=self.app.header_font).pack(pady=5, anchor="w")
        
        # Frequency Analysis
        ttk.Label(inner_frame, text="Frequency Analysis", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="Examines how often each symbol appears in the corpus.\n"
                      "Key indicators:\n"
                      "- High frequency symbols may be common words or grammatical markers\n"
                      "- Low frequency symbols may be rare words or proper nouns",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Positional Analysis
        ttk.Label(inner_frame, text="Positional Analysis", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="Analyzes where symbols typically appear in sequences.\n"
                      "Key indicators:\n"
                      "- Symbols that consistently appear first may be starters\n"
                      "- Symbols that appear last may be terminators\n"
                      "- Middle positions may indicate content words",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Bigram Analysis
        ttk.Label(inner_frame, text="Bigram Analysis", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="Examines which symbols commonly appear together.\n"
                      "Key indicators:\n"
                      "- Common pairs may represent fixed phrases\n"
                      "- Rare transitions may indicate errors or special cases",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # N-gram Analysis
        ttk.Label(inner_frame, text="N-gram Analysis", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="Looks at patterns of 2-4 symbols in sequence.\n"
                      "Key indicators:\n"
                      "- Common n-grams may represent formulaic text\n"
                      "- Repeating patterns may indicate grammatical structures",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Statistical Significance
        ttk.Label(inner_frame, text="Statistical Significance", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="Uses Z-tests to compare symbol frequencies.\n"
                      "Key indicators:\n"
                      "- Overused symbols may be significant\n"
                      "- Underused symbols may be missing expected elements",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Add to notebook
        notebook.add(frame, text="Analysis Techniques")
    
    def create_interpretation_guide(self, notebook):
        """Create the interpretation methodology guide"""
        frame = ttk.Frame(notebook)
        
        # Create a canvas and scrollbar for this tab
        canvas = tk.Canvas(frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        
        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        
        # Create a frame inside the canvas
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        # Pack everything
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add content
        ttk.Label(inner_frame, text="Interpretation Methodology", font=self.app.header_font).pack(pady=5, anchor="w")
        
        # Corpus Matches
        ttk.Label(inner_frame, text="Corpus Matches", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="The tool first looks for exact or partial matches in your corpus.\n"
                      "These provide the strongest evidence when available.",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Symbol Meanings
        ttk.Label(inner_frame, text="Symbol Meanings", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="For each symbol, the tool checks any known meanings from the corpus.\n"
                      "These are combined to form preliminary interpretations.",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Pattern Analysis
        ttk.Label(inner_frame, text="Pattern Analysis", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="The tool examines:\n"
                      "- Positional preferences\n"
                      "- Collocation patterns\n"
                      "- N-gram frequencies\n"
                      "- Statistical significance",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Classifier Predictions
        ttk.Label(inner_frame, text="Classifier Predictions", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="When sufficient labeled data is available, machine learning models\n"
                      "predict interpretations based on symbol sequences.",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Final Synthesis
        ttk.Label(inner_frame, text="Final Interpretation", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="All evidence is combined with weighted confidence scores\n"
                      "to produce the most likely interpretation.",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Add to notebook
        notebook.add(frame, text="Interpretation")
    
    def create_sample_workflow(self, notebook):
        """Create a sample workflow guide"""
        frame = ttk.Frame(notebook)
        
        # Create a canvas and scrollbar for this tab
        canvas = tk.Canvas(frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        
        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        
        # Create a frame inside the canvas
        inner_frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=inner_frame, anchor="nw")
        
        # Pack everything
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Add content
        ttk.Label(inner_frame, text="Sample Workflow", font=self.app.header_font).pack(pady=5, anchor="w")
        
        # Example 1
        ttk.Label(inner_frame, text="Example 1: Simple Inscription", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="1. Load your corpus data and symbol images\n"
                      "2. Build the analysis models\n"
                      "3. Enter 'A→B→C' as an inscription\n"
                      "4. Examine the frequency analysis for each symbol\n"
                      "5. Check the bigram transitions between symbols\n"
                      "6. Review the final interpretation\n"
                      "7. Compare with any matching corpus entries",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Example 2
        ttk.Label(inner_frame, text="Example 2: Complex Analysis", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="1. After loading data, enter a longer inscription\n"
                      "2. Examine the n-gram patterns in the sequence\n"
                      "3. Check which symbols are statistically over/underused\n"
                      "4. Look at the positional preferences\n"
                      "5. Review the classifier prediction if available\n"
                      "6. Synthesize all evidence for interpretation",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Tips
        ttk.Label(inner_frame, text="Tips for Effective Analysis", font=self.app.header_font).pack(pady=5, anchor="w")
        ttk.Label(inner_frame, 
                 text="- Start with short inscriptions to build intuition\n"
                      "- Compare your results with known corpus examples\n"
                      "- Look for repeating patterns across inscriptions\n"
                      "- Note symbols that consistently appear together\n"
                      "- Consider both frequent and rare symbols\n"
                      "- Use the visualizations to spot trends",
                 font=self.app.normal_font, justify="left").pack(pady=5, padx=10, anchor="w")
        
        # Add to notebook
        notebook.add(frame, text="Sample Workflow")

class IndusValleyDecipherer:
    def __init__(self, root):
        self.root = root
        self.root.title("Indus Valley Script Deciphering Tool")
        self.root.geometry("1400x900")
        
        # Set modern theme
        sv_ttk.set_theme("light")  # Try "dark" for dark mode
        
        # Configure fonts
        self.title_font = ('Segoe UI', 16, 'bold')
        self.header_font = ('Segoe UI', 12, 'bold')
        self.normal_font = ('Segoe UI', 10)
        
        # Data storage
        self.symbols_dir = ""
        self.dataset_path = ""
        self.dataset = None
        self.symbol_images = {}
        self.known_symbols = set()
        self.image_references = {}
        
        # Models
        self.inscription_freq = Counter()
        self.reading_freq = Counter()
        self.position_stats = defaultdict(Counter)
        self.bigram_stats = Counter()
        self.meaning_map = defaultdict(list)
        self.collocation_stats = defaultdict(Counter)
        self.ngram_stats = defaultdict(Counter)
        self.classifier = None
        self.vectorizer = None
        self.inscription_classifier = None
        self.inscription_vectorizer = None
        
        # Create UI
        self.create_widgets()
        self.create_menu()
        
        # Initialize tutorial guide
        self.tutorial_guide = TutorialGuide(self)
    
    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Load Symbols Directory", command=self.load_symbols_dir)
        file_menu.add_command(label="Load Dataset", command=self.load_dataset)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Analysis menu
        analysis_menu = tk.Menu(menubar, tearoff=0)
        analysis_menu.add_command(label="Build Models", command=self.build_models)
        analysis_menu.add_command(label="Show Statistics", command=self.show_statistics)
        menubar.add_cascade(label="Analysis", menu=analysis_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Documentation", command=self.show_docs)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def show_docs(self):
        webbrowser.open("https://example.com/indus-valley-decipherer-docs")
    
    def show_about(self):
        about_window = tk.Toplevel(self.root)
        about_window.title("About")
        about_window.geometry("400x300")
        
        ttk.Label(about_window, text="Indus Valley Script Decipherer", 
                 font=self.title_font).pack(pady=10)
        
        ttk.Label(about_window, text="Version 2.0", 
                 font=self.header_font).pack()
        
        ttk.Label(about_window, text="\nA tool for analyzing and deciphering\nIndus Valley script symbols\n", 
                 font=self.normal_font).pack()
        
        ttk.Label(about_window, text="Developed by [Atul Sharma]", 
                 font=self.normal_font).pack()
        
        ttk.Button(about_window, text="Close", 
                  command=about_window.destroy).pack(pady=10)
    
    def create_widgets(self):
        # Main container with modern styling
        main_container = ttk.Frame(self.root, padding=(15, 15))
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Header with modern design
        header_frame = ttk.Frame(main_container, style='Card.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(header_frame, text="Indus Valley Script Deciphering Tool", 
                 font=self.title_font, style='Header.TLabel').pack(side=tk.LEFT, padx=10)
        
        # Body - split into left (controls) and right (results)
        body_frame = ttk.Frame(main_container)
        body_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left panel - Controls with card styling
        control_frame = ttk.LabelFrame(body_frame, text="Controls", padding=15, 
                                     style='Card.TLabelframe')
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        # Data loading section with modern icons
        data_frame = ttk.LabelFrame(control_frame, text="Data Loading", padding=10, 
                                  style='Card.TLabelframe')
        data_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(data_frame, text="Load Symbols Directory", 
                  command=self.load_symbols_dir, style='Accent.TButton').pack(fill=tk.X, pady=5)
        ttk.Button(data_frame, text="Load Dataset CSV", 
                  command=self.load_dataset, style='Accent.TButton').pack(fill=tk.X, pady=5)
        
        # Analysis section
        analysis_frame = ttk.LabelFrame(control_frame, text="Analysis", padding=10, 
                                      style='Card.TLabelframe')
        analysis_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(analysis_frame, text="Build Analysis Models", 
                  command=self.build_models, style='Accent.TButton').pack(fill=tk.X, pady=5)
        ttk.Button(analysis_frame, text="Show Statistics", 
                  command=self.show_statistics, style='Accent.TButton').pack(fill=tk.X, pady=5)
        
        # Decipher section with modern input
        decipher_frame = ttk.LabelFrame(control_frame, text="Decipher Script", padding=10, 
                                      style='Card.TLabelframe')
        decipher_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(decipher_frame, text="Input (Inscription or Reading):").pack(anchor=tk.W)
        
        self.input_text = ttk.Entry(decipher_frame, font=self.normal_font)
        self.input_text.pack(fill=tk.X, pady=(0, 10))
        
        # Modern radio buttons
        self.analysis_mode = tk.StringVar(value="inscription")
        mode_frame = ttk.Frame(decipher_frame)
        mode_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Radiobutton(mode_frame, text="Inscription", 
                       variable=self.analysis_mode, value="inscription").pack(side=tk.LEFT)
        ttk.Radiobutton(mode_frame, text="Reading", 
                       variable=self.analysis_mode, value="reading").pack(side=tk.LEFT, padx=10)
        
        ttk.Button(decipher_frame, text="Decipher Script", 
                  command=self.decipher_script, style='Accent.TButton').pack(fill=tk.X, pady=5)
        
        # Right panel - Results with modern notebook
        result_frame = ttk.Frame(body_frame, style='Card.TFrame')
        result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # Notebook for multiple tabs with modern styling
        self.results_notebook = ttk.Notebook(result_frame)
        self.results_notebook.pack(fill=tk.BOTH, expand=True)
        
        # Text results tab
        text_frame = ttk.Frame(self.results_notebook)
        self.results_text = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, 
                                                   font=self.normal_font, padx=10, pady=10)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        self.results_notebook.add(text_frame, text="Analysis Results")
        
        # Visualization tab
        vis_frame = ttk.Frame(self.results_notebook)
        self.figure = plt.Figure(figsize=(8, 6), dpi=100, facecolor='none')
        self.canvas = FigureCanvasTkAgg(self.figure, master=vis_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.results_notebook.add(vis_frame, text="Visualizations")
        
        # Image display tab with modern scrollable canvas
        self.image_frame = ttk.Frame(self.results_notebook)
        
        # Create a canvas and scrollbar
        self.image_canvas = tk.Canvas(self.image_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.image_frame, orient="vertical", command=self.image_canvas.yview)
        
        # Configure the canvas
        self.image_canvas.configure(yscrollcommand=scrollbar.set)
        self.image_canvas.bind('<Configure>', lambda e: self.image_canvas.configure(
            scrollregion=self.image_canvas.bbox("all")))
        
        # Create a frame inside the canvas
        self.image_inner_frame = ttk.Frame(self.image_canvas)
        self.image_canvas.create_window((0, 0), window=self.image_inner_frame, anchor="nw")
        
        # Pack everything
        self.image_canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.results_notebook.add(self.image_frame, text="Inscription Images")
        
        # Status bar with modern styling
        self.status_var = tk.StringVar()
        self.status_var.set("Ready. Please load data and build models.")
        ttk.Label(self.root, textvariable=self.status_var, 
                 relief=tk.SUNKEN, anchor=tk.W, style='Status.TLabel').pack(
                 fill=tk.X, side=tk.BOTTOM, ipady=2)
        
        # Configure text tags for rich text display
        self.results_text.tag_config('header', foreground='#1a73e8', font=self.header_font)
        self.results_text.tag_config('highlight', foreground='#0d652d', font=('Segoe UI', 10, 'bold'))
        self.results_text.tag_config('warning', foreground='#d93025')
        self.results_text.tag_config('normal', font=self.normal_font)
        self.results_text.tag_config('prediction', foreground='#681da8', font=('Segoe UI', 10, 'bold'))
        self.results_text.tag_config('technique', foreground='#e37400', font=('Segoe UI', 10, 'bold'))
        self.results_text.tag_config('symbol', foreground='#5c4033', font=('Segoe UI', 10, 'bold'))
        self.results_text.tag_config('interpretation', foreground='#0d652d', font=('Segoe UI', 10, 'bold'))
        
        # Configure styles for modern look
        self.style = ttk.Style()
        self.style.configure('Card.TFrame', background='white', borderwidth=1, relief='solid')
        self.style.configure('Card.TLabelframe', background='white', borderwidth=1, relief='solid')
        self.style.configure('Status.TLabel', background='#f1f3f4', foreground='#5f6368')
        self.style.configure('Accent.TButton', background='#1a73e8', foreground='white')
        self.style.map('Accent.TButton',
                     background=[('active', '#0d5bba'), ('pressed', '#0d5bba')])
    
    def tokenize_text(self, text, mode='inscription'):
        """Tokenize text into symbols based on mode"""
        if not isinstance(text, str):
            return []
        
        # Different cleaning rules for inscriptions vs readings
        if mode == 'inscription':
            cleaned = re.sub(r'[^a-zA-Z\u0250-\uFFFF\-→]', '', text)
        else:  # readings may have different conventions
            cleaned = re.sub(r'[^\w\u0250-\uFFFF\-→]', '', text)
        
        symbols = []
        i = 0
        while i < len(cleaned):
            if i+1 < len(cleaned) and cleaned[i:i+2] == '→':
                symbols.append('→')
                i += 2
            else:
                symbols.append(cleaned[i])
                i += 1
        return symbols
    
    def load_symbols_dir(self):
        """Load the directory containing inscription images"""
        self.symbols_dir = filedialog.askdirectory(title="Select Symbols Directory")
        if self.symbols_dir:
            self.status_var.set(f"Loaded symbols from: {self.symbols_dir}")
            self.append_to_results("Symbols directory loaded successfully.", 'highlight')
    
    def load_dataset(self):
        self.dataset_path = filedialog.askopenfilename(
            title="Select Dataset CSV", 
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if self.dataset_path:
            try:
                self.dataset = pd.read_csv(self.dataset_path)
                
                # Extract symbols from both inscriptions and readings
                inscription_symbols = set()
                reading_symbols = set()
                
                for _, row in self.dataset.iterrows():
                    if pd.notna(row.get('Inscription')):
                        inscription_symbols.update(self.tokenize_text(row['Inscription'], 'inscription'))
                    if pd.notna(row.get('Reading')):
                        reading_symbols.update(self.tokenize_text(row['Reading'], 'reading'))
                
                self.known_symbols = inscription_symbols.union(reading_symbols)
                
                self.status_var.set(f"Loaded dataset: {os.path.basename(self.dataset_path)}")
                self.append_to_results(f"Dataset loaded with {len(self.dataset)} records.", 'highlight')
                self.append_to_results(f"Found {len(self.known_symbols)} unique symbols in corpus.", 'normal')
                
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load dataset: {str(e)}")
                self.append_to_results(f"Error loading dataset: {str(e)}", 'warning')
    
    def build_models(self):
        if self.dataset is None:
            messagebox.showwarning("Warning", "Please load dataset first")
            return
            
        self.append_to_results("\nBuilding analysis models...", 'header')
        
        # Reset models
        self.inscription_freq = Counter()
        self.reading_freq = Counter()
        self.position_stats = defaultdict(Counter)
        self.bigram_stats = Counter()
        self.meaning_map = defaultdict(list)
        self.collocation_stats = defaultdict(Counter)
        self.ngram_stats = defaultdict(Counter)
        self.classifier = None
        self.vectorizer = None
        self.inscription_classifier = None
        self.inscription_vectorizer = None
        
        # Prepare data for machine learning models
        readings = []
        meanings = []
        inscriptions = []
        inscription_meanings = []
        
        for _, row in self.dataset.iterrows():
            # Process inscription if available
            if pd.notna(row.get('Inscription')):
                inscription = self.tokenize_text(row['Inscription'], 'inscription')
                self.inscription_freq.update(inscription)
                
                # Store meaning associations
                if pd.notna(row.get('Meaning/Interpretation')):
                    for symbol in inscription:
                        self.meaning_map[symbol].append(row['Meaning/Interpretation'])
                
                # Collect data for inscription ML models
                inscriptions.append(' '.join(inscription))
                if pd.notna(row.get('Meaning/Interpretation')):
                    inscription_meanings.append(row['Meaning/Interpretation'])
            
            # Process reading if available
            if pd.notna(row.get('Reading')):
                reading = self.tokenize_text(row['Reading'], 'reading')
                self.reading_freq.update(reading)
                
                # Build positional and bigram models
                for pos, symbol in enumerate(reading):
                    self.position_stats[pos][symbol] += 1
                
                for i in range(len(reading)-1):
                    bigram = f"{reading[i]}→{reading[i+1]}"
                    self.bigram_stats[bigram] += 1
                
                # Build collocation models
                for i in range(len(reading)):
                    context = reading[max(0,i-2):i+3]  # 2 symbols before/after
                    self.collocation_stats[reading[i]].update(context)
                
                # Build n-gram models (1-4 grams)
                for n in range(1, 5):
                    for i in range(len(reading)-n+1):
                        ngram = '→'.join(reading[i:i+n])
                        self.ngram_stats[n][ngram] += 1
                
                # Collect data for ML models
                readings.append(' '.join(reading))
                if pd.notna(row.get('Meaning/Interpretation')):
                    meanings.append(row['Meaning/Interpretation'])
        
        # Build classifier if we have enough labeled data
        if len(meanings) > 20 and len(set(meanings)) > 3:
            self.build_classifier(readings, meanings, 'reading')
        
        if len(inscription_meanings) > 20 and len(set(inscription_meanings)) > 3:
            self.build_classifier(inscriptions, inscription_meanings, 'inscription')
        
        self.append_to_results("- Inscription frequency model built", 'highlight')
        self.append_to_results("- Reading frequency model built", 'highlight')
        self.append_to_results("- Positional statistics calculated", 'highlight')
        self.append_to_results("- Bigram transition model compiled", 'highlight')
        self.append_to_results("- Collocation analysis model built", 'highlight')
        self.append_to_results("- N-gram analysis model built (1-4 grams)", 'highlight')
        self.append_to_results(f"- Meaning associations for {len(self.meaning_map)} symbols", 'highlight')
        
        if hasattr(self, 'classifier'):
            self.append_to_results("- Reading classifier trained", 'highlight')
        if hasattr(self, 'inscription_classifier'):
            self.append_to_results("- Inscription classifier trained", 'highlight')
        
        self.status_var.set("All models built successfully")
        self.visualize_frequencies()
    
    def build_classifier(self, texts, meanings, mode='reading'):
        """Build a simple classifier to predict meaning from texts"""
        try:
            # Simplify meanings to top categories
            meaning_counts = Counter(meanings)
            top_meanings = [m for m, _ in meaning_counts.most_common(10)]  # Use top 10 meanings
            
            # Filter data to only include top meanings
            X = []
            y = []
            for text, meaning in zip(texts, meanings):
                if meaning in top_meanings:
                    X.append(text)
                    y.append(meaning)
            
            if len(set(y)) < 2:  # Need at least 2 classes
                return
            
            # Vectorize the texts
            vectorizer = CountVectorizer(ngram_range=(1, 2), tokenizer=lambda x: x.split())
            X_vec = vectorizer.fit_transform(X)
            
            # Train classifier
            X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2)
            classifier = MultinomialNB()
            classifier.fit(X_train, y_train)
            
            # Calculate accuracy
            accuracy = classifier.score(X_test, y_test)
            
            if mode == 'reading':
                self.vectorizer = vectorizer
                self.classifier = classifier
                self.append_to_results(f"  Reading classifier accuracy: {accuracy:.1%}\n", 'highlight')
            else:
                self.inscription_vectorizer = vectorizer
                self.inscription_classifier = classifier
                self.append_to_results(f"  Inscription classifier accuracy: {accuracy:.1%}\n", 'highlight')
            
        except Exception as e:
            self.append_to_results(f"  Could not build {mode} classifier: {str(e)}\n", 'warning')
    
    def show_statistics(self):
        if not hasattr(self, 'inscription_freq'):
            messagebox.showwarning("Warning", "Please build models first")
            return
            
        self.results_text.delete(1.0, tk.END)
        self.append_to_results("\nSCRIPT STATISTICS\n", 'header')
        
        # Basic symbol frequencies
        self.append_to_results("\nINSCRIPTION SYMBOL FREQUENCIES:\n", 'header')
        for symbol, count in self.inscription_freq.most_common(20):
            self.append_to_results(f"{symbol}: {count} occurrences\n", 'normal')
        
        self.append_to_results("\nREADING SYMBOL FREQUENCIES:\n", 'header')
        for symbol, count in self.reading_freq.most_common(20):
            self.append_to_results(f"{symbol}: {count} occurrences\n", 'normal')
        
        # Positional preferences
        self.append_to_results("\nPOSITIONAL PREFERENCES:\n", 'header')
        for pos in sorted(self.position_stats.keys()):
            if pos < 10:  # Only show first 10 positions
                total = sum(self.position_stats[pos].values())
                self.append_to_results(f"Position {pos+1} (n={total}):\n", 'normal')
                for symbol, count in self.position_stats[pos].most_common(3):
                    self.append_to_results(f"  {symbol}: {count} ({count/total:.1%})\n", 'normal')
        
        # Common bigrams
        self.append_to_results("\nTOP BIGRAM PAIRS:\n", 'header')
        for bigram, count in self.bigram_stats.most_common(15):
            self.append_to_results(f"{bigram}: {count} occurrences\n", 'normal')
        
        # N-gram statistics
        self.append_to_results("\nTOP N-GRAMS:\n", 'header')
        for n in sorted(self.ngram_stats.keys()):
            self.append_to_results(f"{n}-grams:\n", 'highlight')
            for ngram, count in self.ngram_stats[n].most_common(5):
                self.append_to_results(f"  {ngram}: {count}\n", 'normal')
        
        self.visualize_statistics()
    
    def display_inscription_image(self, image_name, predictions=None):
        """Display the inscription image if available along with predictions"""
        # Clear previous images
        for widget in self.image_inner_frame.winfo_children():
            widget.destroy()
        
        if not self.symbols_dir or not image_name:
            ttk.Label(self.image_inner_frame, text="No image directory loaded or no image specified").pack()
            return
        
        # Create a frame for the image and predictions
        main_frame = ttk.Frame(self.image_inner_frame)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Try to find the image file
        image_path = None
        for ext in ['.png', '.jpg', '.jpeg', '.gif', '.bmp']:
            possible_path = os.path.join(self.symbols_dir, f"{image_name}")
            if os.path.exists(possible_path):
                image_path = possible_path
                break
        
        if image_path:
            try:
                img = Image.open(image_path)
                
                # Resize if too large
                max_size = (600, 400)
                if img.width > max_size[0] or img.height > max_size[1]:
                    img.thumbnail(max_size, Image.LANCZOS)
                
                photo = ImageTk.PhotoImage(img)
                
                # Store reference to prevent garbage collection
                self.image_references["current_inscription"] = photo
                
                # Display image
                image_frame = ttk.Frame(main_frame)
                image_frame.pack(side=tk.LEFT, padx=10)
                
                label = ttk.Label(image_frame, image=photo)
                label.image = photo  # Keep reference
                label.pack()
                
                ttk.Label(image_frame, text=f"Image: {os.path.basename(image_path)}").pack()
                
                # Display predictions if available
                if predictions:
                    prediction_frame = ttk.Frame(main_frame)
                    prediction_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
                    
                    ttk.Label(prediction_frame, text="Model Predictions", 
                             font=('Segoe UI', 12, 'bold')).pack(anchor=tk.W, pady=5)
                    
                    for model_name, prediction in predictions.items():
                        frame = ttk.Frame(prediction_frame)
                        frame.pack(fill=tk.X, pady=2)
                        
                        ttk.Label(frame, text=f"{model_name}:", 
                                 font=('Segoe UI', 10, 'bold')).pack(side=tk.LEFT, anchor=tk.W)
                        ttk.Label(frame, text=prediction).pack(side=tk.LEFT, padx=5)
            except Exception as e:
                ttk.Label(main_frame, text=f"Error loading image: {str(e)}").pack()
        else:
            ttk.Label(main_frame, text=f"No image found for: {image_name}").pack()
        
        # Switch to images tab
        self.results_notebook.select(self.results_notebook.index(self.image_frame))
    
    def find_matching_image(self, input_text, mode):
        """Find the image that matches the input text (either inscription or reading)"""
        if self.dataset is None or not self.symbols_dir:
            return None
        
        # Search for exact matches first
        col_name = 'Inscription' if mode == 'inscription' else 'Reading'
        matches = self.dataset[self.dataset[col_name] == input_text]
        
        if not matches.empty:
            image_name = matches.iloc[0]['No.']
            return image_name
        
        # If no exact match, try partial matches
        for _, row in self.dataset.iterrows():
            if pd.notna(row[col_name]) and input_text in row[col_name]:
                return row['No.']
        
        return None
    
    def get_model_predictions(self, input_text, mode):
        """Get predictions from different models"""
        predictions = {}
        symbols = self.tokenize_text(input_text, mode)
        
        # Frequency model prediction
        freq_predictions = []
        freq_model = self.inscription_freq if mode == 'inscription' else self.reading_freq
        total = sum(freq_model.values())
        
        for symbol in symbols:
            meanings = Counter(self.meaning_map.get(symbol, []))
            if meanings:
                freq_predictions.append(meanings.most_common(1)[0][0])
            else:
                freq_predictions.append("?")
        
        if freq_predictions:
            predictions["Frequency Model"] = " → ".join(freq_predictions)
        
        # Symbol frequency analysis
        freq_analysis = []
        for symbol in symbols:
            count = freq_model.get(symbol, 0)
            pct = count / total if total > 0 else 0
            freq_analysis.append(f"{symbol}({count})")
        
        predictions["Symbol Frequency"] = " → ".join(freq_analysis)
        
        # N-gram analysis
        if len(symbols) >= 2:
            ngram_scores = []
            for n in range(2, min(4, len(symbols)+1)):
                ngrams = ['→'.join(symbols[i:i+n]) for i in range(len(symbols)-n+1)]
                for ngram in ngrams:
                    count = self.ngram_stats[n].get(ngram, 0)
                    ngram_scores.append(f"{ngram}:{count}")
            
            if ngram_scores:
                predictions["N-gram Analysis"] = ", ".join(ngram_scores[:3])  # Show top 3
        
        # Specialized analysis based on mode
        if mode == 'reading':
            # Bigram model prediction
            if len(symbols) > 1:
                bigrams = [f"{symbols[i]}→{symbols[i+1]}" for i in range(len(symbols)-1)]
                bigram_scores = []
                for bigram in bigrams:
                    bigram_scores.append(str(self.bigram_stats.get(bigram, 0)))
                predictions["Bigram Scores"] = ", ".join(bigram_scores)
            
            # Classifier prediction
            if hasattr(self, 'classifier'):
                try:
                    X = self.vectorizer.transform([' '.join(symbols)])
                    probs = self.classifier.predict_proba(X)[0]
                    classes = self.classifier.classes_
                    top_idx = np.argmax(probs)
                    predictions["Reading Classifier"] = f"{classes[top_idx]} ({probs[top_idx]:.1%})"
                except Exception as e:
                    predictions["Reading Classifier"] = "Prediction failed"
            
            # Positional analysis
            pos_analysis = []
            for pos, symbol in enumerate(symbols):
                total = sum(self.position_stats[pos].values())
                if total > 0:
                    count = self.position_stats[pos].get(symbol, 0)
                    pos_analysis.append(f"Pos{pos+1}:{symbol}({count/total:.0%})")
            
            if pos_analysis:
                predictions["Positional Analysis"] = ", ".join(pos_analysis)
        
        else:  # inscription mode
            # Inscription classifier prediction
            if hasattr(self, 'inscription_classifier'):
                try:
                    X = self.inscription_vectorizer.transform([' '.join(symbols)])
                    probs = self.inscription_classifier.predict_proba(X)[0]
                    classes = self.inscription_classifier.classes_
                    top_idx = np.argmax(probs)
                    predictions["Inscription Classifier"] = f"{classes[top_idx]} ({probs[top_idx]:.1%})"
                except Exception as e:
                    predictions["Inscription Classifier"] = "Prediction failed"
            
            # Collocation analysis
            if len(symbols) >= 3:
                colloc_analysis = []
                for i in range(1, len(symbols)-1):
                    context = symbols[i-1:i+2]
                    colloc_analysis.append("→".join(context))
                predictions["Collocation Context"] = ", ".join(colloc_analysis)
        
        # Statistical significance analysis
        if len(symbols) >= 2:
            freq_model = self.inscription_freq if mode == 'inscription' else self.reading_freq
            total_corpus = sum(freq_model.values())
            if total_corpus > 0:
                input_freq = Counter(symbols)
                total_input = len(symbols)
                sig_symbols = []
                
                for symbol in input_freq:
                    p_corpus = freq_model.get(symbol, 0) / total_corpus
                    p_input = input_freq[symbol] / total_input
                    
                    if p_corpus > 0:
                        se = np.sqrt(p_corpus * (1 - p_corpus) / total_input)
                        z = (p_input - p_corpus) / se
                        p_value = 2 * (1 - norm.cdf(abs(z)))
                        
                        if p_value < 0.05:
                            if p_input > p_corpus:
                                sig_symbols.append(f"{symbol}(↑)")
                            else:
                                sig_symbols.append(f"{symbol}(↓)")
                
                if sig_symbols:
                    predictions["Statistical Significance"] = ", ".join(sig_symbols)
        
        return predictions
    
    def decipher_script(self):
        input_text = self.input_text.get().strip()
        if not input_text:
            messagebox.showwarning("Warning", "Please enter text to decipher")
            return
            
        self.results_text.delete(1.0, tk.END)
        self.append_to_results(f"Deciphering: '{input_text}'\n", 'header')
        
        mode = self.analysis_mode.get()
        symbols = self.tokenize_text(input_text, mode)
        self.append_to_results(f"Tokenized as {mode}: {symbols}\n\n", 'highlight')
        
        if not symbols:
            self.append_to_results("No valid symbols found in input\n", 'warning')
            return
        
        # Find matching image
        image_name = self.find_matching_image(input_text, mode)
        
        # Get model predictions
        predictions = self.get_model_predictions(input_text, mode)
        
        # Display image with predictions
        if image_name:
            self.display_inscription_image(image_name, predictions)
        else:
            # Clear image display if no image found
            for widget in self.image_inner_frame.winfo_children():
                widget.destroy()
            ttk.Label(self.image_inner_frame, text="No matching image found").pack()
            self.results_notebook.select(self.results_notebook.index(self.image_frame))
        
        # Display predictions in text results
        self.append_to_results("\nMODEL PREDICTIONS\n", 'header')
        for model_name, prediction in predictions.items():
            self.append_to_results(f"{model_name}: ", 'technique')
            self.append_to_results(f"{prediction}\n", 'prediction')
        
        # Run all analysis methods
        self.analyze_symbols(symbols, mode)
        self.analyze_with_collocations(symbols)
        self.analyze_with_ngrams(symbols)
        self.analyze_with_ztest(symbols)
        
        if mode == 'reading':
            self.analyze_positional_patterns(symbols)
            self.analyze_bigram_transitions(symbols)
            
        self.find_corpus_matches(input_text, mode)
        
        # Generate final interpretation
        self.generate_final_interpretation(symbols, mode)
        
        self.status_var.set(f"Finished deciphering as {mode}")
    
    def analyze_symbols(self, symbols, mode):
        """Analyze individual symbols with frequencies and meanings"""
        self.append_to_results("\nSYMBOL ANALYSIS\n", 'header')
        freq_model = self.inscription_freq if mode == 'inscription' else self.reading_freq
        total = sum(freq_model.values())
        
        for symbol in symbols:
            self.append_to_results(f"\nSymbol: ", 'normal')
            self.append_to_results(f"{symbol}\n", 'symbol')
            
            # Frequency analysis
            count = freq_model.get(symbol, 0)
            pct = count / total if total > 0 else 0
            self.append_to_results(f"Frequency: {count} ({pct:.1%} of {mode}s)\n", 'normal')
            
            # Meaning associations
            meanings = Counter(self.meaning_map.get(symbol, []))
            if meanings:
                self.append_to_results("Top meanings:\n", 'highlight')
                for meaning, cnt in meanings.most_common(3):
                    self.append_to_results(f"  - {meaning} ({cnt} refs)\n", 'normal')
    
    def analyze_with_collocations(self, symbols):
        """Analyze symbol collocations"""
        self.append_to_results("\nCOLLOCATION ANALYSIS\n", 'header')
        
        for i, symbol in enumerate(symbols):
            self.append_to_results(f"\nSymbol: ", 'normal')
            self.append_to_results(f"{symbol}\n", 'symbol')
            
            collocations = self.collocation_stats.get(symbol, Counter())
            if collocations:
                total = sum(collocations.values())
                self.append_to_results("Most frequent collocates:\n", 'highlight')
                for coll, count in collocations.most_common(3):
                    self.append_to_results(f"  - {coll}: {count} ({count/total:.1%})\n", 'normal')
            else:
                self.append_to_results("No collocation data available\n", 'warning')
    
    def analyze_with_ngrams(self, symbols):
        """Analyze n-gram patterns in the input"""
        self.append_to_results("\nN-GRAM ANALYSIS\n", 'header')
        
        # Analyze n-grams of different lengths in the input
        for n in range(2, min(5, len(symbols)+1)):
            self.append_to_results(f"\n{n}-grams in input:\n", 'highlight')
            
            # Get all n-grams in input
            input_ngrams = ['→'.join(symbols[i:i+n]) for i in range(len(symbols)-n+1)]
            
            for ngram in input_ngrams:
                count = self.ngram_stats[n].get(ngram, 0)
                self.append_to_results(f"  {ngram}: ", 'normal')
                
                if count > 0:
                    total_ngrams = sum(self.ngram_stats[n].values())
                    pct = count / total_ngrams
                    self.append_to_results(f"found {count} times ({pct:.1%} of all {n}-grams)\n", 'normal')
                else:
                    self.append_to_results("not found in corpus\n", 'warning')
    
    def analyze_with_ztest(self, symbols):
        """Perform Z-test to compare symbol frequencies with corpus"""
        self.append_to_results("\nSTATISTICAL SIGNIFICANCE ANALYSIS (Z-TEST)\n", 'header')
        
        if len(symbols) < 2:
            self.append_to_results("Not enough symbols for statistical analysis\n", 'warning')
            return
        
        mode = self.analysis_mode.get()
        freq_model = self.inscription_freq if mode == 'inscription' else self.reading_freq
        total_corpus = sum(freq_model.values())
        if total_corpus == 0:
            self.append_to_results("No corpus data available\n", 'warning')
            return
        
        input_freq = Counter(symbols)
        total_input = len(symbols)
        
        self.append_to_results("Comparing symbol frequencies in input vs corpus:\n", 'highlight')
        
        for symbol in input_freq:
            p_corpus = freq_model.get(symbol, 0) / total_corpus
            p_input = input_freq[symbol] / total_input
            
            if p_corpus == 0:
                self.append_to_results(f"  {symbol}: not found in corpus\n", 'warning')
                continue
            
            # Calculate Z-score
            se = np.sqrt(p_corpus * (1 - p_corpus) / total_input)
            z = (p_input - p_corpus) / se
            
            # Calculate p-value (two-tailed test)
            p_value = 2 * (1 - norm.cdf(abs(z)))
            
            self.append_to_results(f"  {symbol}: ", 'normal')
            self.append_to_results(f"Input freq={p_input:.3f}, Corpus freq={p_corpus:.3f}, ", 'normal')
            
            if p_value < 0.05:
                if p_input > p_corpus:
                    self.append_to_results("SIGNIFICANTLY OVERUSED ", 'highlight')
                else:
                    self.append_to_results("SIGNIFICANTLY UNDERUSED ", 'highlight')
                self.append_to_results(f"(p={p_value:.4f})\n", 'normal')
            else:
                self.append_to_results("not statistically significant\n", 'normal')
    
    def analyze_positional_patterns(self, symbols):
        self.append_to_results("\nPOSITIONAL ANALYSIS\n", 'header')
        
        for pos, symbol in enumerate(symbols):
            self.append_to_results(f"\nPosition {pos+1}: ", 'normal')
            self.append_to_results(f"{symbol}\n", 'symbol')
            
            total = sum(self.position_stats[pos].values())
            if total > 0:
                count = self.position_stats[pos][symbol]
                pct = count / total
                self.append_to_results(f"Appears here {count} times ({pct:.1%})\n", 'normal')
                
                common = self.position_stats[pos].most_common(3)
                self.append_to_results("Most common at this position:\n", 'highlight')
                for sym, cnt in common:
                    self.append_to_results(f"  - {sym}: {cnt} ({cnt/total:.1%})\n", 'normal')
            else:
                self.append_to_results("No data for this position\n", 'warning')
    
    def analyze_bigram_transitions(self, symbols):
        """Analyze transitions between symbols"""
        self.append_to_results("\nBIGRAM TRANSITIONS\n", 'header')
        
        for i in range(len(symbols)-1):
            current = symbols[i]
            next_sym = symbols[i+1]
            bigram = f"{current}→{next_sym}"
            
            self.append_to_results(f"\nTransition: ", 'normal')
            self.append_to_results(f"{bigram}\n", 'symbol')
            
            bigram_count = self.bigram_stats.get(bigram, 0)
            current_count = self.reading_freq.get(current, 1)
            
            self.append_to_results(f"Found {bigram_count} times\n", 'normal')
            self.append_to_results(f"{bigram_count/current_count:.1%} of '{current}' followed by '{next_sym}'\n", 'normal')
            
            if bigram_count < 3 and current_count > 5:
                alternatives = []
                for k, v in self.bigram_stats.items():
                    if k.startswith(current+'→') and v > bigram_count:
                        alternatives.append((k.split('→')[1], v))
                
                if alternatives:
                    alternatives.sort(key=lambda x: x[1], reverse=True)
                    self.append_to_results("More common alternatives:\n", 'highlight')
                    for sym, cnt in alternatives[:3]:
                        self.append_to_results(f"  - {sym}: {cnt}\n", 'normal')
    
    def find_corpus_matches(self, input_text, mode):
        """Find matching inscriptions/readings in the corpus"""
        self.append_to_results("\nCORPUS MATCHES\n", 'header')
        matches = []
        col_name = 'Inscription' if mode == 'inscription' else 'Reading'
        
        for _, row in self.dataset.iterrows():
            if pd.notna(row.get(col_name)) and input_text in row[col_name]:
                matches.append(row)
        
        if matches:
            self.append_to_results(f"Found {len(matches)} exact matches:\n", 'highlight')
            for match in matches[:3]:  # Show top 3 matches
                self.append_to_results(
                    f"  - {match.get(col_name, '')}\n"
                    f"    Site: {match.get('Site', 'Unknown')}\n"
                    f"    Interpretation: {match.get('Meaning/Interpretation', 'None')}\n",
                    'normal'
                )
        else:
            self.append_to_results("No exact matches found\n", 'warning')
    
    def generate_final_interpretation(self, symbols, mode):
        """Synthesize all evidence into final interpretation"""
        self.append_to_results("\nFINAL INTERPRETATION\n", 'header')
        
        # Collect evidence from different methods
        evidence = []
        
        # 1. Check corpus matches
        col_name = 'Inscription' if mode == 'inscription' else 'Reading'
        matches = [row for _, row in self.dataset.iterrows() 
                  if pd.notna(row.get(col_name)) and self.input_text.get().strip() in row[col_name]]
        
        if matches:
            interps = Counter([m.get('Meaning/Interpretation', '') for m in matches])
            best_match = interps.most_common(1)[0]
            evidence.append({
                'type': 'corpus_match',
                'interpretation': best_match[0],
                'confidence': min(0.9, best_match[1]/len(matches))
            })
        
        # 2. Check meaning associations
        meaning_interps = []
        for symbol in symbols:
            meanings = Counter(self.meaning_map.get(symbol, []))
            if meanings:
                best_meaning = meanings.most_common(1)[0]
                meaning_interps.append({
                    'interpretation': best_meaning[0],
                    'confidence': min(0.7, best_meaning[1]/len(self.meaning_map[symbol]))
                })
        
        if meaning_interps:
            evidence.extend(meaning_interps)
        
        # 3. Check n-gram patterns
        ngram_interps = []
        for n in range(2, min(5, len(symbols)+1)):
            ngrams = ['→'.join(symbols[i:i+n]) for i in range(len(symbols)-n+1)]
            for ngram in ngrams:
                if ngram in self.ngram_stats[n]:
                    count = self.ngram_stats[n][ngram]
                    total = sum(self.ngram_stats[n].values())
                    if count/total > 0.1:  # Only consider significant n-grams
                        ngram_interps.append({
                            'interpretation': f"Common {n}-gram pattern: {ngram}",
                            'confidence': min(0.6, count/total)
                        })
        
        if ngram_interps:
            evidence.extend(ngram_interps)
        
        # 4. Check classifier predictions
        if mode == 'reading' and hasattr(self, 'classifier'):
            try:
                X = self.vectorizer.transform([' '.join(symbols)])
                probs = self.classifier.predict_proba(X)[0]
                classes = self.classifier.classes_
                top_idx = np.argmax(probs)
                evidence.append({
                    'interpretation': classes[top_idx],
                    'confidence': min(0.8, probs[top_idx])
                })
            except:
                pass
        elif mode == 'inscription' and hasattr(self, 'inscription_classifier'):
            try:
                X = self.inscription_vectorizer.transform([' '.join(symbols)])
                probs = self.inscription_classifier.predict_proba(X)[0]
                classes = self.inscription_classifier.classes_
                top_idx = np.argmax(probs)
                evidence.append({
                    'interpretation': classes[top_idx],
                    'confidence': min(0.8, probs[top_idx])
                })
            except:
                pass
        
        # Combine evidence
        if not evidence:
            self.append_to_results("Insufficient evidence for interpretation\n", 'warning')
            return
        
        # Simple combination - in real implementation would use better weighting
        combined = Counter()
        for e in evidence:
            combined[e['interpretation']] += e['confidence']
        
        best_interp = combined.most_common(1)[0]
        self.append_to_results(f"Primary Interpretation ({best_interp[1]:.0%} confidence):\n", 'highlight')
        self.append_to_results(f"{best_interp[0]}\n", 'interpretation')
        
        if len(combined) > 1:
            self.append_to_results("\nAlternative Interpretations:\n", 'highlight')
            for interp, score in combined.most_common()[1:3]:
                self.append_to_results(f"  - {interp} ({score:.0%})\n", 'normal')
    
    def visualize_frequencies(self):
        """Visualize symbol frequencies"""
        self.figure.clear()
        
        # Create subplots
        ax1 = self.figure.add_subplot(121)
        ax2 = self.figure.add_subplot(122)
        
        # Plot inscription frequencies
        top_insc = self.inscription_freq.most_common(10)
        insc_symbols = [s[0] for s in top_insc]
        insc_counts = [s[1] for s in top_insc]
        ax1.bar(insc_symbols, insc_counts, color='steelblue')
        ax1.set_title('Top 10 Inscription Symbols')
        ax1.tick_params(axis='x', rotation=45)
        
        # Plot reading frequencies
        top_read = self.reading_freq.most_common(10)
        read_symbols = [s[0] for s in top_read]
        read_counts = [s[1] for s in top_read]
        ax2.bar(read_symbols, read_counts, color='darkgreen')
        ax2.set_title('Top 10 Reading Symbols')
        ax2.tick_params(axis='x', rotation=45)
        
        self.figure.tight_layout()
        self.canvas.draw()
        self.results_notebook.select(1)
    
    def visualize_statistics(self):
        """Visualize various statistics"""
        self.figure.clear()
        
        # Create subplots
        ax1 = self.figure.add_subplot(221)
        ax2 = self.figure.add_subplot(222)
        ax3 = self.figure.add_subplot(212)
        
        # Plot 1: Inscription frequencies
        top_insc = self.inscription_freq.most_common(10)
        insc_symbols = [s[0] for s in top_insc]
        insc_counts = [s[1] for s in top_insc]
        ax1.bar(insc_symbols, insc_counts, color='steelblue')
        ax1.set_title('Top Inscription Symbols')
        ax1.tick_params(axis='x', rotation=45)
        
        # Plot 2: Positional preferences
        pos_data = []
        for pos in sorted(self.position_stats.keys()):
            if pos < 5:  # Only show first 5 positions
                most_common = self.position_stats[pos].most_common(1)[0]
                pos_data.append((f"Pos {pos+1}", most_common[0], most_common[1]))
        
        positions = [d[0] for d in pos_data]
        symbols = [d[1] for d in pos_data]
        counts = [d[2] for d in pos_data]
        
        bars = ax2.bar(positions, counts, color='darkgreen')
        ax2.set_title('Most Common Symbols by Position')
        for i, bar in enumerate(bars):
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{symbols[i]}', ha='center', va='bottom')
        
        # Plot 3: Bigram network
        G = nx.DiGraph()
        top_bigrams = self.bigram_stats.most_common(15)
        for bigram, count in top_bigrams:
            src, tgt = bigram.split('→')
            G.add_edge(src, tgt, weight=count)
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, ax=ax3, node_size=800,
               node_color='lightblue', font_size=10, 
               edge_color='gray', width=[d['weight']/10 for (u,v,d) in G.edges(data=True)])
        ax3.set_title('Common Symbol Transitions')
        
        self.figure.tight_layout()
        self.canvas.draw()
        self.results_notebook.select(1)
    
    def append_to_results(self, text, tag='normal'):
        """Helper to append text to results with formatting"""
        self.results_text.insert(tk.END, text, tag)
        self.results_text.see(tk.END)
        self.results_text.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = IndusValleyDecipherer(root)
    root.mainloop()
