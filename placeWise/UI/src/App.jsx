// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import UploadMediaPage from './components/pages/UploadMediaPage';
import UploadPropertyPage from './components/pages/UploadPropertyPage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<UploadPropertyPage />} />
        <Route path="/uploadMedia" element={<UploadMediaPage />} />
      </Routes>
    </Router>
  );
};

export default App;
