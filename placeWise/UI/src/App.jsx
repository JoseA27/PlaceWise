// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UploadMediaPage from './components/pages/UploadMediaPage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<UploadMediaPage />} />
      </Routes>
    </Router>
  );
};

export default App;
