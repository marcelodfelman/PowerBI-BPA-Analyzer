"""
TMDL Best Practices Analyzer

A tool for analyzing Power BI TMDL (Tabular Model Definition Language) files
against Microsoft's Analysis Services best practice rules.
"""

__version__ = "1.0.0"

from .tmdl_analyzer import TMDLBestPracticesAgent
from .ai_enhanced_analyzer import AIEnhancedTMDLAnalyzer

__all__ = ['TMDLBestPracticesAgent', 'AIEnhancedTMDLAnalyzer']
