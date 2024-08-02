import React from 'react';
import ArticleList from './components/ArticleList';
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
        Financial Fast Feed
      </header>
      <div className="articles-container">
        <ArticleList />
      </div>
      <footer>
        <div className="left">
          <a href="https://github.com/EthanCratchley/finance-news" target="_blank" rel="noopener noreferrer">GitHub</a> | 
          <a href="mailto:ethankcratchley@gmail.com"> Contact</a> | 
          <a href="https://buymeacoffee.com/ethancratchley" target="_blank" rel="noopener noreferrer"> Donate</a>
        </div>
        <div className="center">
          <a href="https://www.ethancratchley.com" target="_blank" rel="noopener noreferrer">
            a Ethan Cratchley production
          </a>
        </div>
      </footer>
    </div>
  );
}

export default App;
