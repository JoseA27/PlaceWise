// src/components/templates/PropertyFormTemplate.jsx

import React from 'react';
import CreatePropertyForm from '../molecules/CreatePropertyForm';
import SocialIcons from '../molecules/SocialIcons';

const PropertyFormTemplate = () => (
  <div className="row-span-2">
    <CreatePropertyForm />
    <p className="block font-medium text-gray-900 text-center">
      ¿Quieres vincular esta propiedad con tu red social?
    </p>
    <SocialIcons />
  </div>
);

export default PropertyFormTemplate;
