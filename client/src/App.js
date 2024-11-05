import React, { useState } from 'react';
import ArticleList from './components/ArticleList';
import './App.css';

function App() {
  const [selectedSources, setSelectedSources] = useState([]); // Stores selected sources for filtering
  const [showDropdown, setShowDropdown] = useState(false); // Manages visibility of the filter dropdown

  // List of available sources for filtering articles
  const availableSources = [
    'blockchain.news',
    'bitcoinist.com',
    'newsbtc.com',
    'cointelegraph.com',
    'reuters.com',
    'seekingalpha.com',
    'fortune.com',
    'tradingeconomics.com',
  ];

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

  // Add or remove a source from selected sources when the checkbox is toggled
  const handleSourceChange = (source) => {
    setSelectedSources((prevSelectedSources) =>
      prevSelectedSources.includes(source)
        ? prevSelectedSources.filter((s) => s !== source)
        : [...prevSelectedSources, source]
    );
  };

  return (
    <div className="App">
      <header>
        Financial Fast Feed
      </header>
      <div className="filter-container">
        <button onClick={toggleDropdown} className="filter-button">
          Filter by Source
        </button>
        <div className={`dropdown-menu ${showDropdown ? 'show' : ''}`}>
          {availableSources.map((source) => (
            <label key={source}>
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
      <div className="articles-container">
        <ArticleList selectedSources={selectedSources || []} />
      </div>
      <footer>
        <div className="left">
          <a href="https://github.com/EthanCratchley/finance-news" target="_blank" rel="noopener noreferrer">GitHub</a> | 
          <a href="mailto:ethankcratchley@gmail.com"> Contact</a> | 
          <a href="https://buymeacoffee.com/ethancratchley" target="_blank" rel="noopener noreferrer"> Donate</a>
        </div>
        <div className="middle">
          <a href="https://www.ethancratchley.com" target="_blank" rel="noopener noreferrer">
            Created by Ethan Cratchley and SFU OS Development
          </a>
        </div>
      </footer>
    </div>
  );
}

export default App;
