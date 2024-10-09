// src/components/templates/FileUploadTemplate.jsx

import React from 'react';
import MultipleFileUpload from '../molecules/MultipleFileUpload';
import FileUpload from '../molecules/FileUpload';
import SaveButton from '../atoms/SaveButton';
import CancelButton from '../atoms/CancelButton';
import ImageUpload from '../molecules/ImageUpload';
import VideoUpload from '../molecules/VideoUpload';
import DocumentUpload from '../molecules/DocumentUpload';

const FileUploadTemplate = () => (
  <div className="block font-medium text-gray-900">
    <h2>Fotos de la propiedad</h2>
    <ImageUpload />
    <h2>Videos de la propiedad</h2>
    <VideoUpload />
    <h2>Documentos de la propiedad</h2>
    <DocumentUpload />
    <h2>Planos de la propiedad</h2>
    <MultipleFileUpload />
    <h2>Experiencias del sitio/Recorridos por la zona</h2>
    <MultipleFileUpload />
    <h2>Vista 3D de la propiedad</h2>
    <FileUpload />
    <div className="bg-white col-span-2 flex justify-end mt-8">
      <SaveButton />
      <CancelButton />
    </div>
  </div>
);

export default FileUploadTemplate;
