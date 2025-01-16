import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import ArticleList from './components/ArticleList';
import TermsOfService from './TermsOfService';
import './App.css';

function App() {
  const [selectedCategories, setSelectedCategories] = useState([]);
  const [selectedSources, setSelectedSources] = useState([]);
  const [showDropdown, setShowDropdown] = useState(false);

  const categories = [
    { 
      label: 'Crypto', 
      sources: [
        'cointelegraph.com', 
        'multicoin.capital', 
        'bitrss.com'
      ] 
    },
    { 
      label: 'Stocks', 
      sources: [
        'seekingalpha.com', 
        'fortune.com'
      ] 
    },
    { 
      label: 'Miscellaneous Financial News', 
      sources: [
        'finance-monthly.com',
        'benzinga.com',
        'bankpediaa.com',
        'marketbeat.com',
        'money.com',
        'moneyweek.com',
        //'europeanfinancialreview.com',
        'worldfinance.com',
        'finews.com',
      ] 
    }
  ];

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  const handleCategoryChange = (category) => {
    const sources = categories.find((c) => c.label === category).sources;

    setSelectedCategories((prev) =>
      prev.includes(category)
        ? prev.filter((c) => c !== category)
        : [...prev, category]
    );

    setSelectedSources((prev) =>
      selectedCategories.includes(category)
        ? prev.filter((source) => !sources.includes(source))
        : [...prev, ...sources]
    );
  };

  const handleSourceChange = (source) => {
    setSelectedSources((prev) =>
      prev.includes(source)
        ? prev.filter((s) => s !== source)
        : [...prev, source]
    );
  };

  const filteredSources = [...new Set(selectedSources)];

  return (
    <Router>
      <div className="App">
        <header>Financial Fast Feed</header>
        
        {/* Main Routes */}
        <Routes>
          <Route
            path="/"
            element={
              <>
                <div className="filter-container">
                  <button onClick={toggleDropdown} className="filter-button">
                    Filter by Category & Source
                  </button>
                  <div className={`dropdown-menu ${showDropdown ? 'show' : ''}`}>
                    {categories.map((category) => (
                      <div key={category.label} className="category-group">
                        <label>
                          <input
                            type="checkbox"
                            checked={selectedCategories.includes(category.label)}
                            onChange={() => handleCategoryChange(category.label)}
                          />
                          {category.label}
                        </label>
                        <div className="source-list">
                          {category.sources.map((source) => (
                            <label key={source} className="source-item">
                              <input
                                type="checkbox"
                                checked={selectedSources.includes(source)}
                                onChange={() => handleSourceChange(source)}
                              />
                              {source}
                            </label>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
                <div className="articles-container">
                  <ArticleList selectedSources={filteredSources} />
                </div>
              </>
            }
          />
          {/* TOS Page */}
          <Route path="/tos" element={<TermsOfService />} />
        </Routes>

        {/* Footer */}
        <footer>
          <div className="left">
            <a
              href="https://github.com/EthanCratchley/finance-news"
              target="_blank"
              rel="noopener noreferrer"
            >
              GitHub
            </a>{' '}
            | <a href="mailto:ethankcratchley@gmail.com"> Contact</a>
          </div>
          <div className="middle">
            <a
              href="https://www.ethancratchley.com"
              target="_blank"
              rel="noopener noreferrer"
            >
              Created by Ethan Cratchley and SFU OS Development
            </a>
          </div>
          <div className="right">
            <Link to="/tos">TOS</Link> 
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;
