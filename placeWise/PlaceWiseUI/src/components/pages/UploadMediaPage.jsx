// src/components/pages/UploadMediaPage.jsx

import React, { useState, useRef } from 'react';
import MainLayout from '../templates/MainLayout';
import FileUploadTemplate from '../templates/FileUploadTemplate';
import BottomNavBar from '../organisms/BottomNavBar';

const UploadMediaPage = () => {
  const [images, setImages] = useState([]);
  const [videos, setVideos] = useState([]);
  const [documents, setDocuments] = useState([]);
  const [plans, setPlans] = useState([]);
  const [experienceVideos, setExperienceVideos] = useState([]);

  const fileInputRefs = {
    Fotos: useRef(null),
    Videos: useRef(null),
    Documentos: useRef(null),
    Planos: useRef(null),
    Experiencias: useRef(null)
  };

  const handleOptionSelect = (option) => {
    if (fileInputRefs[option]) {
      fileInputRefs[option].current.click();
    }
  };

  const handleFileUpload = (event, type) => {
    const files = Array.from(event.target.files);
    const newFiles = files.map((file) => URL.createObjectURL(file));
    
    switch (type) {
      case 'Fotos':
        setImages((prev) => [...prev, ...newFiles]);
        break;
      case 'Videos':
        setVideos((prev) => [...prev, ...newFiles]);
        break;
      case 'Documentos':
        setDocuments((prev) => [...prev, ...newFiles]);
        break;
      case 'Planos':
        setPlans((prev) => [...prev, ...newFiles]);
        break;
      case 'Experiencias':
        setExperienceVideos((prev) => [...prev, ...newFiles]);
        break;
      default:
        break;
    }
  };

  return (
    <MainLayout>
      <div className="flex justify-center">
        <h1 className="mt-5 text-xl font-bold text-gray-900">Agregar Media</h1>
      </div>
      <div className="m-10 h-screen">
        <FileUploadTemplate 
          images={images}
          videos={videos}
          documents={documents}
          plans={plans}
          experienceVideos={experienceVideos}
          onFileUpload={handleFileUpload}
        />
        
        {Object.keys(fileInputRefs).map((key) => (
          <input
            key={key}
            ref={fileInputRefs[key]}
            type="file"
            onChange={(e) => handleFileUpload(e, key)}
            accept={
              key === 'Fotos' ? "image/*" :
              key === 'Videos' || key === 'Experiencias' ? "video/*" :
              ".pdf,.doc,.docx,.txt,.xls,.xlsx"
            }
            multiple
            className="hidden"
          />
        ))}
      </div>
      <BottomNavBar onOptionSelect={handleOptionSelect} />
    </MainLayout>
  );
};

export default UploadMediaPage;
