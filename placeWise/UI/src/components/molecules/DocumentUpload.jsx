// src/components/molecules/DocumentUpload.jsx

import React, { useState } from 'react';
import { FaFileAlt } from 'react-icons/fa';

const DocumentUpload = () => {
  const [documents, setDocuments] = useState([]);

  // Maneja la carga de un nuevo documento
  const handleDocumentChange = (event) => {
    const files = Array.from(event.target.files);
    const newDocuments = files.map((file) => ({
      url: URL.createObjectURL(file),
      name: file.name,
    }));
    setDocuments((prevDocuments) => [...prevDocuments, ...newDocuments]);
  };

  return (
    <div className="flex flex-col space-y-4 mt-4">
      <div className="flex flex-wrap space-x-4">
        {documents.map((document, index) => (
          <div key={index} className="relative w-24 h-24 border border-gray-300 mb-4 flex flex-col items-center justify-center bg-gray-100">
            <div className="flex items-center justify-center flex-grow">
              <FaFileAlt className="text-gray-700 text-3xl" />
            </div>
            <div className="absolute bottom-0 w-full bg-gray-800 bg-opacity-75 text-white text-xs text-center p-1 truncate">
              {document.name}
            </div>
          </div>
        ))}
        <label className="w-24 h-24 flex items-center justify-center border-2 border-gray-300 border-dashed cursor-pointer mb-4">
          <input
            type="file"
            onChange={handleDocumentChange}
            className="hidden"
            accept=".pdf,.doc,.docx,.txt,.xls,.xlsx"
          />
          <span className="text-xl text-gray-500">+</span>
        </label>
      </div>
    </div>
  );
};

export default DocumentUpload;
