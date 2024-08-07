import React, { useState } from 'react';
import ArticleList from './components/ArticleList';
import './App.css';

function App() {
  const [selectedSources, setSelectedSources] = useState([]);
  const [showDropdown, setShowDropdown] = useState(false);

  const availableSources = [
    'blockchain.news',
    'bitcoinist.com',
    'newsbtc.com',
    'cointelegraph.com',
    'bitcoinmagazine.com',
    'reuters.com',
    'seekingalpha.com',
    'wsj.com', // Wall Street Journal
    'fortune.com',
    'investorempires.com',
    'ft.com', // Financial Times
    'tradingeconomics.com',
    'marketwatch.com',
    'canada.ca' // Canada News Centre
  ];

  const toggleDropdown = () => {
    setShowDropdown(!showDropdown);
  };

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
            a Ethan Cratchley production
          </a>
        </div>
      </footer>
    </div>
  );
}

export default App;
