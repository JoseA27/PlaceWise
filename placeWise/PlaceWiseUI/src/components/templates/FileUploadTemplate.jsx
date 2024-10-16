// src/components/templates/FileUploadTemplate.jsx

import React from 'react';
import SaveButton from '../atoms/SaveButton';
import CancelButton from '../atoms/CancelButton';
import ImageUpload from '../molecules/ImageUpload';
import VideoUpload from '../molecules/VideoUpload';
import DocumentUpload from '../molecules/DocumentUpload';
import TextAreaField from '../atoms/TextAreaField';
import SocialIcons from '../molecules/SocialIcons';

const FileUploadTemplate = ({
  images,
  videos,
  documents,
  plans,
  experienceVideos,
  onFileUpload
}) => {
  return (
    <div className="max-w-6xl mx-auto p-4 font-medium text-gray-900 dark:text-white">
      <div className="grid gap-6 mb-8 md:grid-cols-2">
        <div>
          <h2 className="mb-2 text-lg font-semibold">Fotos de la propiedad</h2>
          <ImageUpload images={images} />
        </div>
        <div>
          <h2 className="mb-2 text-lg font-semibold">Videos de la propiedad</h2>
          <VideoUpload videos={videos} />
        </div>
        <div>
          <h2 className="mb-2 text-lg font-semibold">Documentos de la propiedad</h2>
          <DocumentUpload documents={documents} />
        </div>
        <div>
          <h2 className="mb-2 text-lg font-semibold">Planos de la propiedad</h2>
          <DocumentUpload documents={plans} />
        </div>
        <div>
          <h2 className="mb-2 text-lg font-semibold">Experiencias del sitio/Recorridos por la zona</h2>
          <TextAreaField id="descripcion" placeholder="Describa experiencias en el sitio (Opcional)..." rows={4} />
        </div>
        <div>
          <h2 className="mb-2 text-lg font-semibold">Video Experiencias del sitio/Recorridos por la zona (Opcional)</h2>
          <VideoUpload videos={experienceVideos} />
        </div>
        <div className="md:col-span-2">
          <p className="block font-medium text-gray-900 text-center">
            ¿Quieres vincular esta propiedad con tu red social?
          </p>
          <SocialIcons />
        </div>
      </div>
      <div className="flex justify-end space-x-4 mt-4 mb-16">
        <CancelButton />
        <SaveButton />
      </div>
    </div>
  );
};

export default FileUploadTemplate;
