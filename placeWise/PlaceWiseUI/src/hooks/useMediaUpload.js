// Este codigo no es funcional, es solo un ejemplo de como se podria implementar un hook para subir archivos a un servidor

import { useState } from 'react';
import axios from 'axios';

const useMediaUpload = (uploadUrl) => {
    const [uploadProgress, setUploadProgress] = useState(0);
    const [isUploading, setIsUploading] = useState(false);
    const [error, setError] = useState(null);

    const uploadMedia = async (file) => {
        setIsUploading(true);
        setUploadProgress(0);
        setError(null);

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post(uploadUrl, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
                onUploadProgress: (progressEvent) => {
                    const progress = Math.round((progressEvent.loaded * 100) / progressEvent.total);
                    setUploadProgress(progress);
                },
            });

            setIsUploading(false);
            return response.data;
        } catch (err) {
            setError(err);
            setIsUploading(false);
            throw err;
        }
    };

    return {
        uploadMedia,
        uploadProgress,
        isUploading,
        error,
    };
};

export default useMediaUpload;